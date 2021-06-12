import speech_recognition
import openai
import pyttsx3


# GPT-3 Parameters
openai.organization = "ORG-KEY-HERE"
openai.api_key = 'API-KEY-HERE'

## Speech Recognition Algorithm
recognizer = speech_recognition.Recognizer()
print("Please speak into the microphone:")

## Function which inputs speechtotext into openAI's API
while True:

    try:

        with speech_recognition.Microphone() as mic:

            #Ready the Microphone
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            #Translate speech to text
            SpeechText = recognizer.recognize_google(audio)
            SpeechText = SpeechText.lower()

            ## GPT-3 API
            myPrompt = """
            The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

            Human: Hello, who are you?
            AI: I am an AI created by OpenAI. How can I help you today?
            Human:{SpeechText}
            AI:"""

            # GPT-3 Engine parameters
            start_sequence = "\nAI:"
            restart_sequence = "\nHuman: "
            Addon = "\n"


            response = openai.Completion.create(
                engine="davinci",
                temperature=0.9,
                max_tokens=190,
                top_p=1,
                prompt = str(myPrompt.replace("{SpeechText}", SpeechText)),
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=["\n", "Human:", "AI:"]
            )
            # Print out results for further processing
            prompt = myPrompt.replace("{SpeechText}", SpeechText),
            print(f"Human:{SpeechText}\nAI:{response.choices[0].text}")

            # SPEAK IT OUT
            engine = pyttsx3.init()
            engine.say(response.choices[0].text)
            engine.runAndWait()
            exit()

    except speech_recognition.UnknownValueError:
       print("I didn't quite get you. Can you please repeat that?")
       recognizer = speech_recognition.Recognizer()
    continue
