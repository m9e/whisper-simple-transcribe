import json
import os
import requests
import openai
from datetime import datetime

openai.api_key = os.environ["OPENAI_API_KEY"] # Set your API key as an environment variable

class AudioProcessor:

    def __init__(self, file=None, audio_data=None):
        self.audio_data = audio_data
        self.created_at = datetime.now()
        self.prompt = None
        self.result = None
        self.submitted_at = None
        self.processed_at = None
        self.language = "en-US"
        if file is not None:
          self.file = open(file, 'rb')

    def process_audio(self, file=None):
        if file is not None:
          self.file = open(file, 'rb')

        if not self.file:
          raise Exception('no file')

        # Make the initial API call to submit the audio file
        self.submitted_at = datetime.now()
        try:
          self.result = openai.Audio.transcribe("whisper-1", self.file)
          self.processed_at = datetime.now()
        except Exception as e:
          self.result = None
          self.error = str(e)
            
