import customtkinter as ctk 
# o 'as' serve para apelidar o customtkinter com um nome menor
from tkinter import messagebox 

ctk.set_appearance_mode('white') #o tema da biblioteca agr é emo

#---------------- funções -------------------------------


def calculo(): 
    v = float(valor.get())
    c = float(cotacao.get())
    
    valorfinal = v*c
    messagebox.showinfo('Resultado', f'o valor em reais é :  R${valorfinal}')

#--------------- by Aline --------------------------------

janela = ctk.CTk()
janela.geometry('400x250') #tamanho da janela
janela.resizable(False,False) #para que a janela nao seja redimencionavel
janela.title('Sistema de Conversão de Moedas')
janela.iconbitmap('rocket_money_space_cohet_icon_210916.ico')


ctk.CTkLabel(janela,
             text= 'Sitema de Conversão',
             text_color= 'hot pink',
             font=('arial',25,'bold')).pack(pady=15) #criação do título

valor = ctk.CTkEntry(janela,
                     width=350,
                     height=45,
                     placeholder_text='Digite o valor em dólar: ') #pra add um textinho lá
valor.pack()

cotacao = ctk.CTkEntry(janela,
                     width=350,
                     height=45,
                     placeholder_text='Digite a cotação atual do dólar: ') 
cotacao.pack(pady=10) #o 'pady' serve para dar espaçamento entre as janelas e tal


botao = ctk.CTkButton(janela,
                      text='Calcular',
                      width=150,
                      height=40,
                      fg_color='hot pink',
                      command=calculo) #funcao para fazer o calculo da conversao apos clicar no botao
botao.pack(pady=10) 


janela.mainloop() #mainloop é o 'start' 
