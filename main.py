import tkinter as tk
import jsonwr

colors = ["#033540", "#015366", "#63898C", "#A7D1D2", "#E0F4F5"]


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.WINSIZE = (360, 640)
        self.title("EDiary")
        self.geometry(f"{self.WINSIZE[0]}x{self.WINSIZE[1]}")
        self.minsize(self.WINSIZE[0], self.WINSIZE[1])
        self.configure(bg=colors[0])

        self.tasks = jsonwr.read("save.json")
        self.tasks_num = 0

        self.title = tk.Label(text="EDiary",
                              fg=colors[4],
                              bg=colors[0],
                              font=("Arial", 30, "bold"))
        self.title.pack(side=tk.TOP, pady=5)

        self.tasks_frame = tk.Frame(bg=colors[1])
        self.tasks_frame.pack(fill=tk.BOTH, expand=True)

        self.add_task = tk.Button(text="+",
                                  font=("Arial", 25, "bold"),
                                  fg=colors[4],
                                  bg=colors[0],
                                  borderwidth=0,
                                  activebackground=colors[2],
                                  command=self.open_create_window)
        self.add_task.place(relx=0.9, rely=0.93, anchor="center")

        self.reset_btn = tk.Button(self,
                                   text="R",
                                   borderwidth=0,
                                   bg=colors[1],
                                   fg=colors[4],
                                   font=("Arial", 12, "bold"),
                                   command=self.reset_app)
        self.reset_btn.place(anchor=tk.NW, relx=0, rely=0)

        self.load_app()

    def open_create_window(self):

        def close():
            create_frame.place_forget()

        if self.tasks_num < 8:
            create_frame = tk.Frame(self,
                                    bg=colors[2],
                                    highlightthickness=2,
                                    highlightbackground=colors[0],
                                    highlightcolor=colors[0])
            create_frame.place(relx=0.5, rely=0.5, anchor="center")

            tk.Label(create_frame, text="Subject", bg=colors[2], fg=colors[0],
                     font=("Arial", 20, "bold")).pack(pady=5, padx=20)

            subject_name = tk.Entry(create_frame,
                                    bg=colors[1],
                                    fg=colors[3],
                                    justify="center",
                                    font=("Arial", 11),
                                    borderwidth=0)
            subject_name.pack(fill=tk.X, padx=15)

            parag_frame = tk.Frame(create_frame, bg=colors[2])
            parag_frame.pack(pady=5, padx=15, fill=tk.X)

            p_sym = tk.Label(parag_frame,
                             text="§",
                             bg=colors[2],
                             fg=colors[0],
                             font=("Arial", 12, "bold"),
                             anchor="center")
            p_sym.pack(side=tk.LEFT)

            parag_entry = tk.Entry(parag_frame,
                                   bg=colors[1],
                                   fg=colors[3],
                                   borderwidth=0)
            parag_entry.pack(side=tk.RIGHT, expand=True)

            nums_frame = tk.Frame(create_frame, bg=colors[2])
            nums_frame.pack(fill=tk.X, padx=15)

            n_sym = tk.Label(nums_frame,
                             text="№",
                             bg=colors[2],
                             fg=colors[0],
                             font=("Arial", 12, "bold"),
                             anchor="center")
            n_sym.pack(side=tk.LEFT)

            nums_entry = tk.Entry(nums_frame, borderwidth=0, bg=colors[1], fg=colors[3])
            nums_entry.pack(side=tk.RIGHT, expand=True)

            create_btn = tk.Button(create_frame,
                                   text="Create",
                                   bg=colors[0],
                                   activebackground=colors[3],
                                   fg=colors[4],
                                   font=("Arial", 10, "bold"),
                                   borderwidth=0,
                                   command=lambda: (close(), self.create_task(subject_name.get(), parag_entry.get(),
                                                                              nums_entry.get())))
            create_btn.pack(pady=5)

    def create_task(self, subject, parags, nums):
        self.tasks[subject] = [parags, nums]
        jsonwr.write(self.tasks, "save.json")
        if self.tasks_num <= 8 and subject != "":
            self.tasks_num += 1
            task_frame = tk.Frame(self.tasks_frame, bg=colors[2])
            task_frame.pack(fill=tk.X, pady=5, padx=5)

            task_name = tk.Label(task_frame,
                                 text=subject,
                                 bg=colors[2],
                                 fg=colors[0],
                                 font=("Arial", 15, "bold"))
            task_name.pack()

            tasks_frame = tk.Frame(task_frame, bg=colors[2])
            tasks_frame.pack(fill=tk.X)

            p_sym = tk.Label(tasks_frame,
                             text="§ ",
                             bg=colors[2],
                             fg=colors[0],
                             font=("Arial", 12, "bold"))
            p_sym.pack(side=tk.LEFT)

            paragrs = tk.Label(tasks_frame,
                               text=parags,
                               bg=colors[2],
                               fg=colors[0],
                               font=("Arial", 12))
            paragrs.pack(side=tk.LEFT)

            n_sym = tk.Label(tasks_frame,
                             text="№ ",
                             bg=colors[2],
                             fg=colors[0],
                             font=("Arial", 12, "bold"))
            n_sym.pack(side=tk.LEFT)

            nums = tk.Label(tasks_frame,
                            text=nums,
                            bg=colors[2],
                            fg=colors[0],
                            font=("Arial", 12))
            nums.pack(side=tk.LEFT)

    def load_app(self):
        for task in self.tasks:
            self.create_task(task, self.tasks[task][0], self.tasks[task][1])

    def reset_app(self):
        for t in self.tasks_frame.winfo_children():
            t.destroy()
        self.tasks = {}
        self.tasks_num = 0
        jsonwr.write({}, "save.json")


if __name__ == "__main__":
    app = App()
    app.mainloop()
