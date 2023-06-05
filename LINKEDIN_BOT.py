import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import pyautogui as auto

def start_automation():
    # Set your LinkedIn credentials
    USERNAME = text1_entry.get()
    PASSWORD = text2_entry.get()

    # Set the number of connection requests to send
    NUM_REQUESTS = int(text3_entry.get())

    # Set the search query to find users
    SEARCH_QUERY = text4_entry.get()

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

    x1, y1 = auto.locateCenterOnScreen("assets\\Seeallpeopleresults.png", confidence=0.9)
    auto.moveTo(x1, y1, 1)
    auto.click()
    time.sleep(5)

    for i in range(0, NUM_REQUESTS):
        # Locate the "Connect" button
        connect_button = auto.locateCenterOnScreen("assets\\Connect.png", confidence=0.9)

        # Locate the "Follow" button
        follow_button = auto.locateCenterOnScreen("assets\\Follow.png", confidence=0.9)

        # Check if both buttons are available
        if connect_button and follow_button:
            # If both buttons are available, check which one appears first on the screen
            if connect_button[0] < follow_button[0]:
                # Connect button appears first, click on it
                auto.moveTo(connect_button[0], connect_button[1], 1)
                auto.click()
                time.sleep(2)  # Wait for the popup to appear (adjust the delay as needed)

                # Check if the popup appears
                if auto.locateOnScreen("assets\\Popup.png", confidence=0.9):
                    # If the popup appears, click the "Send" button
                    x3, y3 = auto.locateCenterOnScreen("assets\\Send.png", confidence=0.9)
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
            if auto.locateOnScreen("assets\\Popup.png", confidence=0.9):
                # If the popup appears, click the "Send" button
                x3, y3 = auto.locateCenterOnScreen("assets\\Send.png", confidence=0.9)
                auto.moveTo(x3, y3, 1)
                auto.click()
        elif follow_button:
            # Only the Follow button is available, click on it
            auto.moveTo(follow_button[0], follow_button[1], 1)
            auto.click()

        time.sleep(5)  # Wait for the connection request to be sent (adjust the delay as needed)

    # Close the browser
    driver.quit()
    
    # Show a pop-up message
    messagebox.showinfo("Requests Sent", "All Connection requests sent successfully!")

# Create the main window
window = tk.Tk()
window.title("Linkedin Automation Tool")
window.geometry("800x400")
window.resizable(width=False, height=False)  # Disable window resizing

# Create the left container
left_container = tk.Frame(window, bg="#ffffff", width=400, height=400)
left_container.place(x=0, y=0)

# Add the logo.png on the top left corner of the left container
logo_image = Image.open("assets\\logo.png")
logo_image = logo_image.resize((100, 100), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(left_container, image=logo_photo, bg="#ffffff")
logo_label.place(x=140, y=10)

# Add 4 text boxes and text on the left container with left alignment
text1_label = tk.Label(left_container, text="Username:", anchor="w", bg="#ffffff")
text1_label.place(x=10, y=150)
text1_entry = tk.Entry(left_container, width=35)
text1_entry.place(x=110, y=150)

text2_label = tk.Label(left_container, text="Password:", anchor="w", bg="#ffffff")
text2_label.place(x=10, y=180)
text2_entry = tk.Entry(left_container, width=35, show="*")
text2_entry.place(x=110, y=180)

text3_label = tk.Label(left_container, text="No. of Requests:", anchor="w", bg="#ffffff")
text3_label.place(x=10, y=210)
text3_entry = tk.Entry(left_container, width=35)
text3_entry.place(x=110, y=210)

text4_label = tk.Label(left_container, text="Search Query:", anchor="w", bg="#ffffff")
text4_label.place(x=10, y=240)
text4_entry = tk.Entry(left_container, width=35)
text4_entry.place(x=110, y=240)

# Add a start button with round edges on the left container
start_button = tk.Button(left_container, text="Do Automate", bg="#3498db", fg="#ffffff", relief="flat", bd=0, padx=10, pady=5, borderwidth=0, highlightthickness=0, highlightbackground="#ffffff", command=start_automation)
start_button.config(width=15)
start_button.place(x=130, y=280)

# Create the right container
right_container = tk.Frame(window, width=450, height=400)
right_container.place(x=350, y=0)

# Load and display the image.png on the right container
image = Image.open("assets\\image.jpg")
image = image.resize((450, 400), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(right_container, image=photo)
image_label.place(x=0, y=0)

# Load the background image
bg_image = Image.open("assets\\bg_image.png")
bg_image = bg_image.resize((440, 370), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Add texts on the image of the right container
text_overlay = tk.Label(right_container, text="This project is a Python script that automates\n LinkedIn actions using the Selenium library. \nIt allows users to log in to LinkedIn, search \nfor users based on a query, and send connection \nrequests. The script uses image recognition to\n locate and interact with buttons on the LinkedIn\n website. The script provides a customizable\n number of connection requests to send", fg="#000000", font=("Arial", 12,"bold"), padx=10, pady=5)
text_overlay.config(width=355, height=250, image=bg_photo, compound="center")
text_overlay.place(x=37, y=78)

# Start the tkinter event loop
window.mainloop()
