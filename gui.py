import random
import tkinter as tk
from tkinter import messagebox

# Import the candidate word list from your existing file
from candidatewords import candidateWords


def correctletters(password, guess):
    return sum(1 for a, b in zip(password, guess) if a == b)


class WordGameGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Guess The Word')
        self.resizable(False, False)
        self.password = ''
        self.words = []
        self.guesses_left = 0

        # Difficulty selection
        self.difficulty_var = tk.StringVar(value='Easy')
        diff_frame = tk.LabelFrame(self, text='Difficulty')
        diff_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        for i, (label, _) in enumerate([('Easy', 4), ('Medium', 3), ('Hard', 2)]):
            rb = tk.Radiobutton(diff_frame, text=label, variable=self.difficulty_var, value=label)
            rb.grid(row=0, column=i, padx=5, pady=5)

        # Start button
        start_btn = tk.Button(self, text='Start Game', command=self.start_game)
        start_btn.grid(row=1, column=0, padx=10, pady=(0,10), sticky='ew')

        # Status
        status_frame = tk.Frame(self)
        status_frame.grid(row=2, column=0, padx=10, pady=(0,10), sticky='ew')
        tk.Label(status_frame, text='Guesses Remaining:').grid(row=0, column=0, sticky='w')
        self.guess_label = tk.Label(status_frame, text='-')
        self.guess_label.grid(row=0, column=1, sticky='w', padx=(5,0))

        self.message_label = tk.Label(self, text='', fg='blue')
        self.message_label.grid(row=3, column=0, padx=10, pady=(0,10))

        # Word buttons
        words_frame = tk.LabelFrame(self, text='Words (click to guess)')
        words_frame.grid(row=4, column=0, padx=10, pady=(0,10))
        self.word_buttons = []
        for i in range(8):
            btn = tk.Button(words_frame, text='', width=16, state='disabled', command=lambda i=i: self.make_guess(i))
            btn.grid(row=i//2, column=i%2, padx=5, pady=5)
            self.word_buttons.append(btn)

        # Play again
        self.play_again_btn = tk.Button(self, text='Play Again', command=self.start_game, state='disabled')
        self.play_again_btn.grid(row=5, column=0, padx=10, pady=(0,10), sticky='ew')

        # Quit
        quit_btn = tk.Button(self, text='Quit', command=self.quit)
        quit_btn.grid(row=6, column=0, padx=10, pady=(0,10), sticky='ew')

    def start_game(self):
        # Determine guesses based on difficulty
        diff = self.difficulty_var.get()
        if diff == 'Easy':
            self.guesses_left = 4
        elif diff == 'Medium':
            self.guesses_left = 3
        else:
            self.guesses_left = 2

        self.words = random.sample(candidateWords, 8)
        self.password = random.choice(self.words)

        # Update UI
        for i, w in enumerate(self.words):
            self.word_buttons[i]['text'] = w
            self.word_buttons[i]['state'] = 'normal'
        self.message_label['text'] = 'Password is one of the shown words.'
        self.update_status()
        self.play_again_btn['state'] = 'disabled'

    def update_status(self):
        self.guess_label['text'] = str(self.guesses_left)

    def make_guess(self, index):
        if self.guesses_left <= 0:
            return
        guess_word = self.words[index]
        self.guesses_left -= 1
        if guess_word == self.password:
            self.message_label['text'] = f'Password correct: "{guess_word}". CONGRATULATIONS, YOU WON!'
            self.end_game(win=True)
            return

        correct = correctletters(self.password, guess_word)
        self.message_label['text'] = f'Password incorrect. {correct}/{len(self.password)} letters correct.'
        # Disable the guessed button so user can't guess it again
        self.word_buttons[index]['state'] = 'disabled'
        self.update_status()

        if self.guesses_left == 0:
            self.end_game(win=False)

    def end_game(self, win=False):
        # Reveal password if lost
        if not win:
            self.message_label['text'] = f'You ran out of guesses. The password was "{self.password}".'
        # Disable all word buttons
        for btn in self.word_buttons:
            btn['state'] = 'disabled'
        self.play_again_btn['state'] = 'normal'
        # Show a custom dialog box instead of messagebox
        self.show_gameover_dialog(win)

    def show_gameover_dialog(self, win):
        dialog = tk.Toplevel(self)
        dialog.title('Game Over')
        dialog.resizable(False, False)
        dialog.grab_set()
        # Center the dialog over the main window
        self.update_idletasks()
        x = self.winfo_x() + (self.winfo_width() // 2) - 150
        y = self.winfo_y() + (self.winfo_height() // 2) - 60
        dialog.geometry(f"300x120+{x}+{y}")
        # Simple, classic look
        if win:
            msg = 'CONGRATULATIONS!\nYou guessed the password.'
        else:
            msg = f'You lost. The password was:\n"{self.password}"'
        label = tk.Label(dialog, text=msg, font=('Arial', 12), pady=20)
        label.pack()
        btn_frame = tk.Frame(dialog)
        btn_frame.pack(pady=10)
        play_again_btn = tk.Button(btn_frame, text='Play Again', width=12, command=lambda: [dialog.destroy(), self.start_game()])
        play_again_btn.grid(row=0, column=0, padx=10)
        quit_btn = tk.Button(btn_frame, text='Quit', width=12, command=self.quit)
        quit_btn.grid(row=0, column=1, padx=10)
        dialog.protocol("WM_DELETE_WINDOW", dialog.destroy)


if __name__ == '__main__':
    app = WordGameGUI()
    app.mainloop()
