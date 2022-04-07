from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def default():
    return "Go to URL at play"

@app.route("/play/")
def play(num = 3, color = "blue"):
    return render_template("index.html", num = int(num), color = str(color))  

@app.route("/play/<num>/")
def play_num(num = 3, color = "blue"):
    return render_template("index.html", num = int(num), color = str(color))  

@app.route("/play/<num>/<color>")
def play_num_color(num = 3, color = "blue"):
    return render_template("index.html", num = int(num), color = str(color))  














if __name__ == "__main__":
    app.run(debug=True)