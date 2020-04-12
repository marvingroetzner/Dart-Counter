import tkinter as tk

root = tk.Tk()

# mach mal 800*900
canvas = tk.Canvas(root, height=300, width=300)
canvas.pack()

gamescore = 301
multiplier = 1


# Function Subtraktion: Button gibt seinen eigenen Wert zurück und zieht ihn von der Startsumme (301/501/701) ab
def subtraktion(buttonValue):
    global gamescore

    if gamescore > 0:

        if buttonValue <=20:

            multpValue = buttonValue * multiplier
            print("ButtonValue = ", multpValue)
            gamescore = gamescore - multpValue
            print("Gamescore = ", gamescore)

        elif buttonValue == 25:
            if multiplier == 1:
                multpValue = buttonValue * multiplier
                print("ButtonValue = ", multpValue)
                gamescore = gamescore - multpValue
                print("Gamescore = ", gamescore)
            elif multiplier == 2:
                multpValue = buttonValue * multiplier
                print("ButtonValue = ", multpValue)
                gamescore = gamescore - multpValue
                print("Gamescore = ", gamescore)
            elif multiplier == 3:
                print("Du kannst keine Triple 25 werfen!")


    # elif gamescore < 0:
    #     #undothe last

# Function labelaktualisieren: Nach gedrücktem Button aktualisiert sich das Label und zeigt aktuellen Score
def labelaktualisieren():

    LabelScore.config(text=gamescore)



def doubletriple(buttonID):
    global multiplier

    if buttonID == 1:
        multiplier = 1
        print("single")

    elif buttonID == 2:
        multiplier = 2
        print("double")

    else:
        multiplier = 3
        print("triple")




LabelScore = tk.Label(canvas, text=gamescore, bg="gray")
LabelScore.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)

frame = tk.Frame(root, bg="#6da2f7")
frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.7)

button1 = tk.Button(frame, text="1", bg="gray", command=lambda: [subtraktion(1), labelaktualisieren(), doubletriple(1)])
button1.place(relx=0, rely=0.1, relwidth=0.1, relheight=0.1)
button2 = tk.Button(frame, text="2", bg="gray", command=lambda: [subtraktion(2), labelaktualisieren(), doubletriple(1)])
button2.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.1)
button3 = tk.Button(frame, text="3", bg="gray", command=lambda: [subtraktion(3), labelaktualisieren(), doubletriple(1)])
button3.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.1)
button4 = tk.Button(frame, text="4", bg="gray", command=lambda: [subtraktion(4), labelaktualisieren(), doubletriple(1)])
button4.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.1)
button5 = tk.Button(frame, text="5", bg="gray", command=lambda: [subtraktion(5), labelaktualisieren(), doubletriple(1)])
button5.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.1)
button6 = tk.Button(frame, text="6", bg="gray", command=lambda: [subtraktion(6), labelaktualisieren(), doubletriple(1)])
button6.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.1)
button7 = tk.Button(frame, text="7", bg="gray", command=lambda: [subtraktion(7), labelaktualisieren(), doubletriple(1)])
button7.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.1)
button8 = tk.Button(frame, text="8", bg="gray", command=lambda: [subtraktion(8), labelaktualisieren(), doubletriple(1)])
button8.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.1)
button9 = tk.Button(frame, text="9", bg="gray", command=lambda: [subtraktion(9), labelaktualisieren(), doubletriple(1)])
button9.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.1)
button10 = tk.Button(frame, text="10", bg="gray", command=lambda: [subtraktion(10), labelaktualisieren(), doubletriple(1)])
button10.place(relx=0.9, rely=0.1, relwidth=0.1, relheight=0.1)
button11 = tk.Button(frame, text="11", bg="gray", command=lambda: [subtraktion(11), labelaktualisieren(), doubletriple(1)])
button11.place(relx=0, rely=0.2, relwidth=0.1, relheight=0.1)
button12 = tk.Button(frame, text="12", bg="gray", command=lambda: [subtraktion(12), labelaktualisieren(), doubletriple(1)])
button12.place(relx=0.1, rely=0.2, relwidth=0.1, relheight=0.1)
button13 = tk.Button(frame, text="13", bg="gray", command=lambda: [subtraktion(13), labelaktualisieren(), doubletriple(1)])
button13.place(relx=0.2, rely=0.2, relwidth=0.1, relheight=0.1)
button14 = tk.Button(frame, text="14", bg="gray", command=lambda: [subtraktion(14), labelaktualisieren(), doubletriple(1)])
button14.place(relx=0.3, rely=0.2, relwidth=0.1, relheight=0.1)
button15 = tk.Button(frame, text="15", bg="gray", command=lambda: [subtraktion(15), labelaktualisieren(), doubletriple(1)])
button15.place(relx=0.4, rely=0.2, relwidth=0.1, relheight=0.1)
button16 = tk.Button(frame, text="16", bg="gray", command=lambda: [subtraktion(16), labelaktualisieren(), doubletriple(1)])
button16.place(relx=0.5, rely=0.2, relwidth=0.1, relheight=0.1)
button17 = tk.Button(frame, text="17", bg="gray", command=lambda: [subtraktion(17), labelaktualisieren(), doubletriple(1)])
button17.place(relx=0.6, rely=0.2, relwidth=0.1, relheight=0.1)
button18 = tk.Button(frame, text="18", bg="gray", command=lambda: [subtraktion(18), labelaktualisieren(), doubletriple(1)])
button18.place(relx=0.7, rely=0.2, relwidth=0.1, relheight=0.1)
button19 = tk.Button(frame, text="19", bg="gray", command=lambda: [subtraktion(19), labelaktualisieren(), doubletriple(1)])
button19.place(relx=0.8, rely=0.2, relwidth=0.1, relheight=0.1)
button20 = tk.Button(frame, text="20", bg="gray", command=lambda: [subtraktion(20), labelaktualisieren(), doubletriple(1)])
button20.place(relx=0.9, rely=0.2, relwidth=0.1, relheight=0.1)
button25 = tk.Button(frame, text="25", bg="gray", command=lambda: [subtraktion(25), labelaktualisieren(), doubletriple(1)])
button25.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.1)
buttonDouble = tk.Button(frame, text="Double", bg="gray", command=lambda: doubletriple(2))
buttonDouble.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.1)
buttonTriple = tk.Button(frame, text="Triple", bg="gray", command=lambda: doubletriple(3))
buttonTriple.place(relx=0.6, rely=0.3, relwidth=0.2, relheight=0.1)
# buttonBack = tk.Button(frame, text="Back", bg="gray")
# buttonBack.place(relx=0.7, rely=0.3, relwidth=0.2, relheight=0.1)


root.mainloop()



