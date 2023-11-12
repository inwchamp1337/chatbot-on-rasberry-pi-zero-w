## Open AI based Voice Chatbot in Raspberry Pi zero W
 Project for the Second Year, First Semester Physiot Students at KMITL.
## Installation
Can be used with any Raspberry Pi connected to speakers and a microphone.
To install the required libraries, run the following commands in your terminal:

```bash
sudo apt-get install portaudio19-dev
sudo apt-get install python3-pyaudio
pip install speechrecognition
pip install pyttsx3
pip install openai
sudo apt-get install espeak
sudo apt-get install Flac
``````

# To Run

```bash
python aiforpiepie.py 2>/dev/null  #2>/dev/null for ignor alsa 
``````
It would be better if you use the more expensive Raspberry Pi
