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

def calcMean(numbers):

    if not numbers:
        return None

    log_sum = sum(math.log(num) for num in numbers)
    geometric_mean = math.exp(log_sum / len(numbers))
    
    return geometric_mean

def showNumWin(mean):

    window = tk.Tk()
    window.title("Średnia Geometryczna")

    mean_label = tk.Label(window, text=f"Średnia Geometryczna: {mean:.2f}")
    mean_label.pack()

    window.mainloop()

file_path = 'randomNum.txt'
    
numbers = readNum(file_path)
    
mean = calcMean(numbers)
    
showNumWin(mean)
