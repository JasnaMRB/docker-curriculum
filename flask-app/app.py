from flask import Flask, render_template
import random

app = Flask(__name__)

# list of animal images
images = [
    "https://media.giphy.com/media/nNxT5qXR02FOM/giphy.gif",
    "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif",
    "https://media.giphy.com/media/l0MYNB04rBb51QNtC/giphy.gif",
    "https://media.giphy.com/media/11s7Ke7jcNxCHS/giphy.gif",
    "https://media.giphy.com/media/Sj3cnA7JYMENy/giphy.gif",
    "https://media.giphy.com/media/HnYefmiEyBKo0/giphy.gif",
    "https://media.giphy.com/media/qLopWKCbz6UoM/giphy.gif",
    "https://media.giphy.com/media/uwANH4MWtmGHe/giphy.gif",
    "https://media.giphy.com/media/1P2puPdOem9tC/giphy.gif",
    "https://media.giphy.com/media/9pq81D1EJ5XvG/giphy.gif",
    "https://media.giphy.com/media/4nGYmLsCoHNXa/giphy.gif",
    "https://media.giphy.com/media/WEGvLnkGLMqc0/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
