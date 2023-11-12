from openai import OpenAI
import speech_recognition as sr
import pyttsx3

# Initialize OpenAI client
client = OpenAI(api_key="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")

listening = True
engine = pyttsx3.init()

# Set your OpenAI API key and customize the chatgpt role
messages = [{"role": "system", "content": "Your name is PhylotAI *important* and give answers in 2 lines "}]

# Customizing the output voice
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')


def get_response(user_input):
        messages.append({"role": "user", "content": user_input})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        ChatGPT_reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": ChatGPT_reply})
        return ChatGPT_reply
   


while listening:
    with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(source)
        recognizer.dynamic_energy_threshold = 3000

        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=10)
            response = recognizer.recognize_google(audio)
            print(response)

            if (response.lower()):

                response_from_openai = get_response(response)
                print(response_from_openai)
                engine.setProperty('rate', 130)
                engine.setProperty('volume', volume)
                engine.setProperty('voice', 'greek')  # Adjust the voice accordingly
                engine.say(response_from_openai)
                engine.runAndWait()

            else:
                print("Didn't recognize 'jarvis'.")

        except sr.UnknownValueError:
            print("Didn't recognize anything.")
