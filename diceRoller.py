from tkinter import *
from tkinter.ttk import *
import random

root = Tk()

root.geometry("310x187")

def rollTwenty():
    newWindow1 = Toplevel(root)
    newWindow1.title("Roll d20")
    newWindow1.geometry("50x50")
    descText = Text(newWindow1, wrap=WORD)
    descText.insert(INSERT, random.randint(1, 20))
    descText.grid(row=0, column=5)


def rollTwelve():
    newWindow2 = Toplevel(root)
    newWindow2.title("Roll d12")
    newWindow2.geometry("50x50")
    descText = Text(newWindow2, wrap=WORD)
    descText.insert(INSERT, random.randint(1, 12))
    descText.grid(row=0, column=5)

def rollTen():
    newWindow3 = Toplevel(root)
    newWindow3.title("Roll d10")
    newWindow3.geometry("50x50")
    descText = Text(newWindow3, wrap=WORD)
    descText.insert(INSERT, random.randint(1, 10))
    descText.grid(row=0, column=5)

def rollEight():
    newWindow4 = Toplevel(root)
    newWindow4.title("Roll d8")
    newWindow4.geometry("50x50")
    descText = Text(newWindow4, wrap=WORD)
    descText.insert(INSERT, random.randint(1, 8))
    descText.grid(row=0, column=5)

def rollSix():
    newWindow5 = Toplevel(root)
    newWindow5.title("Roll d6")
    newWindow5.geometry("50x50")
    descText = Text(newWindow5, wrap=WORD)
    descText.insert(INSERT, random.randint(1, 6))
    descText.grid(row=0, column=5)

def rollFour():
    newWindow6 = Toplevel(root)
    newWindow6.title("Roll d4")
    newWindow6.geometry("50x50")
    descText = Text(newWindow6, wrap=WORD)
    descText.insert(INSERT, random.randint(1, 4))
    descText.grid(row=0, column=5)

def rollHundred():
    newWindow7 = Toplevel(root)
    newWindow7.title("Roll d100")
    newWindow7.geometry("50x50")
    descText = Text(newWindow7, wrap=WORD)
    descText.insert(INSERT, random.randint(1, 100))
    descText.grid(row=0, column=5)

def rollTwenty2():
    newWindow8 = Toplevel(root)
    newWindow8.title("Roll 2d20")
    newWindow8.geometry("50x50")
    descText = Text(newWindow8, wrap=WORD)
    descText.insert(INSERT, random.randint(2, 40))
    descText.grid(row=0, column=5)


def rollTwelve2():
    newWindow9 = Toplevel(root)
    newWindow9.title("Roll 2d12")
    newWindow9.geometry("50x50")
    descText = Text(newWindow9, wrap=WORD)
    descText.insert(INSERT, random.randint(2, 24))
    descText.grid(row=0, column=5)

def rollTen2():
    newWindow10 = Toplevel(root)
    newWindow10.title("Roll 2d10")
    newWindow10.geometry("50x50")
    descText = Text(newWindow10, wrap=WORD)
    descText.insert(INSERT, random.randint(2, 20))
    descText.grid(row=0, column=5)

def rollEight2():
    newWindow11 = Toplevel(root)
    newWindow11.title("Roll 2d8")
    newWindow11.geometry("50x50")
    descText = Text(newWindow11, wrap=WORD)
    descText.insert(INSERT, random.randint(2, 16))
    descText.grid(row=0, column=5)

def rollSix2():
    newWindow12 = Toplevel(root)
    newWindow12.title("Roll 2d6")
    newWindow12.geometry("50x50")
    descText = Text(newWindow12, wrap=WORD)
    descText.insert(INSERT, random.randint(2, 12))
    descText.grid(row=0, column=5)

def rollFour2():
    newWindow13 = Toplevel(root)
    newWindow13.title("Roll 2d4")
    newWindow13.geometry("50x50")
    descText = Text(newWindow13, wrap=WORD)
    descText.insert(INSERT, random.randint(2, 8))
    descText.grid(row=0, column=5)

