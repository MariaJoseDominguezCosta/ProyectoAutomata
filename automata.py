import tkinter as tk

class Automata:
    def __init__(self):
        # Definimos los estados del autómata
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11'}
        
        # Definimos el alfabeto válido
        self.alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-")
        
        # Definimos las transiciones del autómata como un diccionario
        self.transitions = {
            'q0': {'E': 'q1', 'F': 'q2'},
            'q1': {'U': 'q3', 'V': 'q3', 'W': 'q3', 'X': 'q3', 'Y': 'q3', 'Z': 'q3'},
            'q2': {'A': 'q3', 'B': 'q3', 'C': 'q3', 'D': 'q3', 'E': 'q3', 'F': 'q3', 'G': 'q3', 'H': 'q3', 'I': 'q3', 'J': 'q3', 'K': 'q3', 'L': 'q3', 'M': 'q3', 'N': 'q3', 'O': 'q3', 'P': 'q3'},
            'q3': {'A': 'q4', 'B': 'q4', 'C': 'q4', 'D': 'q4', 'E': 'q4', 'F': 'q4', 'G': 'q4', 'H': 'q4', 'I': 'q4', 'J': 'q4', 'K': 'q4', 'L': 'q4', 'M': 'q4', 'N': 'q4', 'O': 'q4', 'P': 'q4', 'Q': 'q4', 'R': 'q4', 'S': 'q4', 'T': 'q4', 'U': 'q4', 'V': 'q4', 'W': 'q4', 'X': 'q4', 'Y': 'q4', 'Z': 'q4'},
            'q4': {'-': 'q5'},
            'q5': {'0': 'q6', '1': 'q12', '2': 'q12', '3': 'q12', '4': 'q12', '5': 'q12', '6': 'q12', '7': 'q12', '8': 'q12', '9': 'q12'},
            'q6': {'0': 'q7','1': 'q8', '2': 'q8', '3': 'q8', '4': 'q8', '5': 'q8', '6': 'q8', '7': 'q8', '8': 'q8', '9': 'q8'},
            'q7': {'1': 'q9', '2': 'q9', '3': 'q9', '4': 'q9', '5': 'q9', '6': 'q9', '7': 'q9', '8': 'q9', '9': 'q9'},
            'q8': {'0': 'q9', '1': 'q9', '2': 'q9', '3': 'q9', '4': 'q9', '5': 'q9', '6': 'q9', '7': 'q9', '8': 'q9', '9': 'q9'},
            'q9': {'-': 'q10'},
            'q10': {'A': 'q11', 'B': 'q11', 'C': 'q11', 'D': 'q11', 'E': 'q11', 'F': 'q11', 'G': 'q11', 'H': 'q11', 'I': 'q11', 'J': 'q11', 'K': 'q11', 'L': 'q11', 'M': 'q11', 'N': 'q11', 'O': 'q11', 'P': 'q11', 'Q': 'q11', 'R': 'q11', 'S': 'q11', 'T': 'q11', 'U': 'q11', 'V': 'q11', 'W': 'q11', 'X': 'q11', 'Y': 'q11', 'Z': 'q11'},
            'q12': {'0': 'q8','1': 'q8', '2': 'q8', '3': 'q8', '4': 'q8', '5': 'q8', '6': 'q8', '7': 'q8', '8': 'q8', '9': 'q8'},
            'q11': {}
        }
        
        # Definimos el estado inicial
        self.start_state = 'q0'
        
        # Definimos los estados de aceptación
        self.accept_states = {'q11'}

    def is_valid_string(self, input_string):
        current_state = self.start_state
        
        # Procesamos cada carácter de la cadena de entrada
        for char in input_string:
            if char not in self.alphabet:
                return False  # Carácter no válido
            
            # Verificamos si hay una transición desde el estado actual con el carácter actual
            if char in self.transitions[current_state]:
                current_state = self.transitions[current_state][char]
            else:
                return False  # No hay una transición válida para el carácter
        
        # Verificamos si el estado actual es un estado de aceptación
        return current_state in self.accept_states
    
class AutomataGUI:
    def __init__(self, root):
        self.root = root
        root.title("Autómata GUI")
        
        self.automaton = Automata()
        
        # Etiqueta y entrada de texto
        self.label = tk.Label(root, text="Ingrese una cadena:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        # Botón de evaluación
        self.evaluate_button = tk.Button(root, text="Evaluar", command=self.evaluate)
        self.evaluate_button.pack()
        
        # Área de texto para mostrar el recorrido por estados
        self.text_area = tk.Text(root, height=10, width=40)
        self.text_area.pack()

    def evaluate(self):
        input_string = self.entry.get()
        
        if self.automaton.is_valid_string(input_string):
            self.text_area.delete('1.0', tk.END)  # Borra el contenido anterior
            current_state = self.automaton.start_state
            self.text_area.insert(tk.END, f"Estado inicial: {current_state}\n")
            
            for char in input_string:
                if char in self.automaton.transitions[current_state]:
                    current_state = self.automaton.transitions[current_state][char]
                    self.text_area.insert(tk.END, f"Carácter: {char}, Siguiente estado: {current_state}\n")
                else:
                    self.text_area.insert(tk.END, f"Carácter no válido: {char}\n")
                    break
            
            if current_state in self.automaton.accept_states:
                self.text_area.insert(tk.END, "La cadena es válida.")
            else:
                self.text_area.insert(tk.END, "La cadena no es válida.")
        else:
            self.text_area.delete('1.0', tk.END)  # Borra el contenido anterior
            self.text_area.insert(tk.END, "La cadena no es válida.")

# Crear la ventana de la aplicación
root = tk.Tk()
app = AutomataGUI(root)
root.mainloop()