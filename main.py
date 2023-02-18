import time
from plyer import notification

while True:
    # Send the Notification
    notification.notify(
        app_icon = 'water-glass-color-icon.ico',
        title = "Reminder :)",
        message = "Stay Hydrated by Drinking Water !!",
        timeout = 15
    )
    # Remind every hour
    time.sleep(3600)
