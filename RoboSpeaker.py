import os
import win32com.client as wincom


if __name__ == '__main__':
    pass

while True:
    msg=input("Please enter your message:")
    speak=wincom.Dispatch("SAPI.SpVoice")
    speak.Speak(msg)
    if msg=='quit':
        speak.Speak("Good Bye Mate!!!")