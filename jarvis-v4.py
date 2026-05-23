import speech_recognition as sr
import pyttsx3
import subprocess
import json
import psutil
import os
import time

# ---------- TTS ----------
engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# ---------- Speech ----------
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You:", command)
        return command
    except:
        return ""

# ---------- Sessions ----------
SESSION_DIR = "sessions"
LAST_SESSION = os.path.join(SESSION_DIR, "last.json")

if not os.path.exists(SESSION_DIR):
    os.makedirs(SESSION_DIR)

running_processes = []

# ---------- Open App ----------
def open_app(app_name):
    try:
        proc = subprocess.Popen(f'start "" "{app_name}"', shell=True)
        speak(f"Opening {app_name}")

        running_processes.append({
            "name": app_name,
            "pid": proc.pid
        })

    except:
        speak("App not found")

# ---------- Close Apps ----------
def close_apps():
    for proc in running_processes:
        try:
            p = psutil.Process(proc["pid"])
            p.terminate()
        except:
            pass

    running_processes.clear()
    speak("All apps closed")

# ---------- Save Session ----------
def save_session(filename):
    with open(filename, "w") as f:
        json.dump(running_processes, f)

# ---------- Load Session ----------
def load_session(filename):
    if not os.path.exists(filename):
        speak("Session not found")
        return

    with open(filename, "r") as f:
        data = json.load(f)

    for app in data:
        try:
            subprocess.Popen(f'start "" "{app["name"]}"', shell=True)
        except:
            pass

    speak("Session restored")

# ---------- Command Handler ----------
def handle_command(command):

    # ---------- OPEN ----------
    if "open" in command:
        app_name = command.replace("open", "").strip()
        open_app(app_name)

    # ---------- SAVE CUSTOM ----------
    elif "save in" in command:
        name = command.replace("save in", "").strip()
        file = os.path.join(SESSION_DIR, f"{name}.json")

        save_session(file)
        close_apps()

        speak(f"Saved in {name} session")

    # ---------- LOAD CUSTOM ----------
    elif "it's" in command and "time" in command:
        name = command.replace("it's", "").replace("time", "").strip()
        file = os.path.join(SESSION_DIR, f"{name}.json")

        load_session(file)

    # ---------- LAST SESSION ----------
    elif "wake up daddy's home" in command:
        load_session(LAST_SESSION)

    # ---------- GOOD NIGHT ----------
    elif "good night" in command:
        # overwrite last session
        if os.path.exists(LAST_SESSION):
            os.remove(LAST_SESSION)

        save_session(LAST_SESSION)
        close_apps()

        speak("Good night. Session saved.")

    else:
        speak("I didn't understand")

# ---------- Main Loop ----------
def main():
    speak("Jarvis online")

    while True:
        command = listen()

        if "jarvis" in command:
            speak("Yes?")
            time.sleep(0.5)

            command = listen()
            handle_command(command)

if __name__ == "__main__":
    main()
