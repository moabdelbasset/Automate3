from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    menu_options = ["Option 1", "Option 2", "Option 3"]
    return render_template("index.html", menu_options=menu_options)

@app.route("/handle_button", methods=["POST"])
def handle_button():
    selected_option = request.form["dropdown"]
    # Perform some action based on the selected option
#    return "Button pressed! Selected option: {}".format(selected_option)
    return f"You selected: {selected_option}"
if __name__ == "__main__":
    app.run()
