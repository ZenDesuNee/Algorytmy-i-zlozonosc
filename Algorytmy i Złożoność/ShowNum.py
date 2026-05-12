import tkinter as tk
from tkinter import scrolledtext

def readNum(file_path):
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.isdigit():
                    numbers.append(int(line))
                else:
                    print(f"Ignoring invalid line: {line}")
        return numbers
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def showNumWin(numbers):
    
    window = tk.Tk()
    window.title("Wygenerowane liczby")

    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
    text_area.pack()

    numbers_string = ", ".join(map(str, numbers))

    text_area.insert(tk.END, numbers_string)

    window.mainloop()


file_path = 'randomNum.txt'

numbers = readNum(file_path)

showNumWin(numbers)