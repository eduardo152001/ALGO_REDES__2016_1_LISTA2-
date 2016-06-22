import tkinter
from tkinter import messagebox
from projeto2 import funcao_nmap
import nmap

portscan = tkinter.Tk()

portscan.title("portscan")
portscan.geometry("600x600+400+50")
portscan.configure(background='#c0c0c0')


photo = tkinter.PhotoImage(file="cabo.gif")
w = tkinter.Label(portscan, bg="#FFFFFF", image=photo)
w.pack()

texto = tkinter.Label(portscan, text="Bem Vindo ao portscan", fg="#000000", bg="#c0c0c0", font=("arial", 18))
texto.pack()

ip = tkinter.Label(portscan, text="digite o ip abaixo", bg='#c0c0c0', font=("Arial", 12))
ip.pack()

ent = tkinter.Entry(portscan)
ent.pack()


def clicado():
    funcao_nmap(ent.get())
    print(ent.get())
    relatorio = open("relatorio.txt", "w")
    relatorio.write(ent.get())
    relatorio.close()
    messagebox.showinfo("Relatorio Salvo com Sucesso")

btn = tkinter.Button(portscan, text="Gerar e Salvar Relatorio",
                     command=clicado)
btn.pack()

def start():
    messagebox.showinfo("VOLTE SEMPRE.")
    exit(0)

bq = tkinter.Button(portscan, text="Sair",
                    command=start)
bq.pack()

portscan.mainloop()