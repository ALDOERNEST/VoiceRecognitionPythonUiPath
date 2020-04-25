import speech_recognition as sr
def main():
	r = sr.Recognizer()

	with sr.Microphone() as source:
	    print("Say Something...")
	    audio = r.listen(source)

	    try:
	        text = r.recognize_google(audio, language='en-US')
	        return "What did you say: {}".format(text);
	    except:
	         return "I am sorry! I can not understand!";
if __name__ == '__main__':
    print(main());
