# Origin Username Checker

This script automates the process of checking username availability on the EA website. It reads usernames from a text file, inputs them on the EA account page, and determines if they are available or taken based on the presence of specific error messages.

## Prerequisites

- Python 3.6 or later
- [Selenium](https://www.selenium.dev/)
- [colorama](https://pypi.org/project/colorama/)
- Chrome WebDriver

## Installation

1. **download all Prerequisites:**

2. **Download ChromeDriver:**
    - Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    - Place it in the project directory or ensure it is in your system PATH.

4. **Create or edit the `usernames.txt` file:**
    - In the project directory, create or edit the `usernames.txt` file.
    - Add the usernames you want to check, one per line.

## Usage

1. **Run the script:**
    ```sh
    python Check_usernames.py
    ```

2. **Log in manually:**
    - The script will open a browser window and navigate to the EA login page.
    - Manually log in to your EA account.
    - if you are asked for a 2fa code for log in, do it
    - once everything is good, click OFF of the tab that popped up letting you edit your information. The script need to press the "EDIT" button on the EA website for it to work

3. **Start the checking process:**
    - Once logged in, return to the terminal and press Enter to start the script.

4. **Results:**
    - The script will check each username and classify them as "available," "taken,".
    - Usernames that are marked as "FLAGGED" will immeditly be marked and the script will shut down. This is because of EA's username system, once a username has been flagged as innapropriate it will PREVENT you from imputting ANY username for ~10 minutes.
    - if you have a workaround to this issue please let me know

## Script Behavior

- The script will save the results in three text files:
  - `available_usernames.txt`: Contains usernames that are available.
  - `taken_usernames.txt`: Contains usernames that are taken.
  - `flagged_usernames.txt`: Contains usernames that contain prohibited words or characters.

