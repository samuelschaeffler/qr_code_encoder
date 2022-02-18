from flask import Flask, render_template, url_for, request
from encoder import qr
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('site.html')

@app.route("/action_page", methods=['POST', "GET"])
def action_page():
    if request.method == "POST":
       content = request.form.get("content") 
       print("Request to generate QR Code for: "+content)
       qr(content)
    return render_template('action_page.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)