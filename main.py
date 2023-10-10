import tkinter as tk

# Função para exibir a mensagem com base no número inserido
def exibir_mensagem():
    numero_inserido = entry_numero.get()
    try:
        numero = int(numero_inserido)
        if 1 <= numero <= 7:
            mensagem = "Estoy sonhando com minha bela princesa"
        elif 8 <= numero <= 10:
            mensagem = "Será que minha gata vai me dar um bom dia?"
        elif 11 <= numero <= 12:
            mensagem = "To almoçando mas queria estar rangando ela!"
        elif 13 <= numero <= 15:
            mensagem = "Meu momo está trabalhando, sdds dela!"
        elif 16 <= numero <= 18:
            mensagem = "Quero saber as fofocas do forum!! ksks"
        elif 19 <= numero <= 21:
            mensagem = "Mal posso esperar para ver meu momo!"
        elif 22 <= numero <= 23:
            mensagem = "Meu momento mais feliz da semana, uma hora dessas eu to quase voltando para \n casa com minha princesa!"
        elif numero == 24:
            mensagem = "Minha princesa é uma gostosa, podia estar grudadinho nela, quem sabe até dentro rsrs!"
        else:
            mensagem = "Quem me dera se meu dia tivesse mais horas para poder passar com ela!"
        
        # Atualiza a mensagem no canto superior direito
        label_mensagem.config(text=mensagem)
    except ValueError:
        label_mensagem.config(text="Insira um número válido.")

# Cria uma instância da janela principal
janela = tk.Tk()
janela.title("Relogio do pensamento no meu amor")

# Cria um Entry para inserir o número
entry_numero = tk.Entry(janela)
entry_numero.pack(pady=10)

# Cria um botão para exibir a mensagem
botao_exibir = tk.Button(janela, text="Verificar a hora", command=exibir_mensagem)
botao_exibir.pack()

# Cria um rótulo para exibir a mensagem no canto superior direito
label_mensagem = tk.Label(janela, text="", anchor="e", padx=10)
label_mensagem.pack(side="top", fill="x")

# Define uma mensagem inicial no canto superior direito
mensagem_inicial = "Bem-vindo! Aqui você sabe os tipos de pensamentos que eu tenho por meu AMOR!"
label_mensagem.config(text=mensagem_inicial)
label_mensagem.pack(side="top", fill="x")

# Cria um botão "Sair" para fechar a aplicação
botao_sair = tk.Button(janela, text="Sair", command=janela.quit)
botao_sair.pack()

# Inicia o loop principal da interface gráfica
janela.mainloop()
