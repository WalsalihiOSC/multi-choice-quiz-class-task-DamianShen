from tkinter import *

class MultiChoice:
    def __init__(self, parent):
        self.answer = StringVar()
        self.answer.set("")

        self.question_label = Label(parent, text = "Question: Who is the prime minister of NZ?")
        self.question_label.grid(column = 0, row = 0)
        
        f1 = Frame(parent)
        f1.grid(column = 0, row = 1)

        answer_list = ["Jacinda Adern", "Bill English", "John Key", "Helen Clark"]
        
        z = 0
        for x in(answer_list):
            Radiobutton(f1, text = x, value = x, variable = self.answer).grid(row = z, sticky = W)
            z += 1

if __name__ == "__main__":
    root = Tk()
    buttons = MultiChoice(root)
    root.title("Multi Choice Quiz")
    root.mainloop()
