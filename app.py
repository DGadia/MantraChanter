from flask import Flask, render_template, request
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    audio_file = None
    if request.method == "POST":
        text = request.form["text"]
        repeat = int(request.form["repeat"])
        lang = request.form["language"]  # get selected language

        final_text = " ".join([text] * repeat)

        tts = gTTS(final_text, lang=lang)
        audio_file = "static/output.mp3"
        tts.save(audio_file)

    return render_template("index.html", audio_file=audio_file)


if __name__ == "__main__":
    app.run(debug=True)
