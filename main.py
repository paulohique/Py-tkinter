import tkinter as tk
from tkinter import ttk, messagebox

def mostrar_aviso():
    numero_inserido = entry_numero.get()
    try:
        numero = int(numero_inserido)
        if 1 <= numero <= 7:
            mensagem = "1"
        elif 8 <= numero <= 10:
            mensagem = "2"
        elif 11 <= numero <= 12:
            mensagem = "3"
        elif 13 <= numero <= 15:
            mensagem = "4"
        elif 16 <= numero <= 18:
            mensagem = "5"
        elif 19 <= numero <= 21:
            mensagem = "6"
        elif 22 <= numero <= 23:
            mensagem = "7"
        elif numero == 24:
            mensagem = "8"
        else:
            mensagem = "9"

        messagebox.showinfo("Pensamento", mensagem)
    except ValueError:
        messagebox.showerror("Erro", "Insira um horário válido.")

janela = tk.Tk()
janela.title("Relogio do pensamento em meu amor")
largura_janela = 200
altura_janela = 210

posicao_x = (janela.winfo_screenwidth() // 2) - (largura_janela // 2)
posicao_y = (janela.winfo_screenheight() // 2) - (altura_janela // 2)

janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")


entry_numero = tk.Entry(janela)
entry_numero.pack(pady=10)

label_mensagem = tk.Label(janela, text="", anchor="e", padx=10)
label_mensagem.pack(side="top", fill="x")

mensagem_inicial = "Bem-vindo(a)"
label_mensagem.config(text=mensagem_inicial)
label_mensagem.pack(padx= 10, pady=10)


botao_exibir = ttk.Button(janela, text="Verificar a hora", command=mostrar_aviso)
botao_exibir.pack()

botao_sair = ttk.Button(janela, text="Sair", command=janela.quit)
botao_sair.pack()

janela.mainloop()
