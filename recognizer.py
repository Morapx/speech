import speech_recognition as sr

r = sr.Recognizer()

audio_file = sr.AudioFile('good-morningMan.wav')

with audio_file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    result = r.recognize_google(audio, language='es-MX')

    with open('result.txt' , mode="w") as file:
        file.write("Texto detectado:")
        file.write("\n")
        file.write(result)
        print("Listón")