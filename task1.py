import time
from plyer import notification

notification_title = 'Hello'
notification_message = 'Drink Some Water. Have a Nice Day.'

notification.notify(
    title = notification_title,
    message = notification_message,
    app_icon = r"C:/Users/Yashraj/OneDrive/Documents/SYNC/python.ico",
    timeout = 10,
    toast = False
    )