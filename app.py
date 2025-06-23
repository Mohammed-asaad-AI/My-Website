from flask import Flask, render_template, request, redirect,url_for, flash
from flask_mail import Mail, Message
import smtplib 
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = "your-secret-key"

# إعدادات البريد الإلكتروني
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "hammaasaad@gmail.com"  # بريد المرسل
app.config["MAIL_PASSWORD"] = "bpfu uldm rozb yxhb"  # App Password من Google

mail = Mail(app)


# الصفحة الرئيسية
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# صفحة generic
@app.route("/generic")
def generic():
    return render_template("generic.html")


# صفحة elements
@app.route("/elements")
def elements():
    return render_template("elements.html")


# إرسال البريد من النموذج
@app.route("/send_email", methods=["POST"])
def send_email():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    msg = Message(
        subject=f"New message from {name}",
        sender=app.config["MAIL_USERNAME"],
        recipients=["mo.asaad999@gmail.com"],
        body=f"From: {name} <{email}>\n\nMessage:\n{message}",
    )

    try:
        mail.send(msg)
        flash(" Message sent successfully!", "success")
    except Exception as e:
        print(" Email send failed:", e)  # ← هذا مهم جداً لكشف الخطأ
        flash(f" An error occurred: {str(e)}", "danger")

    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