def rollHundred2():
    newWindow14 = Toplevel(root)
    newWindow14.title("Roll 2d100")
    newWindow14.geometry("50x50")
    descText = Text(newWindow14, wrap=WORD)
    descText.insert(INSERT, random.randint(2, 200))
    descText.grid(row=0, column=5)

def rollTwenty3():
    newWindow15 = Toplevel(root)
    newWindow15.title("Roll 3d20")
    newWindow15.geometry("50x50")
    descText = Text(newWindow15, wrap=WORD)
    descText.insert(INSERT, random.randint(3, 60))
    descText.grid(row=0, column=5)


def rollTwelve3():
    newWindow16 = Toplevel(root)
    newWindow16.title("Roll 3d12")
    newWindow16.geometry("50x50")
    descText = Text(newWindow16, wrap=WORD)
    descText.insert(INSERT, random.randint(3, 36))
    descText.grid(row=0, column=5)

def rollTen3():
    newWindow17 = Toplevel(root)
    newWindow17.title("Roll 3d10")
    newWindow17.geometry("50x50")
    descText = Text(newWindow17, wrap=WORD)
    descText.insert(INSERT, random.randint(3, 30))
    descText.grid(row=0, column=5)

def rollEight3():
    newWindow18 = Toplevel(root)
    newWindow18.title("Roll 3d8")
    newWindow18.geometry("50x50")
    descText = Text(newWindow18, wrap=WORD)
    descText.insert(INSERT, random.randint(3, 24))
    descText.grid(row=0, column=5)

def rollSix3():
    newWindow19 = Toplevel(root)
    newWindow19.title("Roll 3d6")
    newWindow19.geometry("50x50")
    descText = Text(newWindow19, wrap=WORD)
    descText.insert(INSERT, random.randint(3, 18))
    descText.grid(row=0, column=5)

def rollFour3():
    newWindow20 = Toplevel(root)
    newWindow20.title("Roll 3d4")
    newWindow20.geometry("50x50")
    descText = Text(newWindow20, wrap=WORD)
    descText.insert(INSERT, random.randint(3, 12))
    descText.grid(row=0, column=5)

def rollHundred3():
    newWindow21 = Toplevel(root)
    newWindow21.title("Roll 3d100")
    newWindow21.geometry("50x50")
    descText = Text(newWindow21, wrap=WORD)
    descText.insert(INSERT, random.randint(3, 300))
    descText.grid(row=0, column=5)

def rollTwenty4():
    newWindow22 = Toplevel(root)
    newWindow22.title("Roll 4d20")
    newWindow22.geometry("50x50")
    descText = Text(newWindow22, wrap=WORD)
    descText.insert(INSERT, random.randint(4, 80))
    descText.grid(row=0, column=5)


def rollTwelve4():
    newWindow23 = Toplevel(root)
    newWindow23.title("Roll 4d12")
    newWindow23.geometry("50x50")
    descText = Text(newWindow23, wrap=WORD)
    descText.insert(INSERT, random.randint(4, 48))
    descText.grid(row=0, column=5)

def rollTen4():
    newWindow24 = Toplevel(root)
    newWindow24.title("Roll 3d10")
    newWindow24.geometry("50x50")
    descText = Text(newWindow24, wrap=WORD)
    descText.insert(INSERT, random.randint(4, 40))
    descText.grid(row=0, column=5)

def rollEight4():
    newWindow25 = Toplevel(root)
    newWindow25.title("Roll 3d8")
    newWindow25.geometry("50x50")
    descText = Text(newWindow25, wrap=WORD)
    descText.insert(INSERT, random.randint(4, 32))
    descText.grid(row=0, column=5)

def rollSix4():
    newWindow26 = Toplevel(root)
    newWindow26.title("Roll 3d6")
    newWindow26.geometry("50x50")
    descText = Text(newWindow26, wrap=WORD)
    descText.insert(INSERT, random.randint(4, 24))
    descText.grid(row=0, column=5)

