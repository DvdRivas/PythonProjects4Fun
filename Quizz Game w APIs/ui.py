import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial",20,"italic")

class UI:
    def __init__(self,quiz:QuizBrain):
        self.quiz = quiz
        self.window = tkinter.Tk()
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)
        self.window.title("Quizzler")
        self.canvas = tkinter.Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.grid(columnspan=2, column=0, row=1, pady=40)
        self.category = tkinter.Label(text="",bg=THEME_COLOR,fg="white",font=("Arial",12,"bold"))
        self.category.grid(column=0,row=0)
        self.score = 0
        self.PrintScore()
        true = tkinter.PhotoImage(file="images/true.png")
        false = tkinter.PhotoImage(file="images/false.png")
        self.true_button = tkinter.Button(image=true,pady=20,padx=20,command=self.check_true)
        self.true_button.grid(column=0,row=2)
        self.false_button = tkinter.Button(image=false,pady=20,padx=20,command=self.check_false)
        self.false_button.grid(column=1, row=2)
        self.text = self.canvas.create_text(150, 125, text="Question", font=FONT,width=280)
        self.Text()
        self.window.mainloop()


    def Text(self):
        self.canvas.config(bg="white")
        self.PrintScore()
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.text, text=self.quiz.next_question())
            self.category["text"] = self.quiz.get_category()
        else:
            self.canvas.itemconfig(self.text, text="You've completed the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def PrintScore(self):

        self.label_score = tkinter.Label(text=f"Score {self.score}/{self.quiz.question_number}",bg=THEME_COLOR,fg="white",font=("Arial",14,"bold"))
        self.label_score.grid(column=1,row=0)

    def UpdateScore(self):
        self.canvas.config(bg="green")
        self.score += 1

    def check_false(self):
        if self.quiz.get_answer() == "False":
            self.UpdateScore()
        else:
            self.canvas.config(bg="red")
        self.end()

    def check_true(self):
        if self.quiz.get_answer() == "True":
            self.UpdateScore()
        else:
            self.canvas.config(bg="red")
        self.end()
    def end(self):
        self.window.after(1000,self.Text)