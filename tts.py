import subprocess
import tempfile
import os

# Replace with your Persian text
persian_text = "سلام! این یک آزمایش است."

# Path to the Piper model for Persian (replace with the correct model path)
model_path = "./piper-farsi"

def synthesize_and_play(text, model_path):
    # Create a temporary file to store the audio output
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio_file:
        temp_audio_path = temp_audio_file.name
    
    # Command to generate audio from text using Piper
    command = [
        "piper",
        "--model", model_path,
        "--output", temp_audio_path,
        "--text", text
    ]
    
    # Run Piper command
    try:
        subprocess.run(command, check=True)
        print("Audio generated successfully.")
        
        # Play the audio (Linux example using 'aplay')
        subprocess.run(["aplay", temp_audio_path])
    except subprocess.CalledProcessError as e:
        print("Error generating audio:", e)
    finally:
        # Clean up the temporary audio file
        os.remove(temp_audio_path)

# Synthesize and play the Persian text
synthesize_and_play(persian_text, model_path)
