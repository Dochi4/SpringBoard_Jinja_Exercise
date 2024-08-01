from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story,story

app = Flask(__name__)

app.config['SECRET_KEY'] = "storytime"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Shows madelibs home page"""
    return render_template("madlibs_home.html", prompts=story.prompts)

@app.route("/madlibs_story")
def show_story():
    answers = {prompt: request.args[prompt] for prompt in story.prompts}
    generated_story = story.generate(answers)
    return render_template('madlibs_story.html', story=generated_story)