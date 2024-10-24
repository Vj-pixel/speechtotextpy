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
    
# Loop infinitely for user to speak
while(1):    
    
    # Exception handling to handle exceptions at runtime
    try:
        
        # Use the microphone as the source for input
        with sr.Microphone() as source2:
            
            # Wait for a second to let the recognizer adjust
            # the energy threshold based on the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            # Listen for the user's input
            audio2 = r.listen(source2)
            
            # Using Google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            # Corrected print statement
            print("Did you say:", MyText)
            SpeakText(MyText)
            
            if (MyText == "skibidi"):
                SpeakText("That's not a nice word!")
                
            if (MyText == "exit"):
                SpeakText("Ok, bye bye!")
                exit();
            
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        
    except sr.UnknownValueError:
        print("Unknown error occurred")
