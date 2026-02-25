from gemini_connect import get_ai_response

def prompt_generation(duration, goal, topics, hours):
    prompt = f"Make a {goal} study plan for {duration}. I study {hours} hours a day. Focus more on {topics}. include A week by week schedule,What to study each day, A table of all topics with difficulty and resources, Highlight {topics} in a different color, return mandatory as html only and all tags should be placed inside body tag"
    return prompt

from flask import Flask, render_template, request
from google import genai




app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def gnerate_study_view():
    if request.method == 'GET':
        return render_template('generate_study_hours.html')
    elif request.method == 'POST':
        duration=request.form['duration']
        goal=request.form['goal']
        hours=request.form['hours']
        topic=request.form['topic']

        prompt=prompt_generation(duration, goal, topic, hours)
        response = get_ai_response(prompt)
        return render_template('study_hours_result.html', ans = response)


if __name__ == '__main__':
    app.run(debug=True)