# Voice-Controlled Weather Assistant

This Python application allows users to interact with a voice-controlled assistant that can recognize commands, process natural language, and provide weather updates for different cities. The application leverages various technologies, including speech recognition, natural language processing (NLP), and text-to-speech synthesis.

## Features

- **Voice Recognition**: The application listens to voice commands in Turkish and converts them to text.
- **Natural Language Processing**: It processes the recognized text using spaCy to understand the user's commands.
- **Weather Information**: Retrieves real-time weather information for a specified city using an external API.
- **Text-to-Speech**: Provides audible responses to user queries.

## Requirements

Before running the application, ensure you have the following dependencies installed:

- Python 3.x
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [gTTS](https://pypi.org/project/gTTS/)
- [spaCy](https://spacy.io/)
- [mpg321](https://pypi.org/project/mpg321/) (for playing audio on Linux/MacOS)
