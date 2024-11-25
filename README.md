# Basic Keylogger Program

This project is a simple keylogger built using Python's `pynput` library. It records keystrokes and saves them to a log file for educational and ethical use only.

## Features

- Logs all printable characters and special keys (e.g., `Enter`, `Backspace`).
- Saves keystrokes to a file named `keylog.txt`.
- Exits gracefully when the `Esc` key is pressed.

## Requirements

- Python 3.x
- `pynput` library

## Installation

1. Clone the repository or download the script.
2. Install the required library:
   ```bash
   pip install pynput
Usage
Run the script:
bash
Copy code
python keylogger.py
The program will record all keystrokes and save them to a file named keylog.txt in the current directory.
Press the Esc key to stop the keylogger.
Example Output
If you type "Hello World!" followed by pressing Enter, the keylog.txt file will look like this:

css
Copy code
Hello World! [Key.enter]
Notes
Ethical Considerations: This program should only be used on devices you own or with explicit permission from the owner. Unauthorized use is a violation of privacy and may be illegal.
Permissions: Ensure you have permission to test or run this program on any device.
Log File Location: The keystrokes are saved in a file named keylog.txt in the directory where the script is executed.
License
This project is licensed under the MIT License.

Disclaimer
This tool is for educational purposes only. The developers are not responsible for any misuse of this software.

yaml
Copy code

---

### **Ethical Disclaimer**
Keyloggers have potential for misuse. Always ensure:
- You have explicit permission to use it.
- You comply with applicable laws and regulations.
- The program is used responsibly and transparently. 

Let me know if you’d like to enhance this with additional features, such as logging timestamps or implementing encryption for the logs!










