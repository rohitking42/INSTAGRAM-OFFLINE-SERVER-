from flask import Flask, request, render_template, redirect, url_for
import time
import os

# Flask app initialization
app = Flask(__name__)
app.debug = True

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Fetch form data
        username = request.form.get("username")
        password = request.form.get("password")
        choice = request.form.get("choice")
        target_username = request.form.get("target_username")
        thread_id = request.form.get("thread_id")
        haters_name = request.form.get("haters_name")
        delay = int(request.form.get("delay"))

        # Process the uploaded file
        message_file = request.files["message_file"]
        if message_file and message_file.filename.endswith(".txt"):
            messages = message_file.read().decode("utf-8").splitlines()
        else:
            return "Invalid file format. Please upload a .txt file containing messages."

        # Simulate message sending (You can integrate Instagram Private API here)
        for message in messages:
            if choice == "inbox" and target_username:
                print(f"Sending to {target_username}: {haters_name}, {message}")
            elif choice == "group" and thread_id:
                print(f"Sending to Group {thread_id}: {haters_name}, {message}")
            else:
                return "Please provide valid target details."

            time.sleep(delay)

        return "Messages sent successfully!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
      
