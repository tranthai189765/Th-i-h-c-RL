import speech_recognition
import pyttsx3
from datetime import date


today = date.today()

d3 = f"Today is {today.strftime("%B %d, %Y")}, boss!"#print("Today is: ", d2)
while True :
    robot_ear = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("Robot : I'm listening...")
        audio = robot_ear.listen(mic)

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    print("You: " + you)
    

    if you == "":
        robot_brain = "I can't hear you, try again"
    elif you == "hello Friday":
        robot_brain = "Hello Boss!"
    elif you == "what day is today":
        robot_brain = d3
    elif you == "who is my crush":
        robot_brain = "You don't have any crush, boss!"
    elif you =="bye":
        robot_brain = "Bye,boss!"
    else:
        robot_brain = "I don't know, boss"
    print(robot_brain)

    engine = pyttsx3.init()
    engine.say(robot_brain)
    engine.runAndWait()
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"")

print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"")

print("BCD)

