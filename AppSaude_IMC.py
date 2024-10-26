import customtkinter as ctk  #importar a biblioteca tk inter

#------------- funções ------------------------
def imc():
    p = int(peso.get())  #chama oq tá dentro de peso
    a = float(altura.get()) #chama oq tá dentro de altura
    calculo = p/(a*a)

#-------------------------------------------
    if (calculo<18.5):
        situacao = 'Magro(a) 🙂 ' 
    elif (calculo>=18.5 and calculo<25):
        situacao = 'com o peso ideal/normal 😎✌️' 
    elif (calculo>=25 and calculo<30):
        situacao = 'Com sobrepeso 😨'
    else:
        situacao = 'Obeso 😱'          


    resultado.configure(text=f'O seu iMC é: {calculo:.1f} \n Você está {situacao}' )

#------------------fim função---------------------------

#-------- criação da janela ---------------------
ctk.set_appearance_mode('dark') #modo darkj

janela = ctk.CTk() #criar a janela
janela.geometry('500x400') #tamanho da janela
janela.resizable(False,False) #tamanho imóvel


#------------------- título ----------------------------
ctk.CTkLabel(janela,        #CTkLabel cria texto
             text='APP SAÚDE 2024',
             text_color='hot pink',
             font=('arial', 30, 'bold')).pack(pady=10)


#---------------- janela 1 ----------------------------
peso = ctk.CTkEntry(janela,
                    width=400, 
                    height=40,
                    placeholder_text='Digte o seu peso',
                    font=('arial', 16))
peso.pack(pady=10) #ativa a janela. pady é o espaçamento entre as janelas

#---------------- janela 2 ------------------------------
altura = ctk.CTkEntry(janela,
                    width=400, 
                    height=40,
                    placeholder_text='Digte a sua altura',
                    font=('arial', 16))
altura.pack(pady=10) #ativa a janela. pady é o espaçamento entre as janelas

#------------------- botão --------------------------
botao = ctk.CTkButton(janela,
                      width=200,
                      height=60,
                      text='CALCULAR IMC',
                      font=('arial', 15),
                      command=imc)  #pra ativar a funcao imc quando clicar no botao
botao.pack(pady=15) #ativa a janela. pady é o espaçamento entre as janelas

#------------ janela do resultado --------------
resultado = ctk.CTkLabel(janela,
                         text='',
                         font=('arial', 20))
resultado.pack(pady=10) #ativa a janela. pady é o espaçamento entre as janelas

janela.mainloop()
