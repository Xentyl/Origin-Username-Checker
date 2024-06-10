import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Load your list of usernames from the text file
with open('usernames.txt', 'r') as file:
    usernames = file.read().splitlines()

# Initialize the WebDriver (ensure the path to chromedriver is correct)
driver = webdriver.Chrome()  # or specify the path: webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open the EA login page
driver.get('https://myaccount.ea.com/cp-ui/aboutme/index')

# Wait for page to load and manual login
input("Press Enter after manually logging in...")

# Click the "Edit" button to bring up the username input box
edit_button = driver.find_element(By.ID, 'editBasicInformation')
edit_button.click()

# Wait for the username input field to appear
time.sleep(2)  # Adjust based on the website's response time

# Function to check if a username is taken
def check_username(username):
    # Locate the username input field and clear it
    username_input = driver.find_element(By.ID, 'ebi_originId-input')
    username_input.clear()
    
    # Input the username
    username_input.send_keys(username)
    username_input.send_keys(Keys.TAB)  # Simulate pressing Tab
    
    # Wait for the response
    time.sleep(2)  # Adjust this based on the website's response time
    
    # Check for the presence of the error message indicating a prohibited word or character
    error_message = driver.find_elements(By.XPATH, "//span[contains(@class, 'origin-ux-textbox-status-message') and contains(text(), 'ID contains a prohibited word or character')]")
    if error_message:
        # If the error message is found, flag the username and stop the script
        with open('flaggedusers.txt', 'a') as f:
            f.write(f'{username}\n')
        return 'error'
    else:
        # If no error message, proceed with checking if the username is taken or available
        username_field = driver.find_element(By.ID, 'container_origin_id')
        class_attribute = username_field.get_attribute('class')
        if 'field-error' in class_attribute:
            return 'taken'  # If the field-error class is present, the username is taken
        else:
            return 'available'  # If the field-error class is not present, the username is available

# List to collect taken and available usernames
taken_usernames = []
available_usernames = []

# Iterate through the list of usernames and check availability
for username in usernames:
    result = check_username(username)
    if result == 'taken':
        print(f'{username} is taken')
        taken_usernames.append(username)
    elif result == 'available':
        print(f'{username} is available')
        available_usernames.append(username)
    elif result == 'error':
        print(f'{username} contains a prohibited word or character')
        break  # Stop the script if an error occurs

# Close the browser
driver.quit()

# Write the taken usernames to a file
with open('taken_usernames.txt', 'w') as file:
    for username in taken_usernames:
        file.write(f'{username}\n')

# Write the available usernames to a file
with open('available_usernames.txt', 'w') as file:
    for username in available_usernames:
        file.write(f'{username}\n')

print('Check completed. Taken usernames have been saved to taken_usernames.txt and available usernames to available_usernames.txt.')

