import customtkinter as ctk
import tkinter as tk
import threading
import math
import time
import speech_recognition as sr
import pyttsx3

# ---------------- JARVIS BACKEND ----------------

engine = pyttsx3.init()

def speak(text):
    status_label.configure(text=f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

def listen():
    global listening

    listening = True

    try:
        with sr.Microphone() as source:
            status_label.configure(text="Listening...")
            audio = recognizer.listen(source, phrase_time_limit=5)

        command = recognizer.recognize_google(audio).lower()

        status_label.configure(text=f"You: {command}")

        handle_command(command)

    except:
        status_label.configure(text="Didn't catch that.")

    listening = False

def handle_command(command):
    if "hello" in command:
        speak("Hello master.")

    elif "how are you" in command:
        speak("Running perfectly.")

    else:
        speak(f"You said {command}")

# ---------------- UI ----------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("500x700")
app.title("JARVIS")

canvas = tk.Canvas(
    app,
    width=500,
    height=700,
    bg="#0d0d0d",
    highlightthickness=0
)
canvas.pack(fill="both", expand=True)

listening = False
pulse = 0

# ---------------- ORB ----------------

def draw_orb():
    global pulse

    canvas.delete("all")

    pulse += 0.08

    base_radius = 80

    if listening:
        radius = base_radius + math.sin(pulse * 4) * 20
        glow = 40
    else:
        radius = base_radius + math.sin(pulse) * 5
        glow = 20

    x = 250
    y = 300

    # Glow
    for i in range(glow, 0, -5):
        alpha = hex(max(10, 255 - i * 6))[2:]

        color = f"#00aaff"

        canvas.create_oval(
            x-radius-i,
            y-radius-i,
            x+radius+i,
            y+radius+i,
            fill=color,
            outline=""
        )

    # Main orb
    canvas.create_oval(
        x-radius,
        y-radius,
        x+radius,
        y+radius,
        fill="#00aaff",
        outline=""
    )

    app.after(30, draw_orb)

# ---------------- CLICK ORB ----------------

def orb_click(event):
    open_text_input()

canvas.bind("<Button-1>", orb_click)

# ---------------- TEXT INPUT ----------------

def open_text_input():

    popup = ctk.CTkToplevel(app)
    popup.geometry("400x150")
    popup.title("Type Command")

    entry = ctk.CTkEntry(
        popup,
        width=300,
        height=40,
        font=("Arial", 18)
    )
    entry.pack(pady=20)

    def submit():
        cmd = entry.get().lower()

        status_label.configure(text=f"You: {cmd}")

        handle_command(cmd)

        popup.destroy()

    button = ctk.CTkButton(
        popup,
        text="Send",
        command=submit
    )
    button.pack(pady=10)

# ---------------- STATUS ----------------

status_label = ctk.CTkLabel(
    app,
    text="JARVIS ONLINE",
    font=("Arial", 20)
)

status_label.place(relx=0.5, rely=0.8, anchor="center")

# ---------------- MIC BUTTON ----------------

mic_button = ctk.CTkButton(
    app,
    text="🎤",
    width=60,
    height=60,
    corner_radius=30,
    font=("Arial", 24),
    command=lambda: threading.Thread(target=listen).start()
)

mic_button.place(relx=0.5, rely=0.9, anchor="center")

# ---------------- START ----------------

draw_orb()

speak("Jarvis online.")

app.mainloop()
