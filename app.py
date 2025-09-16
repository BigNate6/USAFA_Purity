from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# --- YOUR PYTHON LOGIC GOES HERE ---
# For this example, let's create a simple function.
# Replace this with your actual program's logic.
def generate_sentence(user_input):
    # Example: Just repeats the user's input in a sentence.
    if not user_input:
        return ""
    return f"You told me this: '{user_input}'!"
# ------------------------------------

@app.route('/', methods=['GET', 'POST'])
def home():
    # This is the default text shown on the page
    result_sentence = ""

    # This block runs when the user submits the form
    if request.method == 'POST':
        # Get the text from the form's input box
        user_text = request.form.get('user_input')
        # Run your function with the user's text
        result_sentence = generate_sentence(user_text)

    # This sends the result back to the HTML page to be displayed
    return render_template('index.html', result=result_sentence)

if __name__ == '__main__':
    app.run(debug=True)