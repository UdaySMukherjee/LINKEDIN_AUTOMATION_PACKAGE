# -*- coding: utf-8 -*-
"""
Created on Tue May 30 22:36:13 2023
@author: Uday Sankar Mukherjee
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import pyautogui as auto

# Set your LinkedIn credentials
USERNAME = input("Enter Linkedin Email")
PASSWORD = input("Enter Linkedin Password")

# Set the number of connection requests to send
NUM_REQUESTS = int(input("Entar Max Requests You want to send(<10)"))

# Set the search query to find users
SEARCH_QUERY = input("Enter the Search Query")

# Configure the Selenium webdriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maximize the browser window
driver = webdriver.Chrome(options=options)

# Load LinkedIn login page
driver.get("https://www.linkedin.com/login")

# Login to LinkedIn
driver.find_element(By.ID, "username").send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]").click()

# Wait for the LinkedIn page to load
wait = WebDriverWait(driver, 10)
search_bar = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))

# Access the search bar and type the search query
search_bar.send_keys(SEARCH_QUERY)
search_bar.send_keys(Keys.RETURN)  # Press Enter to perform the search
time.sleep(5)

x1,y1=auto.locateCenterOnScreen("Seeallpeopleresults.png",confidence=0.9)
auto.moveTo(x1,y1,1)
auto.click()
time.sleep(5)

for i in range(0, NUM_REQUESTS):
    # Locate the "Connect" button
    connect_button = auto.locateCenterOnScreen("Connect.png", confidence=0.9)
    
    # Locate the "Follow" button
    follow_button = auto.locateCenterOnScreen("Follow.png", confidence=0.9)
    
    # Check if both buttons are available
    if connect_button and follow_button:
        # If both buttons are available, check which one appears first on the screen
        if connect_button[0] < follow_button[0]:
            # Connect button appears first, click on it
            auto.moveTo(connect_button[0], connect_button[1], 1)
            auto.click()
            time.sleep(2)  # Wait for the popup to appear (adjust the delay as needed)
            
            # Check if the popup appears
            if auto.locateOnScreen("Popup.png", confidence=0.9):
                # If the popup appears, click the "Send" button
                x3, y3 = auto.locateCenterOnScreen("Send.png", confidence=0.9)
                auto.moveTo(x3, y3, 1)
                auto.click()
        else:
            # Follow button appears first, click on it
            auto.moveTo(follow_button[0], follow_button[1], 1)
            auto.click()
    elif connect_button:
        # Only the Connect button is available, click on it
        auto.moveTo(connect_button[0], connect_button[1], 1)
        auto.click()
        time.sleep(2)  # Wait for the popup to appear (adjust the delay as needed)
        
        # Check if the popup appears
        if auto.locateOnScreen("Popup.png", confidence=0.9):
            # If the popup appears, click the "Send" button
            x3, y3 = auto.locateCenterOnScreen("Send.png", confidence=0.9)
            auto.moveTo(x3, y3, 1)
            auto.click()
    elif follow_button:
        # Only the Follow button is available, click on it
        auto.moveTo(follow_button[0], follow_button[1], 1)
        auto.click()
    
    time.sleep(5)  # Wait for the connection request to be sent (adjust the delay as needed)

# Close the browser
driver.quit()
