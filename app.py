from flask import Flask, render_template, request, jsonify
from strong import generate_password, check_password_strength, MIN_LENGTH, MIN_DIGITS, MIN_UPPERCASE, MIN_LOWERCASE, MIN_SPECIAL, SPECIAL_CHARACTERS

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    password = ""
    message = ""
    issues = []
    show_modal = False
    guidelines_text = ""

    if request.method == "POST":
        action = request.form.get("action")

        if action == "generate":
            password = generate_password()
            message = "Generated a strong password."

        elif action == "check":
            password = request.form.get("password", "")
            if password:
                is_strong, issues = check_password_strength(password)
                message = "Your password is strong!" if is_strong else "Weak password detected."
            else:
                message = "Please enter a password to check."

        elif action == "guidelines":
            show_modal = True
            guidelines_text = (
                f"Password Guidelines:\n"
                f"- Minimum {MIN_LENGTH} characters\n"
                f"- At least {MIN_DIGITS} digits\n"
                f"- At least {MIN_UPPERCASE} uppercase letters\n"
                f"- At least {MIN_LOWERCASE} lowercase letters\n"
                f"- At least {MIN_SPECIAL} special characters ({SPECIAL_CHARACTERS})\n"
                f"- Avoid common words or patterns like '123456', 'password', etc."
            )

    return render_template(
        "index.html",
        password=password,
        message=message,
        issues=issues,
        show_modal=show_modal,
        guidelines_text=guidelines_text
    )


if __name__ == "__main__":
    app.run(debug=True)
