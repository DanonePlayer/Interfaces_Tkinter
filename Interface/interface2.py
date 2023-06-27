import tkinter as tk
from turtle import st, width
from webbrowser import BackgroundBrowser

class Tela():
    def __init__(self,master):
        self.janela = master
        self.janela.title("Login")
        self.janela.configure(background="#696969")
        self.janela.geometry("400x600")

        
        self.fr = tk.Frame(janela, bg="#696969", width=900, relief="flat", height=50)
        self.fr.grid(column=0, row=0)


        self.lbl_login = tk.Label(self.fr, text="LOGIN", font="Loma, 22", bg="#696969")
        self.lbl_login.grid(row=0, column=0)

        self.lbl_linha = tk.Label(self.fr, text="", font="Arial, 1", bg="#ffa500", width=370)
        self.lbl_linha.grid(row=1, column=0, padx=5)


        self.lbl_usuario = tk.Label(text="Usuario:", font="Arial, 15", bg="#696969").grid(row=5, column=0, sticky=tk.W, padx=12, pady=20)
        self.ent1 = tk.Entry(text="" )


        self.lbl_senha = tk.Label(text="Senha:", font="Arial, 15", bg="#696969").grid(row=6, column=0, sticky=tk.W, padx=12)

        self.ent = tk.Entry()
        
        

janela = tk.Tk()
Tela(janela)
janela.mainloop()
        