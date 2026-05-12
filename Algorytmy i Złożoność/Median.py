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

def calcMedian(numbers):
    if not numbers:
        return None
    
    numbers.sort()
    
    n = len(numbers)
    if n % 2 == 1:
        median = numbers[n // 2]
        return median
    
    else:
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        return mid1, mid2

def showNumWin(median):

    window = tk.Tk()
    window.title("Mediana")

    if isinstance(median, tuple):
        median_label = tk.Label(window, text=f"Mediana: {median[0]}, {median[1]}")
    else:
        median_label = tk.Label(window, text=f"Mediana: {median}")

    median_label.pack()

    window.mainloop()


file_path = 'randomNum.txt'
    
numbers = readNum(file_path)
    
median = calcMedian(numbers)

showNumWin(median)
