from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this to a more secure key in production

MIN_NUMBER = 1
MAX_NUMBER = 100

@app.route("/", methods=["GET", "POST"])
def index():
    """Main game route - handles both displaying the game and processing guesses."""

    if "secret_number" not in session:
        session["secret_number"] = random.randint(MIN_NUMBER, MAX_NUMBER)

    if "attempts" not in session:
        session["attempts"] = 0

    message = None
    message_type = "info"

    if request.method == "POST":
        try:
            guess_input = request.form.get("guess", "").strip()

            if not guess_input:
                message = "Please enter a number."
                message_type = "error"
            else:
                guess = int(guess_input)
                secret_number = session["secret_number"]

                if guess < MIN_NUMBER or guess > MAX_NUMBER:
                    message = f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}."
                    message_type = "error"
                else:
                    session["attempts"] += 1

                    if guess < secret_number:
                        message = f"❄️ Too low! (Attempt {session['attempts']})"
                    elif guess > secret_number:
                        message = f"🔥 Too high! (Attempt {session['attempts']})"
                    else:
                        message = f"🎉 Correct! Attempts: {session['attempts']}"
                        message_type = "success"
                        session["secret_number"] = random.randint(MIN_NUMBER, MAX_NUMBER)
                        session["attempts"] = 0

        except ValueError:
            message = "Please enter a valid number."
            message_type = "error"

    return render_template(
        "index.html",
        message=message,
        message_type=message_type
    )

@app.route("/reset", methods=["POST"])
def reset():
    """Reset the game."""
    session["secret_number"] = random.randint(MIN_NUMBER, MAX_NUMBER)
    session["attempts"] = 0
    return render_template("index.html", message="Game reset! Good luck! 🍀", message_type="info")

if __name__ == "__main__":
    app.run(debug=True)
