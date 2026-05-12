import os
import subprocess
import tkinter as tk
from tkinter import messagebox

randomNum = r'randomNum.txt'
genNum = r'NewSetOfNum.py'
showNum = r'ShowNum.py'
aritNum = r'AritMean.py'
harmNum = r'HarmMean.py'
geoNum = r'GeoMean.py'
devNum = r'StdDev.py'
modeNum = r'Mode.py'
rangeNum = r'Range.py'
medianNum = r'Median.py'

def createNumber():
    count = entry.get()
    if count.strip().isdigit():
        subprocess.run(['python', genNum, count])
        entry.delete(0, tk.END)
    else:
        messagebox.showerror("Błąd", "Wprowadź prawidłową liczbę całkowitą dodatnią.")

def showNumber():
    subprocess.run(['python', showNum])
    
def calcArit():
    subprocess.run(['python', aritNum])

def calcHarm():
    subprocess.run(['python', harmNum])
    
def calcGeo():
    subprocess.run(['python', geoNum])
    
def calcDev():
    subprocess.run(['python', devNum])
    
def calcMode():
    subprocess.run(['python', modeNum])
    
def calcRange():
    subprocess.run(['python', rangeNum])

def calcMedian():
    subprocess.run(['python', medianNum])
        
def exitDelete():
    if os.path.exists(randomNum):
        os.remove(randomNum)
        
    root.quit()

root = tk.Tk()
root.title("Menu")

entry_label = tk.Label(root, text="Ilość liczb do wygenerowania:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Generuj Losowy zbiór liczb", command=createNumber)
button.pack()

button = tk.Button(root, text="Pokaż wygenerowane liczby", command=showNumber)
button.pack()

button = tk.Button(root, text="Oblicz Średnią Arytmetyczną", command=calcArit)
button.pack()

button = tk.Button(root, text="Oblicz Średnią Harmoniczną", command=calcHarm)
button.pack()

button = tk.Button(root, text="Oblicz Średnią Geometryczną", command=calcGeo)
button.pack()

button = tk.Button(root, text="Oblicz Odchylenie Standardowe", command=calcDev)
button.pack()

button = tk.Button(root, text="Oblicz Mode (Miara położenia)", command=calcMode)
button.pack()

button = tk.Button(root, text="Oblicz Rozstęp", command=calcRange)
button.pack()

button = tk.Button(root, text="Oblicz Medianę", command=calcMedian)
button.pack()

button = tk.Button(root, text="Exit", command=exitDelete)
button.pack()

root.mainloop()