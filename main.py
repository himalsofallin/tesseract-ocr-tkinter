import tkinter as tk
from tkinter import filedialog
import os,pytesseract
from PIL import Image
localappdata_path = os.getenv("PROGRAMFILES")

if not os.path.exists(localappdata_path + r"\Tesseract-OCR\tesseract.exe"):
    print("Tesseract not found, please download and install it and check @himalsofallin README.md for more info")
    exit()

pytesseract.pytesseract.tesseract_cmd = localappdata_path + r"\Tesseract-OCR\tesseract.exe"


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(filetypes=[("Image Files", ".png .jpg")])

if file_path == "":
    print("No file selected")
elif file_path.endswith(".png") or file_path.endswith(".jpg"):
    #create new tkinter dialog window and write text to it
    text_window = tk.Tk()
    text_window.title("Text from image")
    text_window.geometry("1200x700")
    text_window.configure(background="white")
    text_window.resizable(False, False)
    text_window.attributes("-topmost", True)
    text_window.attributes("-toolwindow", True)
    text_window.attributes("-topmost", False)
    
    #read image with tesseract
    text = pytesseract.image_to_string(Image.open(file_path))
    if text == "":
        text = "No text found"

    #create text widget and insert text
    text_widget = tk.Text(text_window, height=500, width=500, bg="white", fg="black")
    text_widget.insert(tk.END, text)
    text_widget.pack()

    #create close button and completely quit
    close_button = tk.Button(text_window, text="Close", command=text_window.destroy)
    close_button.pack()

    text_window.mainloop()
else:
    print("File type not supported")