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

def calcVariance(numbers):
    if not numbers:
        return None
    
    mean = sum(numbers) / len(numbers)
    
    sum_of_squares = sum((num - mean) ** 2 for num in numbers)
    
    variance = sum_of_squares / len(numbers)
    
    return variance

def showNumWin(variance):

    window = tk.Tk()
    window.title("Wariancja")

    variance_label = tk.Label(window, text=f"Wariancja: {variance:.2f}")
    variance_label.pack()

    window.mainloop()


file_path = 'randomNum.txt'
    
numbers = readNum(file_path)
    
variance = calcVariance(numbers)
    
showNumWin(variance)
