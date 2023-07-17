import pyttsx3
def text(t):
    e = pyttsx3.init()
    e.say(t)
    e.runAndWait()

while True:


    print("System initialize")
    t = str(input("Enter your text: "))


    if t == 'q':
        text("BYE My friend")
        break

    text(t)
