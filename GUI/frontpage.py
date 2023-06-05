import tkinter as tk
from PIL import ImageTk, Image

# Create the main window
window = tk.Tk()
window.title("Linkedin Automation Tool")
window.geometry("800x400")

# Create the left container
left_container = tk.Frame(window, bg="#ffffff", width=400, height=400)
left_container.place(x=0, y=0)

# Add the logo.png on the top left corner of the left container
logo_image = Image.open("logo.png")
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

text2_entry = tk.Entry(left_container, width=35)
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
start_button = tk.Button(left_container, text="Do Automate", bg="#3498db", fg="#ffffff", relief="flat", bd=0, padx=10, pady=5, borderwidth=0, highlightthickness=0, highlightbackground="#ffffff")
start_button.config(width=15)
start_button.place(x=130, y=280)

# Create the right container
right_container = tk.Frame(window, width=450, height=400)
right_container.place(x=350, y=0)

# Load and display the image.png on the right container
image = Image.open("image.jpg")
image = image.resize((450, 400), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(right_container, image=photo)
image_label.place(x=0, y=0)

# Load the background image
bg_image = Image.open("bg_image.png")
bg_image = bg_image.resize((440, 370), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Add texts on the image of the right container
text_overlay = tk.Label(right_container, text="This project is a Python script that automates\n LinkedIn actions using the Selenium library. \nIt allows users to log in to LinkedIn, search \nfor users based on a query, and send connection \nrequests. The script uses image recognition to\n locate and interact with buttons on the LinkedIn\n website. The script provides a customizable\n number of connection requests to send", fg="#000000", font=("Arial", 12,"bold"), padx=10, pady=5)
text_overlay.config(width=355, height=250, image=bg_photo, compound="center")
text_overlay.place(x=37, y=78)

# Start the tkinter event loop
window.mainloop()
