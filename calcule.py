import tkinter as tk
from tkinter import messagebox

class Calculatrice:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculatrice Pro")
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")

        self.equation = ""
        
        # Écran d'affichage
        self.display = tk.Entry(
            root, font=("Arial", 28), borderwidth=5, relief="flat",
            justify='right', bg="#ecf0f1", fg="#2c3e50"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

        # Configuration des boutons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.on_click(x)
            tk.Button(
                root, text=button, width=5, height=2, font=("Arial", 14, "bold"),
                bg=self.get_color(button), fg="white", relief="flat",
                command=action
            ).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
            
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configuration du poids des colonnes/lignes
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(1, 5):
            root.grid_rowconfigure(i, weight=1)

    def get_color(self, btn):
        """Définit les couleurs selon le type de bouton"""
        if btn == 'C': return "#e74c3c"  # Rouge
        if btn == '=': return "#27ae60"  # Vert
        if btn in ['/', '*', '-', '+']: return "#34495e" # Gris foncé
        return "#7f8c8d" # Gris clair

    def on_click(self, char):
        if char == 'C':
            self.equation = ""
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                # Évaluation de l'expression mathématique
                result = str(eval(self.equation))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
                self.equation = result
            except ZeroDivisionError:
                messagebox.showerror("Erreur", "Division par zéro impossible")
                self.on_click('C')
            except Exception:
                messagebox.showerror("Erreur", "Expression invalide")
                self.on_click('C')
        else:
            self.equation += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.equation)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculatrice(root)
    root.mainloop()