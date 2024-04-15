import tkinter as tk
from tkinter import messagebox
from Services import Elevador

def subir():
    if elevador.atualAndar < elevador.totalAndar:
        elevador.Subir()
        messagebox.showinfo('Ação do Elevador', 'Subindo')
    else:
        messagebox.showinfo('Ação do Elevador', 'Você está no andar mais alto!')

def descer():
    if elevador.atualAndar > 0:
        elevador.Descer()
        messagebox.showinfo('Ação do Elevador', 'Descendo')
    else:
        messagebox.showinfo('Ação do Elevador', 'Você já está no térreo!')

def entrar():
    if elevador.atualCapacidade < elevador.totalCapacidade:
        elevador.Entrar()
        messagebox.showinfo('Ação do Elevador','Entrando uma pessoa')
    else:
        messagebox.showinfo('Ação do Elevador','Está lotado!')

def sair():
    if elevador.atualCapacidade > 0:
        elevador.Sair()
        messagebox.showinfo('Ação do Elevador', 'Saindo uma pessoa')
    else:
        messagebox.showinfo('Ação do Elevador', 'NÃO TEM NINGUÉM')


# Elevador com capacidade máxima de 6 pessoas e 3 andares
elevador = Elevador(6, 3)

# Configurações da janela
root = tk.Tk()
root.title('Controle de Elevador')
root.geometry('650x500')
# Cor de fundo do menu
root.config(bg='black')

# Criando o menu
menu = tk.Menu(root, bg='black', fg='white')
root.config(menu=menu)

# Criando o menu das ações
menu_acoes = tk.Menu(menu,bg='black', fg='white')

menu.add_cascade(label='Ações ►', menu=menu_acoes)

menu_acoes.add_command(label='Subir', command=subir)

menu_acoes.add_command(label='Descer', command=descer)

menu_acoes.add_command(label='Entrar', command=entrar)

menu_acoes.add_command(label='Sair', command=sair)

# Criando o menu informações
menu_info = tk.Menu(menu, tearoff=0, bg='black', fg='white')

menu.add_cascade(label='Informações ◄', menu=menu_info)

menu_info.add_command(label='Capacidade Atual', command=lambda: messagebox.showinfo('Informações do Elevador', f'Capacidade Atual: {elevador.atualCapacidade}'))

menu_info.add_command(label='Andar Atual', command=lambda: messagebox.showinfo('Informações do Elevador', f'Andar Atual: {elevador.atualAndar}'))

# Mensagem centralizada
mensagem_label = tk.Label(root, text='Acesse os campos acima para a funcionalidade do sistema', bg='black', fg='white', font=('Georgia', 15))
mensagem_label.pack(expand=True)

# Configuração da mensagem centralizada
mensagem_label.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()
