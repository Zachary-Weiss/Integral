from pynput import keyboard
import pyautogui
import time
import pyperclip
import random
import sys

# Define your codes and corresponding texts
codes = {
    "t1": "This is what will be added to your clipboard."
}

# Global variable to hold the current input code
current_code = ''

# Function to handle key presses 
def on_press(key):
    global current_code 
    try:
        if hasattr(key, 'char'):
            if key.char == '#' or key.char == '$':  # Trigger with # or $
                current_code = ''  # Clear the current code 
            elif key.char is not None:
                current_code += key.char  # Append character to code 
                
            if current_code in codes:
                text = codes[current_code]
                pyautogui.typewrite((1 + len(current_code)) * "\b") #delete the code that was just typed, including the special char
                pyperclip.copy(text) # Add the text to the clipboard

                print()  # Print a newline after the message. This is so you can keep track of the strings you've copied in the terminal
                current_code = ''  # Reset after typing the text


        if key == keyboard.Key.esc:  # Exit on ESC key
            #return False  # Stop listener
            sys.exit()

    except Exception as e:
        print(f"Error: {e}")

# Set up the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()