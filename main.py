from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    menu_options = ["Option 1", "Option 2", "Option 3"]
    return render_template("index.html", menu_options=menu_options)

def handle_button():
    # Perform some action here
    return "Button pressed!"

if __name__ == "__main__":
    app.run()
