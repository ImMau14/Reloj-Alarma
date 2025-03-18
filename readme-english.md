# Alarm Clock

[Idioma español](./readme.md)

This is an alarm clock made in Tkinter for the purpose of setting an alarm on my computer. It was developed on Windows, but hasn't been tested on Linux yet. It's only in Spanish, but I'll probably translate it to English.

|<img src="https://cdn.discordapp.com/attachments/697811476362035251/1351421123249569832/image.png?ex=67da507f&is=67d8feff&hm=bf4df0a62c1490f26fab8b7e236d57515a2cf40da1d503963f12f3c40aba4df1&">|<img src="https://cdn.discordapp.com/attachments/697811476362035251/1351421186701262889/image.png?ex=67da508f&is=67d8ff0f&hm=05142fd563346a5d82daf928690de3ad039ac88b818e2b0f15fb20a9830202ad&">|
|:-:|:-:|
|Light theme interface|Dark theme interface|

## Features

* Plays a sound in the background that can be customized or disabled.
* Displays an on-screen message that can be disabled or customized.
* Allows you to choose whether or not to run a program.

* Allows you to select between 24-hour and 12-hour formats in the interface.
* Allows you to choose between a light or dark theme in the interface.
* Allows you to choose whether to display the hour, minutes, or seconds in the interface.

## Possible Errors

### Fonts not displaying correctly

In the root folder, there is a folder called **fonts**, which contains the fonts used in the project. Install them and restart the application.

### Dependencies
This project uses **Pillow** for images (custom widgets) and **PyGame** (sound). Make sure you have them installed before running.

You can use the following command in the root directory to install these libraries:
```
pip install -r requirements.txt
```