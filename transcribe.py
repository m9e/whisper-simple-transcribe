import sys
import os
import pyperclip
from Processors import AudioProcessor

def main(filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    # Initialize the AudioProcessor with the given filename
    audio_processor = AudioProcessor(file=filename)

    # Process the audio file and get the transcript
    try:
        audio_processor.process_audio()
        transcript = audio_processor.result.get("text")

        # Print the transcript to stdout
        print(transcript)

        # Copy the transcript to the clipboard
        pyperclip.copy(transcript)
        print("Transcript copied to clipboard.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <audio_filename>")
        sys.exit(1)

    main(sys.argv[1])

