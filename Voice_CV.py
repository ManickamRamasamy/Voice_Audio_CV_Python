# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()


# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Loop infinitely for user to
# speak

while (1):

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:
            welcome = "Welcome to my bio data with voice recognization app \n Would you like to say something \n Please confirm shall we continue with bio data or else say 'close' or 'exit' to close the execution"
            print (welcome)
            SpeakText(welcome)

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.1)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            MyText1 = str(MyText.lower())

            print("Me : " + MyText)
            SpeakText(MyText)
            Exit = "close"
            if MyText1 == "exit" or MyText1 == "close":
                print ("Thank you!!")
                exit()
            else:
                with open("Biodata.txt", "r") as file:
                    rows = (line.split('=') for line in file)
                    dict = {row[0]: row[1] for row in rows}
                    file.close()
                    for keys, values in dict.items():
                        print(keys)
                        SpeakText(dict[keys])
                        print (values)
                    print("Would you like to 'Repeat it' with next set or 'exit/close' : ")



    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")