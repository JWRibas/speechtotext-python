import speech_recognition as sr

recognizer = sr.Recognizer()

mic = sr.Microphone()

# Inicia o reconhecimento de fala
with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)

    print(text)

except sr.UnknownValueError:
    print("Fala não reconhecida")

except sr.RequestError as e:
    print("Erro de requisição: {}".format(e))
