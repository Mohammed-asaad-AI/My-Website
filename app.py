from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generic")
def generic():
    return render_template("generic.html")


@app.route("/elements")
def elements():
    return render_template("elements.html")


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "your-secret-key"

# إعدادات البريد الإلكتروني (مثال باستخدام Gmail)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "your.email@gmail.com"  # بريد المرسل
app.config["MAIL_PASSWORD"] = (
    "your-app-password"  # كلمة مرور التطبيق (وليس كلمة مرور Gmail العادية)
)

mail = Mail(app)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/send_email", methods=["POST"])
def send_email():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    msg = Message(
        f"New message from {name}",
        sender=app.config["MAIL_USERNAME"],
        recipients=["mo.asaad999@gmail.com"],
    )  # بريدك أنت

    msg.body = f"From: {name} <{email}>\n\nMessage:\n{message}"

    try:
        mail.send(msg)
        flash("Message sent successfully!", "success")
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "danger")

    return redirect("/")
