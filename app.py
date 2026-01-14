from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed to use session

@app.route("/", methods=["GET", "POST"])
def index():
    # If no secret number in session, generate one
    if "secret_number" not in session:
        session["secret_number"] = random.randint(1, 100)

    message = None
    if request.method == "POST":
        try:
            guess = int(request.form.get("guess"))
            secret_number = session["secret_number"]

            if guess < secret_number:
                message = "Too low! Try again."
            elif guess > secret_number:
                message = "Too high! Try again."
            else:
                message = "🎉 Correct! The game has reset — try again!"
                # Reset the number for a new challenge
                session["secret_number"] = random.randint(1, 100)
        except:
            message = "Please enter a valid number."
    
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
