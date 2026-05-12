import tkinter as tk
from collections import Counter

def readNum(file_path):
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                try:
                    number = int(line)
                    numbers.append(number)
                except ValueError:
                    print(f"Ignorując nieważną linię: {line}")
        return numbers
    except Exception as e:
        print(f"Wystąpił błąd podczas odczytywania pliku: {e}")
        return []

def calcMode(numbers):
    if not numbers:
        return None
    
    number_counts = Counter(numbers)
    
    max_count = max(number_counts.values())
    
    mode = [num for num, count in number_counts.items() if count == max_count]
    
    return mode

def showNumWin(mode):
    
    window = tk.Tk()
    window.title("Moda")

    mode_label = tk.Label(window, text=f"Moda: {', '.join(map(str, mode))}")
    mode_label.pack()

    window.mainloop()

file_path = 'randomNum.txt'
    
numbers = readNum(file_path)
    
mode = calcMode(numbers)
    
showNumWin(mode)
