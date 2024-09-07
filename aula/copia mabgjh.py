import tkinter as tk

# Criar a janela principal
janela = tk.Tk()

# Definir o título da janela
janela.title("Minha Janela com Tkinter")

# Definir o tamanho da janela (largura x altura)
janela.geometry("400x300")

# Adicionar um rótulo (texto na janela)
rotulo = tk.Label(janela, text="Olá, Mundo!", font=("Arial", 16))
rotulo.pack(pady=20)  # Adiciona espaçamento vertical

# Adicionar um botão
botao = tk.Button(janela, text="Clique aqui", font=("Comics sans ms", 14), command=lambda: print("Botão clicado!"))
botao.pack(pady=10)

# Executar o loop principal da janela
janela.mainloop()