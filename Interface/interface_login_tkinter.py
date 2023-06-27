from struct import pack
import tkinter as tk
from tkinter import SUNKEN, PhotoImage



class SOS:
    def __init__(self, master):
        self.janelaprincipal = master

        
        self.janelaprincipal.title("TELA DE LOGIN")
        self.janelaprincipal.configure()
        self.janelaprincipal.geometry("790x600")




        self.plano_fundo = PhotoImage(file="fundo.png")
        self.lbl_fundo = tk.Label(self.janelaprincipal, image=self.plano_fundo, height=600, width=790)
        self.lbl_fundo.image = self.plano_fundo

        self.lbl_fundo.place(x=0, y=0)

        


        self.frm_direito = tk.Frame(self.janelaprincipal, width=300, height=400, bg="#44284c")
        self.frm_direito.grid(column=2, row=0, pady=90, padx=250)


        

        
        self.photo_usu = PhotoImage(file="clientes.png")
        self.lbl_usu = tk.Label(self.frm_direito, image=self.photo_usu, width=25, height=22, bg="#44284c")
        self.lbl_usu.image = self.photo_usu
        self.lbl_usu.place(x=5, y=195)
        
        text = tk.StringVar()
        text.set("Usuario")
        self.entry_usu = tk.Entry(self.frm_direito, width=30, textvariable=text, bd=3, exportselection=1, borderwidth=3, bg="#44284c")
        self.entry_usu.bind("<Button-1>", self.apaga_usu)
        self.cont_apaga_usu = 0
        self.entry_usu.place(x=55, y=200)

        # self.entry_usu.insert(0, "sas")
    

        self.photo_senha = PhotoImage(file="key.png")
        self.lbl_senha = tk.Label(self.frm_direito, image=self.photo_senha, width=25, height=25, bg="#44284c")
        self.lbl_senha.image = self.photo_senha
        self.lbl_senha.place(x=5, y=245)

        text2 = tk.StringVar()
        text2.set("Senha")
        self.entry_senha = tk.Entry(self.frm_direito, textvariable=text2, width=30, bd=3, exportselection=1, bg="#44284c", show="*")
        self.entry_senha.bind("<Button-1>", self.apaga_senha)
        self.cont_apaga_senha = 0
        self.entry_senha.place(x=55, y=250)




        self.button_login = tk.Button(self.frm_direito, text="Confirmar" ,width=25, overrelief=tk.RIDGE, bg="#44284c", bd=3, activebackground="blue", underline=0)
        self.button_login.place(x=55, y=350)



    def apaga_usu(self, event):
        if self.cont_apaga_usu != 1:
            self.entry_usu.delete(0, tk.END)
            self.cont_apaga_usu += 1


    def apaga_senha(self, event):
        if self.cont_apaga_senha != 1:
            self.entry_senha.delete(0, tk.END)
            self.cont_apaga_senha += 1





janela = tk.Tk()
SOS(janela)
janela.mainloop()
