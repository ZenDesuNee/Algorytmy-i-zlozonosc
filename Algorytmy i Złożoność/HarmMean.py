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
    n = len(numbers)

    reciprocal_sum = sum(1 / num for num in numbers)
    harmonic_mean = n / reciprocal_sum
    
    return harmonic_mean

def showNumWin(mean):

    window = tk.Tk()
    window.title("Średnia Harmoniczna")

    mean_label = tk.Label(window, text=f"Średnia Harmoniczna: {mean:.2f}")
    mean_label.pack()

    window.mainloop()

file_path = 'randomNum.txt'
    
numbers = readNum(file_path)
    
mean = calcMean(numbers)

showNumWin(mean)
