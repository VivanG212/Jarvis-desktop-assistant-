# 🎙️ Jarvis: Local Voice Assistant 

Jarvis is a low-latency, voice-activated personal assistant built in Python. Powered by Google's Gemini API, Jarvis runs natively in the background on macOS—listening to real-time voice commands, maintaining conversation memory, and executing native system controls like volume and brightness adjustments.

Built to mimic a lightweight, localized AI companion, it completely bypasses heavy web interfaces for an immediate, responsive, and invisible desktop experience.

##  Features

*  Real-Time Voice Processing:** Listen naturally; Jarvis processes microphone inputs seamlessly.
*  Persistent Context Memory:** Remembers user data (like your name or preferences) across interactions using localized JSON state tracking.
*  macOS System Automation:** Control system volume, brightness, or execute custom scripts entirely via voice.
*  Gemini Engine Integration:** Leverages the latest Google GenAI SDK for highly intelligent, context-aware dialogue.
*  Silent Background Service:** Configured via macOS `launchd` to boot silently in the background on startup without needing open Terminal windows.

##  Getting Started

### Prerequisites
* A Mac running macOS
* Python 3.10 or higher
* A Gemini API Key (Get one from [Google AI Studio](https://ai.google.dev/))

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/vivangorisaria/JarvisProject.git](https://github.com/vivangorisaria/JarvisProject.git)
   cd JarvisProject

   2. **Setup the virtual environment**
   python3 -m venv venv
   source venv/bin/activate

   4. **Install the required packages**
      pip install -r requirements.txt

   5. **Configure your API Key & Background Boot:**
   Create a launch agent configuration file under ~/Library/LaunchAgents/com.vivan.jarvis.plist pointing to your environment variables and paths:
   launchctl load ~/Library/LaunchAgents/com.vivan.jarvis.plist


   ##  Project Architecture

* `main.py` — Coordinates the primary microphone listening loop and AI routing logic.
* `config.py` — Manages state persistence and user memory serialization (`jarvis_memory.json`).
* `system_actions.py` — Translates text-based intents into native AppleScript commands for system control.
* `audio.py` — Manages speech-to-text input processing and text-to-speech outputs.


   ##  License
This project is open-source and available under the MIT License. Feel free to fork, modify, and build your own custom system integrations!
