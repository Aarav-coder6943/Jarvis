import speech_recognition as sr
import pyttsx3
import subprocess
import json
import psutil
import os
import time
import requests
import datetime

# ---------- TTS ----------
engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# ---------- AI (OLLAMA) ----------
def ask_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]
    except:
        return "I'm having trouble connecting to my brain."

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

# ---------- Greeting ----------
def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning. Systems online.")
    elif hour < 18:
        speak("Good afternoon.")
    else:
        speak("Good evening.")

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
        running_processes.append({"name": app_name, "pid": proc.pid})
    except:
        speak("App not found")

# ---------- Close Apps ----------
def close_apps():
    for proc in running_processes:
        try:
            psutil.Process(proc["pid"]).terminate()
        except:
            pass
    running_processes.clear()
    speak("All apps closed")

# ---------- Save ----------
def save_session(file):
    with open(file, "w") as f:
        json.dump(running_processes, f)

# ---------- Load ----------
def load_session(file):
    if not os.path.exists(file):
        speak("Session not found")
        return

    with open(file, "r") as f:
        data = json.load(f)

    for app in data:
        try:
            subprocess.Popen(f'start "" "{app["name"]}"', shell=True)
        except:
            pass

    speak("Session restored")

# ---------- COMMAND HANDLER ----------
def handle_command(command):

    if "open" in command:
        app = command.replace("open", "").strip()
        open_app(app)

    elif "save in" in command:
        name = command.replace("save in", "").strip()
        file = os.path.join(SESSION_DIR, f"{name}.json")
        save_session(file)
        close_apps()
        speak(f"Saved in {name} mode")

    elif "it's" in command and "time" in command:
        name = command.replace("it's", "").replace("time", "").strip()
        file = os.path.join(SESSION_DIR, f"{name}.json")
        load_session(file)

    elif "wake up daddy's home" in command:
        load_session(LAST_SESSION)

    elif "good night" in command:
        if os.path.exists(LAST_SESSION):
            os.remove(LAST_SESSION)
        save_session(LAST_SESSION)
        close_apps()
        speak("Good night.")

    else:
        # 🧠 fallback to AI
        response = ask_ollama(command)
        speak(response)

# ---------- MAIN ----------
def main():
    greet()

    while True:
        command = listen()

        if "jarvis" in command:
            speak("Yes?")
            time.sleep(0.5)

            command = listen()
            handle_command(command)

if __name__ == "__main__":
    main()
