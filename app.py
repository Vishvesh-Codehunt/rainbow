from flask import Flask, render_template,redirect,request, url_for
from flask_mail import Mail, Message
# import pymysql.cursors

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='tt3013194@gmail.com'
app.config['MAIL_PASSWORD']='Vishvesh3541@'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

app.secret_key = "abdhghsb"

mail = Mail(app)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/email", methods=["POST"])
def email():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    # sql = "INSERT INTO contact (name, email, message) VALUES (%s, %s, %s)"
    # val = (name, email, message)
    # Con.ping(reconnect=True)
    # cur.execute(sql,val)
    # Con.commit()
    msg = Message('Someone wants to contact you!', sender = 'tt3013194@gmail.com', recipients = ['patelvishvesh85@gmail.com'])
    msg.body = f"name: {name}\nemail: {email}\nmessage: {message}"
    mail.send(msg)
    return redirect(url_for('home'))

@app.route("/subscribe", methods=["POST"])
def subscribe():
    # email = request.form["email"]
    # Con.ping(reconnect=True)
    # cur.execute("INSERT INTO newslatter (email) VALUES (%s)", (email,))
    # Con.commit()
    msg = Message('Someone has subscribed to your newslatter!', sender = 'tt3013194@gmail.com', recipients = ['patelvishvesh85@gmail.com'])
    msg.body = f"email: {email} has subscribed to your newslatter."
    mail.send(msg)
    return redirect(url_for('home'))
if __name__ == "__main__":
    app.run(debug=True)