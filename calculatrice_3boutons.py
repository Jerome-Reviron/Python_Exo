import tkinter as tk

class ScrollableCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculatrice à 3 boutons")

        self.character_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '=']
        self.current_index = 0

        self.display = tk.Entry(master, width=10, font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=3, pady=5)

        # Boutons pour faire défiler la liste
        tk.Button(master, text='↑', width=4, height=2, command=self.scroll_up).grid(row=1, column=0)
        tk.Button(master, text='↓', width=4, height=2, command=self.scroll_down).grid(row=2, column=0)

        # Bouton pour valider le choix
        tk.Button(master, text='Valider', width=10, height=2, command=self.validate_choice).grid(row=1, column=1, rowspan=2)

    def scroll_up(self):
        self.current_index = (self.current_index + 1) % len(self.character_list)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.character_list[self.current_index])

    def scroll_down(self):
        self.current_index = (self.current_index - 1) % len(self.character_list)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.character_list[self.current_index])

    def validate_choice(self):
        selected_char = self.character_list[self.current_index]
        if selected_char in ['+', '-', '*', '/'] and self.display.get() and self.display.get()[-1] in ['+', '-', '*', '/']:
            # Ne pas ajouter deux opérateurs successifs
            return
        elif selected_char == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erreur")
        else:
            self.display.insert(tk.END, selected_char)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScrollableCalculator(root)
    root.mainloop()
