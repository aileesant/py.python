Você pode criar uma interface gráfica simples para gerar um buquê de flores usando a biblioteca tkinter no Python. O código abaixo mostra como fazer isso, exibindo uma flor por vez no buquê:

import tkinter as tk
import random

class Flor:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.cor_petalas = random.choice(["red", "blue", "yellow", "pink", "purple"])
        self.cor_miolo = "yellow"

    def desenhar(self):
        # Desenhar pétalas (círculos ao redor)
        self.canvas.create_oval(self.x - 30, self.y - 30, self.x, self.y, fill=self.cor_petalas)
        self.canvas.create_oval(self.x, self.y - 30, self.x + 30, self.y, fill=self.cor_petalas)
        self.canvas.create_oval(self.x - 30, self.y, self.x, self.y + 30, fill=self.cor_petalas)
        self.canvas.create_oval(self.x, self.y, self.x + 30, self.y + 30, fill=self.cor_petalas)
        
        # Desenhar miolo (círculo central)
        self.canvas.create_oval(self.x - 15, self.y - 15, self.x + 15, self.y + 15, fill=self.cor_miolo)

class BuqueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Formar um Buquê de Flores")
        
        # Criar área de desenho (canvas)
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Botão para adicionar flores
        self.botao_add_flor = tk.Button(root, text="Adicionar Flor", command=self.adicionar_flor)
        self.botao_add_flor.pack()

    def adicionar_flor(self):
        # Gera uma posição aleatória para a flor
        x = random.randint(50, 350)
        y = random.randint(50, 350)
        
        # Cria e desenha uma nova flor
        flor = Flor(self.canvas, x, y)
        flor.desenhar()

# Inicializa a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = BuqueApp(root)
    root.mainloop()

Explicação:

Tkinter: É uma biblioteca que fornece ferramentas para a criação de interfaces gráficas no Python.

Canvas: É a área onde as flores são desenhadas.

Flor: A classe Flor desenha uma flor com 4 pétalas e um miolo.

BuqueApp: Classe principal que cria a interface com um botão para adicionar flores. Ao clicar no botão, uma nova flor é desenhada em uma posição aleatória no canvas.


Cada vez que o botão "Adicionar Flor" for clicado, uma nova flor será exibida, formando o buquê
