from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = "1234abcde"
users = {
    "user@example.com": "password123"
}


@app.route("/")
def home():
    return render_template("index.html")



#login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Authentication logic
        if email in users and users[email] == password:
            flash("Login successful!", "success")
            return redirect(url_for("home_page"))
        else:
            flash("Invalid email or password. Please try again.", "danger")
            return redirect(url_for("login"))

    return render_template("authentication/loginPage.html")

@app.route("/home")
def home_page():
    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(debug=True)