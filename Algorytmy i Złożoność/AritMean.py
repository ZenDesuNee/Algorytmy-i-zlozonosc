import tkinter as tk

def readNum(file_path):
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.isdigit():
                    numbers.append(int(line))
                else:
                    print(f"Ignorując nieważną linię: {line}")
        return numbers
    except Exception as e:
        print(f"Wystąpił błąd podczas odczytywania pliku: {e}")
        return []

def calcMean(numbers):
    
    if not numbers:
        return None
    
    return sum(numbers) / len(numbers)

def showNumWin(mean):
    
    window = tk.Tk()
    window.title("Średnia Arytmetyczna")

    mean_label = tk.Label(window, text=f"Średnia arytmetyczna: {mean:.2f}")
    mean_label.pack()

    window.mainloop()
    
file_path = 'randomNum.txt'

numbers = readNum(file_path)
    
mean = calcMean(numbers)
    
showNumWin(mean)

    

