print("tran minh duc")
import tkinter as tk
import random

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
random.shuffle(colours) 
score = 0
timeleft = 120


def nextColour():
    """Kiểm tra đáp án, cập nhật điểm và hiển thị màu mới."""
    global score, timeleft
    
    if timeleft > 0:
        if e.get().lower() == colours[0].lower():
            score += 2
        elif e.get() != "":
            score -= 1

        e.delete(0, tk.END) 
        random.shuffle(colours) 
        
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))

def countdown():
    """Hàm đếm ngược thời gian."""
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)

def startGame(event):
    """Bắt đầu trò chơi."""
    global timeleft
    if timeleft == 120:
        countdown()
        nextColour()

root = tk.Tk()
root.title("COLORGAME")
root.geometry("375x200")

instructions = tk.Label(root, text="Type in the colour of the words, and not the word text!", font=('Helvetica', 12))
instructions.pack()

scoreLabel = tk.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tk.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

label = tk.Label(root, font=('Helvetica', 60))
label.pack()

e = tk.Entry(root)
root.bind('<Return>', startGame)
e.pack()

e.focus_set()

root.mainloop()