def rollFour4():
    newWindow27 = Toplevel(root)
    newWindow27.title("Roll 3d4")
    newWindow27.geometry("50x50")
    descText = Text(newWindow27, wrap=WORD)
    descText.insert(INSERT, random.randint(4, 16))
    descText.grid(row=0, column=5)

def rollHundred4():
    newWindow28 = Toplevel(root)
    newWindow28.title("Roll 3d100")
    newWindow28.geometry("50x50")
    descText = Text(newWindow28, wrap=WORD)
    descText.insert(INSERT, random.randint(4, 400))
    descText.grid(row=0, column=5)

myButton1 = Button(root, text="Roll a d20!", command=rollTwenty)

myButton1.grid(row=1, column=0)

myButton2 = Button(root, text="Roll a d12!", command=rollTwelve)

myButton2.grid(row=10, column=0)

myButton3 = Button(root, text="Roll a d10", command=rollTen)

myButton3.grid(row=19, column=0)

myButton4 = Button(root, text="Roll a d8!", command=rollEight)

myButton4.grid(row=28, column=0)

myButton5 = Button(root, text="Roll a d6!", command=rollSix)

myButton5.grid(row=37, column=0)

myButton6 = Button(root, text="Roll a d4!", command=rollFour)

myButton6.grid(row=46, column=0)

myButton7 = Button(root, text="Roll a d100!", command=rollHundred)

myButton7.grid(row=55, column=0)

myButton8 = Button(root, text="Roll 2d20!", command=rollTwenty2)

myButton8.grid(row=1, column=1)

myButton9 = Button(root, text="Roll 2d12!", command=rollTwelve2)

myButton9.grid(row=10, column=1)

myButton10 = Button(root, text="Roll 2d10", command=rollTen2)

myButton10.grid(row=19, column=1)

myButton11 = Button(root, text="Roll 2d8!", command=rollEight2)

myButton11.grid(row=28, column=1)

myButton12 = Button(root, text="Roll 2d6!", command=rollSix2)

myButton12.grid(row=37, column=1)

myButton13 = Button(root, text="Roll 2d4!", command=rollFour2)

myButton13.grid(row=46, column=1)

myButton14 = Button(root, text="Roll 2d100!", command=rollHundred2)

myButton14.grid(row=55, column=1)

myButton15 = Button(root, text="Roll 3d20!", command=rollTwenty3)

myButton15.grid(row=1, column=2)

myButton16 = Button(root, text="Roll 3d12!", command=rollTwelve3)

myButton16.grid(row=10, column=2)

myButton17 = Button(root, text="Roll 3d10", command=rollTen3)

myButton17.grid(row=19, column=2)

myButton18 = Button(root, text="Roll 3d8!", command=rollEight3)

myButton18.grid(row=28, column=2)

myButton19 = Button(root, text="Roll 3d6!", command=rollSix3)

myButton19.grid(row=37, column=2)

myButton20 = Button(root, text="Roll 3d4!", command=rollFour3)

myButton20.grid(row=46, column=2)

myButton21 = Button(root, text="Roll 3d100!", command=rollHundred3)

myButton21.grid(row=55, column=2)

myButton22 = Button(root, text="Roll 4d20!", command=rollTwenty4)

myButton22.grid(row=1, column=3)

myButton23 = Button(root, text="Roll 4d12!", command=rollTwelve4)

myButton23.grid(row=10, column=3)

myButton24 = Button(root, text="Roll 4d10", command=rollTen4)

myButton24.grid(row=19, column=3)

myButton25 = Button(root, text="Roll 4d8!", command=rollEight4)

myButton25.grid(row=28, column=3)

myButton26 = Button(root, text="Roll 4d6!", command=rollSix4)

myButton26.grid(row=37, column=3)

myButton27 = Button(root, text="Roll 4d4!", command=rollFour4)

myButton27.grid(row=46, column=3)

myButton28 = Button(root, text="Roll 4d100!", command=rollHundred4)

myButton28.grid(row=55, column=3)


root.mainloop()