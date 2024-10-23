Integral is an app that runs in the background that allows you to add strings to your clipboard without needing to Alt-Tab.

## How it works
While Integral is running in the background, it reads your keyboard input. Whenever you type a special character followed by one of the codes you specify, it will add the corresponding string to your clipboard.

## Why
Why not?

## Steps to install
1. Install the ```pynput```, ```pyautogui```, and ```pyperclip``` libraries (This is assuming you already have python installed. If not, install python at ```https://www.python.org/downloads/```. Make sure that Python is added to your PATH in the installer menu). To install the libraries on Windows, open a Powershell session and run ```py -m pip install <NAME_OF_LIBRARY>```, for each of the three libraries.

2. Add your codes and the corresponding strings to the ```codes``` array in integral.py.

3. Optionally, you can change the special character that must be typed before a code in line 22. Currently, the special characters are ```'#'``` and ```'$'```.

4. Navigate to the Integral directory in your terminal and run ```pyinstaller --onefile --noconsole integral.py```. Pyinstaller will build integral.py into a .exe file in ```<YOURPATH>/Integral/dist```.

5. Whenever you want to use your build of Integral, simply run the .exe, either by navigating to it on your file browser and clicking on it or by starting it from the terminal. On Linux (or in a GitBash terminal on Windows), you do this using the ```start``` command. Ex: ```start <PATH>/integral.exe```. On Windows, the command is ```Start-Process```, and you have to use the -FilePath flag. Ex: ```Start-Process -FilePath "<PATH>/integral.exe"```. Note that when you press Esc, integral is closed, so you shouldn't have to worry about task-managering it when you're done.

6. Optionally, you can create a function to run the .exe, so you don't have to navigate to it every time you want to use it. If you're a Linux user or a Windows user with Git Bash, this function can go in your ~/.bashrc file. Here's a simple example:
```
FUNCTION_NAME()
{
        start <YOUR_PATH>/Integral/dist/integral.exe
}
```

## How to use it
The app doesn't have a window. After starting the exe, integral will run in the background until you kill it (by default, the character that kills it is ESC). While it's running, whenever you type a special character (```'#'``` and ```'$'``` by default) followed by one of the codes you specified in step 2, as soon as you finish typing the code, it will be deleted, and the corresponding string will be added to your clipboard.

### Disclaimer:
Integral was created for and is only intended to be used for educational and ethically sound purposes. Use of Integral in morally questionable contexts is not encouraged.
