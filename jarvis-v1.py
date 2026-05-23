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

# ---------- App Mapping ----------
apps = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "vscode": "C:\\Users\\YOUR_USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
}

SESSION_FILE = "session.json"
running_processes = []

# ---------- Open App ----------
def open_app(app_name):
    if app_name in apps:
        path = apps[app_name]
        try:
            proc = subprocess.Popen(path)
            running_processes.append({
                "name": app_name,
                "path": path,
                "pid": proc.pid
            })
            speak(f"Opening {app_name}")
        except:
            speak("Failed to open " + app_name)
    else:
        speak("App not found")

# ---------- Save Session ----------
def save_session():
    with open(SESSION_FILE, "w") as f:
        json.dump(running_processes, f)
    speak("Session saved")

# ---------- Restore Session ----------
def restore_session():
    if not os.path.exists(SESSION_FILE):
        speak("No previous session found")
        return

    with open(SESSION_FILE, "r") as f:
        data = json.load(f)

    for app in data:
        try:
            subprocess.Popen(app["path"])
        except:
            pass

    speak("Welcome back. Everything is ready.")

# ---------- Close Apps ----------
def close_apps():
    for proc in running_processes:
        try:
            p = psutil.Process(proc["pid"])
            p.terminate()
        except:
            pass

    running_processes.clear()
    speak("Good night. Shutting everything down.")

# ---------- Command Handler ----------
def handle_command(command):
    if "open" in command:
        for app in apps:
            if app in command:
                open_app(app)
                return

    elif "wake up daddy's home" in command:
        restore_session()

    elif "good night" in command:
        save_session()
        close_apps()

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
