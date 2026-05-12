import random
import sys
import tkinter as tk

def genRanNum(count):
    try:
        count = int(count)
        if not 1 <= count <= 100:
            return []
    except ValueError:
        return []

    random_numbers = [random.randint(1, 100) for _ in range(count)]

    with open("randomNum.txt", "w") as file:
        file.write("\n".join(map(str, random_numbers)))
        
    showNumWin(random_numbers)

def showNumWin(numbers):
    
    window = tk.Tk()
    window.title("Wygenerowane liczby")
    
    text_area = tk.Text(window, wrap=tk.WORD, width=40, height=10)
    text_area.pack()

    numbers_string = ", ".join(map(str, numbers))

    text_area.insert(tk.END, numbers_string)
    
    window.mainloop()


if len(sys.argv) > 1:
    count = sys.argv[1]
    genRanNum(count)
else:
    print("Nie podano ilości liczb do wygenerowania.")
