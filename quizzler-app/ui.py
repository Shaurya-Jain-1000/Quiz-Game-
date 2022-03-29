from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizz')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        self.score_label = Label(text=f'Score: {self.score}', fg='white', bg=THEME_COLOR, font=(40))
        self.score_label.grid(row=0, column=1)


        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text="my Question", fill=THEME_COLOR, font=('Arial',20,'italic'), width=280 )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.tick_img = PhotoImage(file='images/true.png')
        self.cross_img = PhotoImage(file='images/false.png')

        self.tick_button = Button(image=self.tick_img, command=self.pressed_true)
        self.tick_button.grid(row=2, column=0)

        self.cross_button = Button(image=self.cross_img, command=self.pressed_false)
        self.cross_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text=f'You have reached to the end of the quiz\nYour Score Was:{self.score}')

            self.tick_button.config(state='disabled')
            self.cross_button.config(state='disabled')

    def pressed_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def pressed_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.score+=1
            self.score_label.config(text=f'Score: {self.score}')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)



















