import telegram
import os
from flask import Flask, request

from flask import render_template

# Create the Flask app
app = Flask(__name__)

# Get the bot token and chat ID from environment variables
bot_token = os.environ.get("BOT_TOKEN")
chat_id = os.environ.get("CHAT_ID")

# Create the bot
bot = telegram.Bot(token=bot_token)

# Set up the route for the webhook
@app.route("/webhook", methods=["POST"])
def webhook():
    # Get the update from the request
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    # Get the user and message from the update
    user = update.message.from_user
    message = update.message.text

    # Check if the message is "/start"
    if message == "/start":
        # Send a welcome message to the user
        bot.send_message(chat_id=chat_id, text="Welcome to the bot! How can I help you today?")
    else:
        # Send the message to the admin panel for processing
        process_message(user, message)

    return "ok"

# Set up the route for the admin panel
@app.route("/admin", methods=["GET", "POST"])
def admin_panel():
    # Check if the request is a POST request
    if request.method == "POST":
        # Get the user and message from the form
        user = request.form["user"]
        message = request.form["message"]

        # Send the message to the user
        bot.send_message(chat_id=user, text=message)

        # Redirect to the admin panel
        return redirect("/admin")
    else:
        # Render the admin panel template
        return render_template("admin_panel.html")

# Set up the route for the admin panel
@app.route("/users", methods=["GET", "POST"])
def users_panel():
    # Check if the request is a POST request
    if request.method == "POST":
        # Get the user and action from the form
        user = request.form["user"]
        action = request.form["action"]

        # Perform the appropriate action
        if action == "add":
            add_user(user)
        elif action == "delete":
            delete_user(user)

        # Redirect to the users panel
        return redirect("/users")
    else:
        # Get the list of users
        users = get_users()

        # Render the users panel template
        return render_template("users_panel.html", users=users)

# Set up the route for the webhook
@app.route("/set_webhook", methods=["GET", "POST"])
def set_webhook():
    # Set the webhook for the bot
    bot.set_webhook(url=request.url_root + "webhook")
    return "webhook set"

# Run the app
if __name__ == "__main__":
    app.run()
