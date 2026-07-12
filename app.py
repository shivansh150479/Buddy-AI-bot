from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import pyttsx3
app = Flask(__name__)
engine = pyttsx3.init()
engine.setProperty("rate", 170)
def speak(text):
    engine.say(text)
    engine.runAndWait()
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data["message"].lower()
    if "hello" in message:
        reply = "Hello! aur buddy kaaisse ho.."
    elif "joke" in message:
        reply = "i dont have time to tell you joke i am busy do study its 11"
    elif "made" in message:
        reply = "i am made by Shivansh Bajpai"
    
        
        
        
    elif "time" in message:
            from datetime import datetime
            reply = datetime.now().strftime("%I:%M %p")
    elif "your name" in message:
            reply = "My name is Buddy."
    elif "dog" in message:
        reply = "you are a dog i am buddy.... "
    elif "mc" in message:
        reply = "you bc"
    elif "dont know anything" in message:
        reply = "i am learning but what are you doing ,waisting your time"    
    
            
            
            
            
            
            
    
    else:
            reply = "not in my memory."
    #speak(reply)
    return jsonify({"reply": reply})
#@app.route("/listen")
#def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("listening")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return jsonify({"text": text})
    except:
        return jsonify({"text": ""})
if __name__=="__main__":
    app.run(host="127.0.0.1", port=8000, debug=False, use_reloader=False)