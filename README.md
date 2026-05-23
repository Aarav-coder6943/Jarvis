🤖 J.A.R.V.I.S. — Personal AI Desktop Assistant

A fully voice-controlled AI desktop assistant inspired by Iron Man’s J.A.R.V.I.S.

This project combines:

🎙️ Voice recognition
🧠 Local AI (Ollama)
💻 Desktop automation
⚡ System monitoring
📝 Notes & reminders
🌐 Web browsing
📋 Clipboard management
💾 Session restoration
🔊 Text-to-speech interaction

All running locally on your machine.

✨ Features
🎤 Voice Assistant
Wake word activation (Jarvis)
Voice command execution
Text mode + Voice mode
Natural speech responses
🤖 Local AI Integration

Powered by:

Ollama
Llama 3.1

Ask:

coding questions
explanations
random knowledge
productivity help

Fully local AI support.

💻 Desktop Automation

Launch and control applications using voice.

Examples:

Open Chrome
Launch VSCode
Close Spotify
Kill Discord
🌐 Web Control

Open websites or search the web instantly.

Examples:

Go to YouTube
Browse GitHub
Search for quantum physics
💾 Workspace Sessions

Save and restore entire work setups.

Example:

save session coding
load session coding

Automatically restores:

VSCode
Chrome
Spotify
other apps
📝 Notes System

Create and manage notes directly through commands.

Examples:

note add physics / revise chapter 5
note read physics
note delete physics
⏰ Reminders

Background reminder engine with voice alerts.

Examples:

remind me in 10 minutes drink water
remind me at 18:30 meeting
📊 Live System Monitoring

Built-in diagnostics dashboard:

CPU usage
RAM usage
Disk usage
Battery status
Host information
📋 Clipboard History

Clipboard memory and quick recall system.

🎨 Rich Terminal UI

Powered using:

Rich
Prompt Toolkit

Features:

live dashboard
colored terminal panels
command history
autocomplete
🧠 Tech Stack
Core
Python 3
Libraries
speech_recognition
pyttsx3
psutil
rich
prompt_toolkit
requests
pyperclip
AI
Ollama
Llama 3.1
📦 Installation
1. Clone Repository
git clone https://github.com/Aarav-coder/Jarvis.git
cd jarvis-ai
2. Install Dependencies
pip install -r requirements.txt
3. Install Ollama

Download:

Ollama

Then install the model:

ollama pull llama3.1

Start Ollama:

ollama serve
🚀 Run J.A.R.V.I.S.
python jarvis.py
🎙️ Example Commands
Applications
open chrome
launch vscode
close spotify
Websites
go to youtube
browse github
search for machine learning
Sessions
save session coding
load session coding
Notes
note add math / revise trigonometry
note list
Reminders
remind me in 15 minutes drink water
AI
explain black holes
write a python sorting algorithm
📁 Project Structure
JARVIS/
│
├── jarvis.py
├── requirements.txt
├── sessions/
├── notes.json
├── reminders.json
├── aliases.json
├── clipboard.json
└── README.md
⚡ Future Improvements

Planned upgrades:

Whisper speech recognition
Vision AI
Screen understanding
Browser automation
Plugin system
Memory graph
Smart home integration
Mobile companion app
Wake word engine
Face recognition
Real-time AI context memory
⚠️ Notes
Best experience on Windows
Requires microphone access
Ollama must be running for AI responses
Some commands are OS-dependent
🛠️ Recommended Setup
Hardware
Good microphone
Dual monitor setup (optional)
NVIDIA GPU recommended for local AI
Software
VSCode
Ollama
Python 3.11+
Windows Terminal


Feel free to modify, improve, and build your own assistant.

👨‍💻 Author

Built by Aarav.

Inspired by:

Iron Man
J.A.R.V.I.S.
futuristic AI systems
local-first AI tooling
⭐ Final Note

This project started as a simple assistant idea and evolved into a fully interactive desktop AI environment.

The goal was never just “another chatbot.”

The goal was to build something that genuinely feels alive.
