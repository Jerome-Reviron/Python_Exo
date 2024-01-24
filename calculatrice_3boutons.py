import tkinter as tk

class ScrollableCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculatrice à 3 boutons")

        self.character_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '=', 'R', ')', '(']
        self.current_index = 0
        self.choices = []

        self.display = tk.Entry(master, width=10, font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=3, pady=5)

        # Boutons pour faire défiler la liste
        tk.Button(master, text='↑', width=4, height=2, command=lambda: self.scroll(1)).grid(row=1, column=0)
        tk.Button(master, text='↓', width=4, height=2, command=lambda: self.scroll(-1)).grid(row=2, column=0)

        # Bouton pour valider le choix
        tk.Button(master, text='Valider', width=10, height=2, command=self.validate_choice).grid(row=1, column=1, rowspan=2)
        
        self.history_text = []

    def scroll(self, direction):
        self.current_index = (self.current_index + direction) % len(self.character_list)
        current_text = self.display.get()
        new_text = current_text[:-1] + self.character_list[self.current_index]
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, new_text)

    def validate_choice(self):
        selected_char = self.character_list[self.current_index]
        current_text = self.display.get()

        if selected_char == 'R':
            # Redémarrer l'application si 'R' est sélectionné
            self.reset_application()
            return

        if selected_char == '=':
            try:
                result = eval(current_text.replace('=', ''))
                self.choices.append(result)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                print("Error:", e)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erreur")
        else:
            new_text = current_text + selected_char
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, new_text)

        self.last_clicked = selected_char  # Mettre à jour le dernier caractère cliqué

    def reset_application(self):
        # Réinitialiser l'application
        self.choices = []
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScrollableCalculator(root)
    root.mainloop()
