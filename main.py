from nicegui import ui

class Calculatrice:
    def __init__(self):
        self.equation = ""
        self.result_label = None

    def on_click(self, value):
        if value == 'C':
            self.equation = ""
        elif value == '=':
            try:
                # Utilisation de eval() pour la démonstration pédagogique.
                # Note pour le rapport de stage : En production, privilégier ast.literal_eval.
                self.equation = str(eval(self.equation))
            except Exception:
                self.equation = "Erreur"
        else:
            if self.equation == "Erreur":
                self.equation = ""
            self.equation += str(value)

        if self.result_label:
            self.result_label.set_text(self.equation)

# --- Design de l'Interface ---
calc = Calculatrice()

with ui.card().classes('w-80 mx-auto shadow-lg mt-10'):
    with ui.column().classes('w-full items-center'):
        ui.label('Calculatrice Next-Gen').classes('text-h6 text-grey-8')

        # Écran d'affichage
        calc.result_label = ui.label('0').classes(
            'w-full bg-slate-100 p-4 text-right text-2xl font-mono rounded min-h-[64px] border'
        )

        # Grille des boutons
        with ui.grid(columns=4).classes('w-full gap-2 mt-4'):
            buttons = [
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                'C', '0', '=', '+'
            ]

            for btn in buttons:
                # Couleurs spécifiques pour les fonctions spéciales
                if btn == 'C':
                    color = 'red'
                elif btn == '=':
                    color = 'green'
                else:
                    color = 'primary'
                
                ui.button(btn, on_click=lambda b=btn: calc.on_click(b)).props(f'color={color}').classes('h-12 text-lg')

# --- Lancement de l'application ---
# host='0.0.0.0' : indispensable pour que Docker puisse exposer l'app.
# port=5000 : port interne défini dans ton Terraform.
# reload=False : évite les redémarrages inutiles dans le conteneur.
ui.run(host='0.0.0.0', port=5000, title='Calculatrice Pro', reload=False)
