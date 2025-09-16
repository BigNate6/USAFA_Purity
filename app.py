from flask import Flask, render_template, request
from pathlib import Path
app = Flask(__name__)
script_dir = Path(__file__).parent
file_path = script_dir / "questions.txt"

# --- Create your list of 100 questions here ---
# For this example, I'll create a few and multiply them.
# You should replace these with your actual questions.
question_list = []
with open(file_path) as fil:
    for line in fil:
        question_list.append(str(line))
    fil.close()
# Let's make the list 100 questions long for this demo
questions = question_list

@app.route('/', methods=['GET', 'POST'])
def home():
    result_text = ""
    if request.method == 'POST':
        # This is the new logic to tally the 'yes' answers
        score = 100
        for value in request.form.values():
            if value == 'yes':
                score -= 1
        
        result_text = f"Your Score: {score}"

    # We pass the list of questions to the HTML template
    return render_template('index.html', questions=questions, result=result_text)

if __name__ == '__main__':
    app.run(debug=True)