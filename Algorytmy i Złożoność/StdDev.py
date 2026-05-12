import math
import tkinter as tk

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

def calcDeviation(numbers):
    if not numbers:
        return None
    
    mean = sum(numbers) / len(numbers)
    
    variance = sum((num - mean) ** 2 for num in numbers) / len(numbers)
    
    standard_deviation = math.sqrt(variance)
    
    return standard_deviation

def showNumWin(std_dev):
    
    window = tk.Tk()
    window.title("Odchylenie Standardowe")

    std_dev_label = tk.Label(window, text=f"Odchylenie Standardowe: {std_dev:.2f}")
    std_dev_label.pack()

    window.mainloop()

file_path = 'randomNum.txt'
    
numbers = readNum(file_path)
    
std_dev = calcDeviation(numbers)

showNumWin(std_dev)
    