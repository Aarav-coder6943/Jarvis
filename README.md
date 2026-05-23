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

FOR BEST USE CASES AND BEST IMPLEMENTATION, DOWNLOAD jarvis_JARVIS.zip and extract it, then make a virtual environment in that folder

cd jarvis_JARVIS 
cd jarvis
python -m venv jarvis_env
jarvis_env/Scripts/activate

OR create a startup batch file

cd your_project_path
call jarvis_env\Scripts\activate
python jarvis_backend.py (OR python setup_and_run.py)

AND set this as startup application
This will now launch jarvis as soon as you power om your device



🎙️ COMPLETE LIST OF USER COMMANDS

This version of J.A.R.V.I.S. has a LOT of commands now.
I grouped them by category so your brain doesn’t combust 💀

🧠 SYSTEM / HUD COMMANDS

These show system diagnostics.

Commands:
“hud”
“dashboard”
“status”
“diagnostic”
“how are you”
“system check”
“run a check”
What happens:

Shows:

CPU
RAM
Disk
Battery
Time
Hostname
⚙️ PROCESS MONITOR COMMANDS
Commands:
“top processes”
“process list”
“what’s running”
“running processes”
“process monitor”
What happens:

Displays top CPU-consuming apps.

🔋 BATTERY COMMANDS
Commands:
“battery”
“battery status”
“how much battery”
What happens:

Speaks:

battery %
charging state
🕒 TIME COMMANDS
Commands:
“what time is it”
“tell me the time”
“current time”
📅 DATE COMMANDS
Commands:
“what day is it”
“what’s today’s date”
“the date”
🌦️ WEATHER COMMANDS
Commands:
“weather”
“weather Delhi”
“weather in Mumbai”
“weather for London”
What happens:

Uses:

wttr.in

No API key needed.

📝 NOTES COMMANDS
Add Note
Commands:
note add physics / revise chapter 5

or

note: physics / revise vectors
List Notes
Commands:
“note list”
“notes”
“show notes”
“my notes”
Read Note
Commands:
note read physics
Delete Note
Commands:
note delete physics

or

note remove physics
⏰ REMINDER COMMANDS
Reminder by Minutes
Commands:
remind me in 10 minutes drink water
remind me in 2 hours do homework
Reminder by Clock Time
Commands:
remind me at 15:30 meeting
List Reminders
Commands:
“list reminders”
“show reminders”
“pending reminders”
“my reminders”
📋 CLIPBOARD COMMANDS
Copy Text
Commands:
copy hello world
Clipboard History
Commands:
“clipboard history”
“show clipboard”
“paste history”
🧩 ALIAS COMMANDS
Create Alias
Commands:
alias yt = go to youtube

Then:

yt

automatically runs:

go to youtube
List Aliases
Commands:
“alias list”
“list aliases”
“show aliases”
💻 APP COMMANDS
Open Apps
Commands:
“open chrome”
“launch vscode”
“start spotify”
“run discord”

Supported launch verbs:

open
launch
start
run
Close Apps
Commands:
“close chrome”
“kill discord”
“terminate spotify”
“quit steam”

Supported close verbs:

close
kill
terminate
quit
🌐 WEBSITE COMMANDS
Open Website
Commands:
“go to youtube”
“browse github”
“open website reddit”
Search Google
Commands:
search for quantum physics
💾 SESSION COMMANDS
Save Session
Commands:
save session coding
Load Session
Commands:
load session coding

or

restore session coding
List Sessions
Commands:
“list sessions”
“show sessions”
“what sessions”
Restore Last Session
Commands:
“wake up”
“restore last”
🧮 MATH COMMANDS
Percentage Math
Commands:
15 percent of 340
General Calculations
Commands:
calculate 24 * 7
what is 55 plus 44
compute 45 divided by 9

Supports:

plus
minus
times
multiplied by
divided by
squared
cubed
🔊 VOLUME COMMANDS
Volume Up
Commands:
“volume up”
“turn up”
“louder”
Volume Down
Commands:
“volume down”
“turn down”
“quieter”
Mute
Commands:
“mute”
“mute audio”
“silence”
“mute the volume”
📸 SCREENSHOT COMMANDS
Commands:
“screenshot”
“capture screen”
What happens:

Saves screenshot to desktop.

⚡ POWER COMMANDS
Shutdown Computer
Commands:
“shutdown computer”
“shut down the computer”
Restart Computer
Commands:
“restart computer”
“restart the computer”
Sleep Computer
Commands:
“sleep computer”
“sleep system”
“sleep pc”
“sleep laptop”
🎭 FUN COMMANDS
Tony Stark Quotes
Commands:
“quote”
“tony stark”
Jokes
Commands:
“joke”
“tell me a joke”
Coin Flip
Commands:
“flip a coin”
“coin flip”
Dice Roll
Commands:
“roll a die”
“roll a 20 sided die”
“roll dice”
👋 GREETING COMMANDS
Commands:
“hello”
“hi there”
“hey jarvis”
🙏 THANK YOU COMMANDS
Commands:
“thank you”
“thanks”
🔄 MODE SWITCH COMMANDS
Switch to Voice Mode
Commands:
“voice mode”
“switch to voice”
Switch to Text Mode
Commands:
“text mode”
“type mode”
“switch to text”
🔇 TTS CONTROL COMMANDS
Mute Jarvis Voice
Commands:
“mute jarvis”
“stop talking”
“be quiet”
Unmute Jarvis
Commands:
“unmute jarvis”
“start talking”
“speak again”
🚪 EXIT COMMANDS
Commands:
“good night”
“go offline”
“shutdown jarvis”
“power down”
“goodbye jarvis”
“exit”
“quit”
🤖 AI FALLBACK COMMANDS

This is the coolest part.

ANYTHING unknown automatically gets sent to Ollama AI.

Example:

Jarvis explain quantum entanglement
Jarvis write a python sorting algorithm
Jarvis how do black holes evaporate

If command matching fails:

ask_ai(raw)

runs automatically.

So technically…
the assistant can respond to almost ANY question now.

🎤 VOICE ACTIVATION COMMANDS

Wake words:

“Jarvis”
“J.A.R.V.I.S.”
“Hey Jarvis”
🔥 MOST POWERFUL COMMAND CHAINS

You can also chain behavior mentally like:

Jarvis open vscode
Jarvis open chrome
Jarvis save session coding

Then tomorrow:

Jarvis restore session coding

and BOOM:
entire workspace restored.
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
