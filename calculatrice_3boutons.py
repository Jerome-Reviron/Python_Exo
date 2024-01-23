import tkinter as tk

class ScrollableCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculatrice à 3 boutons")

        self.character_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '=']
        self.current_index = 0
        self.choices = []
        self.validation_pressed = False  # Variable pour suivre si le bouton "Valider" a été pressé

        self.display = tk.Entry(master, width=10, font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=3, pady=5)

        # Boutons pour faire défiler la liste
        tk.Button(master, text='↑', width=4, height=2, command=self.scroll_up).grid(row=1, column=0)
        tk.Button(master, text='↓', width=4, height=2, command=self.scroll_down).grid(row=2, column=0)

        # Bouton pour valider le choix
        tk.Button(master, text='Valider', width=10, height=2, command=self.validate_choice).grid(row=1, column=1, rowspan=2)

    def scroll_up(self):
        self.current_index = (self.current_index + 1) % len(self.character_list)
        current_text = self.display.get()
        if current_text:
            new_text = current_text[:-1] + self.character_list[self.current_index]
        else:
            new_text = self.character_list[self.current_index]
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, new_text)

    def scroll_down(self):
        self.current_index = (self.current_index - 1) % len(self.character_list)
        current_text = self.display.get()
        if current_text:
            new_text = current_text[:-1] + self.character_list[self.current_index]
        else:
            new_text = self.character_list[self.current_index]
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, new_text)

    def validate_choice(self):
        selected_char = self.character_list[self.current_index]
        current_text = self.display.get()

        print("Selected Char:", selected_char)
        print("Current Text:", current_text)

        if selected_char == '=':
            try:
                if len(self.choices) > 0 and not self.validation_pressed:
                    # Utiliser le résultat précédent et effectuer l'opération avec le nouveau texte (en enlevant le "=" final)
                    previous_result = self.choices[-1]
                    calculation_text = str(previous_result) + current_text.replace('=', '')
                    print("Calculation Text:", calculation_text)
                    result = eval(calculation_text)
                    self.choices.append(result)
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, str(result))
                else:
                    # Aucune opération précédente, utiliser le texte actuel
                    result = eval(current_text.replace('=', ''))
                    self.choices.append(result)
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, str(result))
            except Exception as e:
                print("Error:", e)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erreur")

            # Marquer le bouton "Valider" comme pressé
            self.validation_pressed = True
        else:
            if current_text:
                new_text = current_text + selected_char
            else:
                new_text = selected_char
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, new_text)

            # Réinitialiser les choix si "=" est pressé une deuxième fois
            if selected_char == '=' and len(self.choices) > 0:
                self.choices = []
                self.validation_pressed = False  # Réinitialiser la variable de validation

if __name__ == "__main__":
    root = tk.Tk()
    app = ScrollableCalculator(root)
    root.mainloop()
