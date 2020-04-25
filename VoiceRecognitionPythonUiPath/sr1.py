import speech_recognition as sr
def main():
	r = sr.Recognizer()

	with sr.Microphone() as source:
	    	print("Say Something...")
		audio = r.adjust_for_ambient_noise(source)
	    	audio = r.listen(source)
	    	try:
	        	text = r.recognize_google(audio, language='es-PE')
	        	print("What did you say: {}".format(text))
	    	except:
	        	print("I am sorry! I can not understand!")
if __name__ == '__main__':
    main()