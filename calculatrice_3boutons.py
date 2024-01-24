"""Module pour une calculatrice à 3 boutons en utilisant Tkinter."""
import tkinter as tk

class ScrollableCalculator:
    """Classe représentant une calculatrice à 3 boutons en utilisant Tkinter."""
    def __init__(self, master):
        """
        Initialise la calculatrice avec le maître donné.

        :param master: Le maître pour la calculatrice.
        :type master: tk.Tk
        """
        self.master = master
        self.master.title("Calculatrice à 3 boutons")

        self.character_list = ['0', '1', '2', '3', '4', '5',
                            '6', '7', '8', '9', '+', '-',
                            '*', '/', '=', 'R', '(', ')', '.', '%']
        self.current_index = 0
        self.choices = []

        self.display = tk.Entry(master, width=50, font=('Arial', 18))
        self.display.grid(row=0, column=0, columnspan=3, pady=5)

        # Boutons pour faire défiler la liste
        tk.Button(master, text='↑', width=6, height=4,
                command=lambda: self.scroll(1)).grid(row=1, column=0)
        tk.Button(master, text='↓', width=6, height=4,
                command=lambda: self.scroll(-1)).grid(row=2, column=0)

        # Bouton pour valider le choix
        tk.Button(master, text='Valider', width=12, height=4,
                command=self.validate_choice).grid(row=1, column=1, rowspan=2)

        self.history_text = []
        self.last_clicked = None
        self.last_clicked = None
        # Désactiver l'utilisation du clavier
        master.bind("<Key>", lambda e: "break")

    def scroll(self, direction):
        """
        Fait défiler la liste des caractères dans la zone d'affichage.

        :param direction: La direction du défilement, 1 pour monter, -1 pour descendre.
        :type direction: int
        """
        self.current_index = (self.current_index + direction) % len(self.character_list)
        current_text = self.display.get()
        new_text = current_text[:-1] + self.character_list[self.current_index]
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, new_text)

    def validate_choice(self):
        """
        Valide le choix de l'utilisateur en fonction du caractère sélectionné.

        Si 'R' est sélectionné, l'application est redémarrée. Si '=' est sélectionné,
        une tentative d'évaluation de l'expression est effectuée, et le résultat est affiché.
        Sinon, le caractère sélectionné est ajouté à l'affichage actuel.

        En cas de division par zéro, un message d'erreur approprié est affiché.
        """
        selected_char = self.character_list[self.current_index]
        current_text = self.display.get()

        if selected_char == 'R':
            # Redémarrer l'application si 'R' est sélectionné
            self.reset_application()
            return

        if selected_char == '=':
            try:
                # Vérifier la division par zéro
                if '/' in current_text:
                    parts = current_text.split('/')
                    if len(parts) == 2 and parts[1] == '0':
                        raise ZeroDivisionError("Division par zéro impossible")

                result = eval(current_text.replace('=', '')) # pylint: disable=W0123
                self.choices.append(result)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except ZeroDivisionError:
                error_message = "Division par zéro impossible"
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, error_message)
            except ValueError as ve:
                print("Error:", ve)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erreur")

        else:
            new_text = current_text + selected_char
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, new_text)

        self.last_clicked = selected_char  # Mettre à jour le dernier caractère cliqué

    def reset_application(self):
        """
        Réinitialise l'état de l'application.

        Efface l'historique des choix et réinitialise la zone d'affichage.
        """
        # Réinitialiser l'application
        self.choices = []
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScrollableCalculator(root)
    root.mainloop()
