import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
counter = None
checks = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps,checks
    window.after_cancel(counter)
    reps = 0
    checks=""
    check_label.config(text="")
    label.config(text="Timer",fg="white")
    canvas.itemconfig(timer_label,text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    print(reps)
    if reps%7 == 7:
        time = LONG_BREAK_MIN
        label.config(text="Long Brake", fg=RED)
    elif reps%2==0:
        time = WORK_MIN
        label.config(text="Working Time", fg=YELLOW)
    else:
        time = SHORT_BREAK_MIN
        label.config(text="Short Brake",fg=PINK)
    timer_countdown(time * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timer_countdown(count):
    global reps,checks,counter
    canvas.itemconfig(timer_label,text=f"{count//60}:{count%60}")
    if count > 0:
        counter = window.after(1000, timer_countdown,count-1)
        if count%60 < 10:
            canvas.itemconfig(timer_label, text=f"{count // 60}:0{count%60}")
    else:
        reps+=1
        if reps%2 == 1:
            checks += "✔"
            check_label.config(text=checks)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=103,pady=50,bg=GREEN)


label = tkinter.Label(text="Timer",fg="white",font=(FONT_NAME,35,"bold"),bg=GREEN)
label.grid(column=1,row=0)

check_label = tkinter.Label(font=(FONT_NAME,20,"bold"),bg=GREEN)
check_label.grid(column=1,row=3)

buttoon_start = tkinter.Button(text="Start",command=start_timer)
buttoon_start.grid(column=0,row=2)

buttoon_reset = tkinter.Button(text="Restart",command=reset)
buttoon_reset.grid(column=2,row=2)

canvas = tkinter.Canvas(width=200,height=224,bg=GREEN,highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
canvas.grid(column=1,row=1)
timer_label = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))



window.mainloop()