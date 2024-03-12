from tkinter import *
from tkinter import ttk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List')
        self.root.geometry('650x410+300+150')
        
        # Labels
        self.label = Label(self.root, text='To-Do List App',
                           font='Arial 25 bold', width=10, bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=BOTH)
        
        self.label2 = Label(self.root, text='Add Task',
                            font='Arial 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label2.place(x=40, y=54)
        
        self.label3 = Label(self.root, text='Tasks',
                            font='Arial 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)
        
        # Listbox and Text Entry
        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="Arial 20 italic bold")
        self.main_text.place(x=280, y=100)
        
        self.text = Text(self.root, bd=5, height=2, width=30, font='Arial 10 bold')
        self.text.place(x=20, y=120)
        
        # Buttons
        self.button = Button(self.root, text="Add", font='Arial 20 bold italic', 
                             width=10, bd=5, bg='orange', fg='black', command=self.add_task) 
        self.button.place(x=30, y=180)
                                    
        self.button2 = Button(self.root, text="Delete", font='Arial 20 bold italic', 
                              width=10, bd=5, bg='orange', fg='black', command=self.delete_task) 
        self.button2.place(x=30, y=280)
        
        # Load tasks from file
        self.load_tasks_from_file()
    
    def add_task(self):
        """Add a task to the list and save to file."""
        content = self.text.get(1.0, END)
        self.main_text.insert(END, content)
        with open('data.txt', 'a') as file:
            file.write(content)
        self.text.delete(1.0, END)
    
    def delete_task(self):
        """Delete selected task from the list and update file."""
        selected_index = self.main_text.curselection()
        if selected_index:
            self.main_text.delete(selected_index)
            with open('data.txt', 'r+') as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    if line.strip() != self.main_text.get(selected_index):
                        f.write(line)
                f.truncate()

    def load_tasks_from_file(self):
        """Load tasks from file and populate the list."""
        try:
            with open('data.txt', 'r') as file:
                tasks = file.readlines()
                for task in tasks:
                    self.main_text.insert(END, task.strip())
        except FileNotFoundError:
            # If file doesn't exist, create it
            open('data.txt', 'w')

def main():
    root = Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":  
    main()
