import os
import time
import subprocess

def get_mac_status():
    current_time = time.strftime("%I:%M %p")
    try:
        battery_cmd = subprocess.check_output(["pmset", "-g", "batt"]).decode("utf-8")
        percentage = battery_cmd.split("%")[0].split()[-1]
        battery_status = f"Your battery is at {percentage} percent."
    except Exception:
        battery_status = "Battery status unavailable."
    return f"The current time is {current_time}. {battery_status}"

def run_local_macro(cmd_clean, user_data):
    if "status" in cmd_clean or "battery" in cmd_clean or "time" in cmd_clean:
        from audio import speak
        speak(get_mac_status())
        return True
        
    elif "volume" in cmd_clean:
        from audio import speak
        words = cmd_clean.split()
        vol_level = "50"
        for word in words:
            if word.isdigit():
                vol_level = word
                break
        if "mute" in cmd_clean:
            speak("Muting system audio.")
            os.system("osascript -e 'set volume output muted true'")
        elif "unmute" in cmd_clean:
            speak("Unmuting system audio.")
            os.system("osascript -e 'set volume output muted false'")
        else:
            speak(f"Setting volume to {vol_level} percent.")
            os.system(f"osascript -e 'set volume output volume {vol_level}'")
        return True
        
    elif "play music" in cmd_clean or "youtube music" in cmd_clean:
        from audio import speak
        speak("Opening YouTube Music now.")
        time.sleep(1.5)
        os.system("open 'https://music.youtube.com'")
        return True

    elif "play a video" in cmd_clean or "play video" in cmd_clean:
        from audio import speak
        search_query = cmd_clean.replace("play a video", "").replace("play video", "").replace("about", "").strip()
        if search_query:
            speak(f"Searching YouTube for videos about {search_query}.")
            time.sleep(2.0)
            os.system(f"open 'https://www.youtube.com/results?search_query={search_query}'")
        else:
            speak("Opening YouTube.")
            time.sleep(1.0)
            os.system("open 'https://www.youtube.com'")
        return True
        
    elif "open" in cmd_clean:
        from audio import speak
        target_site = cmd_clean.replace("open", "").replace("a tab for", "").replace("browser", "").replace("safari", "").strip()
        if target_site in ["", "safari", "tab"]:
            speak("Opening Safari browser.")
            time.sleep(1.0)
            os.system("open -a Safari")
        else:
            speak(f"Opening {target_site} in your browser.")
            time.sleep(1.5)
            os.system(f"open 'https://www.{target_site}.com'")
        return True
        
    elif "search for" in cmd_clean and "on google" in cmd_clean:
        from audio import speak
        search_query = cmd_clean.replace("search for", "").replace("on google", "").strip()
        speak(f"Searching Safari for {search_query}.")
        time.sleep(1.5)
        os.system(f"open 'https://www.google.com/search?q={search_query}'")
        return True
        
    return False
