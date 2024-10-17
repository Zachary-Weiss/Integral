from pynput import keyboard
import pyautogui
import time
import pyperclip
import random

# Define your codes and corresponding texts
codes = {
    "t1": "This is what will be added to your clipboard."
}

# Global variable to hold the current input code
current_code = ''
type_speed = 0.01
stopTyping = False

# Function to handle key presses 
def on_press(key):
    global current_code 
    try:
        if hasattr(key, 'char'):
            if key.char == '#' or key.char == '$':  # Trigger with # 
                current_code = ''  # Clear the current code 
            elif key.char is not None:
                current_code += key.char  # Append character to code 
                
            if current_code in codes:
                """
                if current_code[0] == "#":
                    # Print and type each character with a random delay
                    text = codes[current_code]
                    pyautogui.typewrite((1 + len(current_code)) * "\b")
                    #pyautogui.typewrite(text)
                    for char in text:
                        print(char, end='', flush=True)  # Print character without newline
                        time.sleep(type_speed)
                        pyautogui.typewrite(char)  # Type the character"""
                # Add the text to the clipboard
                text = codes[current_code]
                pyautogui.typewrite((1 + len(current_code)) * "\b")
                pyperclip.copy(text) #

                print()  # Print a newline after the message
                current_code = ''  # Reset after typing the text


        if key == keyboard.Key.esc:  # Exit on ESC key
            return False  # Stop listener

    except Exception as e:
        print(f"Error: {e}")

# Set up the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()