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

def calcRange(numbers):
    if not numbers:
        return None
    
    minimum = min(numbers)
    maksimum = max(numbers)
    
    range_value = maksimum - minimum
    
    return range_value

def showNumWin(range_value):

    window = tk.Tk()
    window.title("Rozstęp")

    range_label = tk.Label(window, text=f"Rozstęp: {range_value}")
    range_label.pack()

    window.mainloop()

file_path = 'randomNum.txt'
    
numbers = readNum(file_path)
    
range_value = calcRange(numbers)

showNumWin(range_value)
    