import sys
from google import genai
from google.genai import types
import config
from audio import speak, listen_until_done
from system_actions import run_local_macro

# Core AI Engine Initialization
client = genai.Client()
jarvis_brain = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=(
            f"You are Jarvis, an elite AI desktop companion. Address the user as {config.user_data['user_name']}. "
            "Keep responses brief and conversational. You have live web access for real-time data."
        ),
        tools=[types.Tool(google_search=types.GoogleSearch())]
    )
)

speak(f"Systems initialized. Welcome back, {config.user_data['user_name']}.")

while True:
    wake_input = listen_until_done(timeout_seconds=5)
    
    if "jarvis" in wake_input.lower():
        speak("Online. Go ahead.")
        user_command = listen_until_done(timeout_seconds=10)
        
        if not user_command or user_command.strip() == "":
            continue
            
        print(f"Processing command: {user_command}")
        cmd_clean = user_command.lower().strip()
        
        # 1. Update Persistent Local Memory
        if "call me" in cmd_clean:
            new_name = cmd_clean.split("call me")[-1].strip().title()
            config.user_data["user_name"] = new_name
            config.save_memory(config.user_data)
            speak(f"Understood. I will call you {new_name} from now on.")
            continue

        # 2. Hard Stop Script Execution
        elif "goodbye" in cmd_clean or "exit" in cmd_clean:
            speak("Goodbye. Disengaging systems.")
            sys.exit()
            
        # 3. Process Local Hardware Macro Routing Wall
        elif run_local_macro(cmd_clean, config.user_data):
            continue
            
        # 4. Fallback Cloud Processing (Complex Queries)
        else:
            question_words = ["what", "how", "why", "where", "who", "when", "check", "find", "tell", "ask"]
            if any(word in cmd_clean for word in question_words):
                try:
                    response = jarvis_brain.send_message(user_command)
                    speak(response.text)
                except Exception as e:
                    print(f"Cloud Pipeline Limit Notice: {e}")
                    speak("Local systems are active, but my cloud request limit has been reached for the day.")
            else:
                continue
