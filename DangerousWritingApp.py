import tkinter as tk
import time

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Dangerous Writing App")
        self.root.geometry("800x600")

        # HINT: You need to track when the user last typed something.
        # What data type would you use to store a point in time?
        self.last_keystroke_time = None # ← fill this in properly
        self.timer_running = False
        self.DANGER_SECONDS = 5  # seconds before deletion

        self._build_ui()

    def reset(self):
        self.text_area.delete("1.0", tk.END)
        self.status_label.config(text="Start typing...", fg="gray")
        self.timer_running = False
        self.last_keystroke_time = None
        self.button.pack_forget()

    def _build_ui(self):
        # Top bar — shows countdown
        self.status_label = tk.Label(
            self.root, text="Start typing...",
            font=("Helvetica", 18), fg="black",background="pink"
        )
        self.status_label.pack(pady=10)

        # Main text area
        self.text_area = tk.Text(
            self.root, font=("Helvetica", 18),
            wrap=tk.WORD, padx=10, pady=10
        )
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # HINT: Bind a method to the text area so it fires every time
        # the user types a key. Look up: widget.bind("<Key>", ...)
        self.text_area.bind("<Key>", self.on_keypress)

        self.button = tk.Button(self.root,fg="red",bg="white",text="try again!",width=30,height=10,command=self.reset)
        self.button.pack(pady=5)
        self.button.pack_forget()
    def on_keypress(self, event=None):
        self.last_keystroke_time=time.time()
        # Then, if the timer isn't running yet, start it.
        if not self.timer_running:
            self.start_timer()

    def start_timer(self):
        self.timer_running = True
        self.check_inactivity()

    def check_inactivity(self):
        if self.last_keystroke_time is not None:
            elapsed = time.time() - self.last_keystroke_time
            seconds_left = self.DANGER_SECONDS - elapsed

            if seconds_left <= 0:
                 self.delete_all_text()
            else:
                self.update_status_label(seconds_left)
                self.root.after(100, self.check_inactivity)  # check again in 100ms

    def delete_all_text(self):
        # HINT: To delete everything in a Text widget:
        self.text_area.delete("1.0", tk.END)
        self.status_label.config(text="You Failed",fg="red",bg="white")
        self.timer_running=False
        self.last_keystroke_time=None
        self.button.pack(pady=5)

    def update_status_label(self, seconds_left):

        if seconds_left > 3:
            self.text_area.config(fg="white")
        elif seconds_left > 1.5:
            self.text_area.config( fg="yellow")
        else:
            self.text_area.config(fg="red")



if __name__ == "__main__":
    root = tk.Tk()
    root.config(background="pink")
    app = DangerousWritingApp(root)
    root.mainloop()