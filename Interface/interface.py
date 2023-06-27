
from distutils.cmd import Command
from multiprocessing import Value
import tkinter as tk
from tkinter import ttk
from tkinter import NSEW, RAISED, RIDGE, Button, Entry, Frame, Label, Widget, ttk
from turtle import width
from webbrowser import BackgroundBrowser
from tkinter import messagebox

janela = tk.Tk()

janela.title('')
#janela.geometry("310x300")
#janela.minsize(310, 300)
janela.configure(background="#20b2aa")
# janela.resizable(width=False, height=False)

#Dividindo a janela
frame_cima = tk.Frame(janela, width=310, height=50, bg="#20b2aa", relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)


frame_baixo = tk.Frame(janela, width=310, height=250, bg="#20b2aa", relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#configurando o fram cima
lbl_cima = Label(frame_cima, text="LOGIN", font=("Ivy 25"), bg="#20b2aa", fg="#111111")
lbl_cima.place(x=5, y=5)

lbl_linha = Label(frame_cima, text="",width=280,  font=("Ivy 1"), bg="#ffa500")
lbl_linha.place(x=10, y=45)


credenciais = ["Elias", "12345"]
#função vericar senha
def verifica_senha():
    nome = entry_nome.get()
    senha = entry_senha.get()

    if nome == "admin" and senha == "admin":
        messagebox.showinfo("Login", "Seja bem vindo admin!")
        for widget in frame_baixo.winfo_children():
            widget.destroy() 
        for widget in frame_cima.winfo_children():
            widget.destroy()
        nova_janela() 
    elif credenciais[0] == nome and credenciais[1] == senha:
        # messagebox.showinfo("Login", "Seja bem vindo de volta: " + credenciais[0] )
        
        #deletar itens presentes nos Frames
        for widget in frame_baixo.winfo_children():
            widget.destroy() 
        for widget in frame_cima.winfo_children():
            widget.destroy()
        nova_janela() 
    else:
        messagebox.showwarning("Error", "Verifique o nome e a senha novamente!!!")

#função após verificar a senha
def nova_janela():
    lbl_cima = Label(frame_cima, text="Usuario: " + credenciais[0], font=("Ivy 20"), bg="#20b2aa", fg="#111111")
    lbl_cima.place(x=5, y=5)

    lbl_linha = Label(frame_cima, text="",width=280,  font=("Ivy 1"), bg="#ffa500")
    lbl_linha.place(x=10, y=45)

    lbl_cima = Label(frame_baixo, text="Seja bem vindo", font=("Ivy 20"), bg="#20b2aa", fg="#111111")
    lbl_cima.place(x=5, y=105)

    v = tk.StringVar()
    cbx = ttk.Combobox(janela, width=12, textvariable=v)
    cbx["value"] = ("Chá", "Café", "Rosquinha", "Leite", "Água")
    cbx.place(x=120, y=210)
    mnu_barra = tk.Menu(janela)
    mnu_var1 = tk.Menu(mnu_barra, tearoff=0)
    mnu_barra.add_cascade(label = "Menu", menu = mnu_var1)
    mnu_var1.add_command(label="Abrir Arquivo", command= None)
    mnu_var1.add_command(label="pesquisar", command=None)
    janela.config(menu = mnu_barra)

#configurando frame baixo
lbl_nome = Label(frame_baixo, text="Nome *", font=("Ivy 13"), bg="#20b2aa", fg="#111111")
lbl_nome.place(x=10, y=20)

entry_nome = Entry(frame_baixo, width=25, justify="left", font=("", 15), highlightthickness=1, relief="solid")
entry_nome.place(x=14, y=50)


lbl_senha = Label(frame_baixo, text="Senha *", font=("Ivy 13"), bg="#20b2aa", fg="#111111")
lbl_senha.place(x=10, y=95)

entry_senha = Entry(frame_baixo, width=25, justify="left", show="*", font=("", 15), highlightthickness=1, relief="solid")
entry_senha.place(x=14, y=130)



botao_confirmar = Button(frame_baixo, command=verifica_senha, text="Entrar", width=39, height=2, font=("Ivy 8 bold"), bg="#ffa500", fg="#111111", overrelief=RIDGE)#relief=RAISED,
botao_confirmar.place(x=15, y=180)

# scrollbar = tk.Scrollbar(janela)
# scrollbar.place(x=291, y=0)


janela.mainloop()