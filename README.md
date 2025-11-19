# COUNTER APP USING FLET


This is an advanced counter application built using Python and Flet. The app allows users to increment, decrement, and reset a counter with interactive buttons. It includes a theme toggle (light/dark mode) and automatically saves the counter value locally so that it persists across sessions.

## Features

* Increment, decrement, and reset counter.
* Counter value automatically saved locally.
* Maximum and minimum limits (0-10) with alerts.
* Theme toggle between light and dark modes.
* Reset confirmation dialog.
* User-friendly interface with snackbars for alerts.

## Requirements

* Python 3.8 or higher
* Flet library

## Installation

1. Install Python from [python.org](https://www.python.org/downloads/).
2. Install Flet using pip:

```bash
pip install flet
```

## How to Run

1. Save the Python script (`advanced_counter.py`) in a folder.
2. Open a terminal or command prompt in that folder.
3. Run the app using:

```bash
flet run advanced_counter.py
```

## How to Use

1. Click **Increment** to increase the counter (max 10).
2. Click **Decrement** to decrease the counter (min 0).
3. Click **Reset** to reset the counter (confirmation required).
4. Click the theme icon to toggle between light and dark modes.
5. Counter value is saved automatically and restored on reopening the app.

## Author

Created by Maryam Nazar — Python & Flet beginner-friendly project for interactive UI learning.
