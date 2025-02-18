import tkinter as tk

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
        
        self.label = tk.Label(master, text="Pomodoro Timer", font=("Arial", 24))
        self.label.pack(pady=10)
        
        self.time_display = tk.Label(master, text="", font=("Arial", 48))
        self.time_display.pack(pady=20)
        
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=20)
        
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=20)
        
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=20)
        
        self.running = False
        self.time_left = 1500  # 25 minutes
    
    def update_display(self):
        mins, secs = divmod(self.time_left, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        self.time_display.config(text=time_format)
    
    def start_timer(self):
        if not self.running:
            self.running = True
            self.countdown()
    
    def stop_timer(self):
        self.running = False
    
    def reset_timer(self):
        self.time_left = 1500
        self.update_display()
    
    def countdown(self):
        if self.running and self.time_left > 0:
            self.update_display()
            self.master.after(1000, self.countdown)
            self.time_left -= 1
        else:
            self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    pomodoro_timer = PomodoroTimer(root)
    root.mainloop()
