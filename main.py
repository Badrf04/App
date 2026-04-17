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
                # Note pour ton projet Cyber : eval() est une fonction à risque (injection)
                # Mais elle est parfaite pour démontrer le fonctionnement de Bandit.
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
        calc.result_label = ui.label('').classes('w-full bg-slate-100 p-4 text-right text-2xl font-mono rounded min-h-[64px]')

        # Grille des boutons
        with ui.grid(columns=4).classes('w-full gap-2 mt-4'):
            buttons = [
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                'C', '0', '=', '+'
            ]
            
            for btn in buttons:
                color = 'red' if btn == 'C' else 'green' if btn == '=' else 'primary'
                ui.button(btn, on_click=lambda b=btn: calc.on_click(b)).props(f'color={color}').classes('h-12 text-lg')

# IMPORTANT : host='0.0.0.0' est OBLIGATOIRE pour Docker
# port=5000 est le port interne du conteneur
ui.run(host='0.0.0.0', port=5000, title='Calculatrice Pro', reload=False)
