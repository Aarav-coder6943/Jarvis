import speech_recognition as sr
import pyttsx3
import subprocess
import json
import os
import time
import random

# ---------- TTS SETUP ----------
engine = pyttsx3.init()

# 🔊 CHANGE VOICE HERE (0 = male, 1 = female usually)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  

engine.setProperty('rate', 185)  # speed
engine.setProperty('volume', 1)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------- SPEECH ----------
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.pause_threshold = 0.6

def listen():
    with sr.Microphone() as source:
        audio = recognizer.listen(source, phrase_time_limit=4)

    try:
        return recognizer.recognize_google(audio).lower()
    except:
        return ""

# ---------- PERSONALITY ----------
WAKE_RESPONSES = [
    "Yes, master.",
    "At your service.",
    "I'm listening.",
    "What do you need?",
    "Ready for your command.",
    "Your wish is my command.",
    "Online and ready.",
    "Go ahead."
]

SLEEP_RESPONSES = [
    "Good night. Shutting down your empire.",
    "Rest well. I'll guard the system.",
    "Logging off. Sweet dreams.",
    "Powering down. See you soon.",
    "Mission paused. Good night."
]

WAKEUP_RESPONSES = [
    "Welcome back. Everything is ready.",
    "Systems restored. Let's get to work.",
    "Good to see you again.",
    "All systems online.",
    "We're back in business."
]

# ---------- ALIASES ----------
ALIASES = {
    "vs code": "code",
    "visual studio code": "code",
    "android studio": "android studio",
    "chrome": "chrome",
    "google chrome": "chrome",
    "edge": "msedge",
    "firefox": "firefox",
    "brave": "brave",
    "word": "winword",
    "excel": "excel",
    "powerpoint": "powerpnt",
    "notepad": "notepad",
    "calculator": "calc",
    "spotify": "spotify",
    "discord": "discord",
    "telegram": "telegram",
    "cmd": "cmd",
    "powershell": "powershell",
    "file explorer": "explorer"
}

# ---------- SESSION ----------
SESSION_FILE = "session.json"
running_apps = []

# ---------- CLEAN COMMAND ----------
def clean_command(command):
    fillers = ["please", "jarvis", "can you", "could you", "the"]
    for word in fillers:
        command = command.replace(word, "")
    return command.strip()

# ---------- OPEN APP ----------
def open_app(app_name):
    try:
        subprocess.Popen(f'start "" "{app_name}"', shell=True)
        speak(f"Opening {app_name}")
        running_apps.append({"name": app_name})
    except:
        speak("Couldn't open " + app_name)

# ---------- SAVE ----------
def save_session():
    with open(SESSION_FILE, "w") as f:
        json.dump(running_apps, f)

# ---------- RESTORE ----------
def restore_session():
    if not os.path.exists(SESSION_FILE):
        speak("No previous session found")
        return

    with open(SESSION_FILE, "r") as f:
        data = json.load(f)

    for app in data:
        try:
            subprocess.Popen(f'start "" "{app["name"]}"', shell=True)
        except:
            pass

# ---------- COMMAND HANDLER ----------
def handle_command(command):
    command = command.lower()

    if "open" in command:
        cleaned = clean_command(command.replace("open", ""))

        for key in ALIASES:
            if key in cleaned:
                open_app(ALIASES[key])
                return

        open_app(cleaned)

    elif "wake up daddy's home" in command:
        restore_session()
        speak(random.choice(WAKEUP_RESPONSES))

    elif "good night" in command:
        save_session()
        speak(random.choice(SLEEP_RESPONSES))

    else:
        speak("I didn't understand")

# ---------- MAIN LOOP ----------
def main():
    speak("Jarvis online")

    while True:
        command = listen()

        if "jarvis" in command:
            speak(random.choice(WAKE_RESPONSES))
            time.sleep(0.3)

            command = listen()
            handle_command(command)

if __name__ == "__main__":
    main()
