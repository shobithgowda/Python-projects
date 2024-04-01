import os
import sys
import time
import webbrowser
from gtts import gTTS  # Import the gTTS module for Google Text-to-Speech API integration

def say(text, language='en', voice=None, rate=1.0, pitch=1.0, bg_music=None):
    # Build SSML (Speech Synthesis Markup Language)
    ssml = f'<speak>{text}</speak>'
    
    # Add background music
    if bg_music:
        webbrowser.open(bg_music)  # Open the background music URL in the default web browser
    
    try:
        if os.name == 'posix':  # macOS and Linux
            if voice:
                os.system(f'say -v {voice} -r {rate} -p {pitch} {ssml}')  # Use the 'say' command with voice, rate, pitch, and SSML
            else:
                os.system(f'say -r {rate} -p {pitch} {ssml}')  # Use the 'say' command with rate, pitch, and SSML
        elif os.name == 'nt':   # Windows
            tts = gTTS(text=text, lang=language, slow=False)  # Create a gTTS object for text-to-speech conversion
            tts.save('temp.mp3')  # Save the synthesized speech as a temporary MP3 file
            os.system('start temp.mp3')  # Open the MP3 file using the default media player
        else:
            print("Text-to-speech is not supported on this operating system.")
    except Exception as e:
        print(f"Error: {e}")  # Print any errors that occur during text-to-speech conversion

# Function to select the language for text-to-speech
def select_language():
    languages = {'en': 'English', 'kn': 'Kannada', 'hi': 'Hindi', 'te': 'Telugu', 'ta': 'Tamil'}  # Updated languages with language codes
    print("Select language:")
    for code, name in languages.items():
        print(f"{code}: {name}")
    lang = input("Enter language code: ")
    if lang in languages:
        return lang
    else:
        print("Invalid language code.")
        return None

# Function to select the voice for text-to-speech
def select_voice(language):
    voices = {'en': ['m1', 'm2'], 'kn': ['k1', 'k2'], 'hi': ['h1', 'h2'], 'te': ['t1', 't2'], 'ta': ['tt1', 'tt2']}  # Example voices for each language
    print(f"Select voice for {language}:")
    for voice in voices.get(language, []):
        print(voice)
    voice = input("Enter voice name: ")
    if voice in voices.get(language, []):
        return voice
    else:
        print("Invalid voice name.")
        return None

# Function to select the speech rate
def select_rate():
    rate = input("Enter speech rate (default is 1.0): ")
    try:
        return float(rate)
    except ValueError:
        print("Invalid speech rate. Using default rate.")
        return 1.0

# Function to select the speech pitch
def select_pitch():
    pitch = input("Enter speech pitch (default is 1.0): ")
    try:
        return float(pitch)
    except ValueError:
        print("Invalid speech pitch. Using default pitch.")
        return 1.0

# Function to select background music
def select_background_music():
    bg_music = input("Enter background music URL (optional): ")
    return bg_music

# Main function to run the text-to-speech program
def main():
    print("Welcome to the Text-to-Speech program")
    while True:
        text = input("Enter text to speak (or 'q' to quit): ")
        if text.lower() == 'q':
            say("Bye bye!")  # Say "Bye bye!" when quitting
            break
        
        language = select_language()
        if not language:
            continue
        
        voice = select_voice(language)
        rate = select_rate()
        pitch = select_pitch()
        bg_music = select_background_music()
        
        say(text, language, voice, rate, pitch, bg_music)
        time.sleep(1)  # Wait for speech synthesis to complete

if __name__ == '__main__':
    main()
