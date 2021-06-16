import camelcase
import pyttsx3
import emoji
def camel_on():
    Data = input("Enter the data: ")
    x = camelcase.CamelCase()
    x.hump(Data)
    if Data == x.hump(Data):
        print(emoji.emojize(":thumbs_up:"))
    else:
        x = camelcase.CamelCase()
        print(x.hump(Data))
        spk=pyttsx3.init()
        spk.say("Succecss")
        spk.runAndWait()