import time
from plyer import notification

if __name__ == '__main__':
    print("Notification Reminder Loop Started...")
    
    # This loop will keep running in the background
    while True:
        notification.notify(
            title="Time to Code!",
            message="Hey Srijani,open VS Code and start coding! Remember, consistency is key to becoming a great programmer.",
            app_name="RoboHelper",
            timeout=1800
        )
        
        print("Notification sent! Next reminder will be after 30 minutes.")
        
        # 1800 seconds = 30 minutes (30 * 60 seconds)
        time.sleep(1800)  # Wait for 30 minutes before sending the next notification
