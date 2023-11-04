
#Rode pip install tk messagebox github pygithub

import io
import tkinter as tk
from tkinter import messagebox, filedialog
import os
from github import Github
import time


# Informações de autenticação
token = input("Insira seu token do github:")

# Autenticação usando token
g = Github(token)

# Função para criar um repositório
def criar_repositorio():
    # Cria a janela secundária
    subwindow = tk.Toplevel(window)
    subwindow.title("Criar Repositório")

    # Variáveis de entrada
    nome_var = tk.StringVar()
    descricao_var = tk.StringVar() 
    diretorio_var = tk.StringVar()
    publico_var = tk.BooleanVar()

    def btn_criar_click():
        # Obtém os valores das variáveis de entrada
        nome = nome_var.get()
        descricao = descricao_var.get()
        diretorio = diretorio_var.get()
        is_publico = publico_var.get()

        # Criação do repositório
        usuario = g.get_user()
        repositorio = usuario.create_repo(nome, description=descricao, private=not is_publico)
        tipo_repositorio = "público" if is_publico else "privado"
        messagebox.showinfo("Ação", f"Repositório '{nome}' criado com sucesso!\nTipo: {tipo_repositorio}")
        
        #upload de arquivo
        repo = g.get_repo(f'{usuario.login}/{nome}')
        descricao = entry_descricao.get(1.0, tk.END).strip() + '\n'  # Adiciona uma quebra de linha
        repo.create_file('README.md', 'commit inicial', descricao, branch="main")



        # Aguarda 2 segundos antes de obter o conteúdo do arquivo
        time.sleep(2)

        contents = repo.get_contents("README.md")
        print(contents)
            
        # Carrega os arquivos do diretório local
        for raiz, diretorios, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                caminho_completo = os.path.join(raiz, arquivo)
                with open(caminho_completo, 'r') as file:
                    conteudo = file.read()
                caminho_arquivo = caminho_completo.replace(diretorio, '')
                if caminho_arquivo.startswith('/'):
                    caminho_arquivo = caminho_arquivo[1:]
                repo.create_file(caminho_arquivo, f'commit inicial - {caminho_arquivo}', conteudo)

        messagebox.showinfo("Ação", "Upload concluído!")
        btn_resetar_click()
        subwindow.destroy()  # Fecha a janela secundária
        window.deiconify()  # Exibe a janela principal novamente

    def btn_resetar_click():
        nome_var.set('')
        descricao_var.set('')
        diretorio_var.set('')
        publico_var.set(False)
        entry_descricao.delete(1.0, tk.END)

    def btn_voltar_click():
        subwindow.destroy()
        window.deiconify()  # Exibe a janela principal novamente

    def btn_procurar_click():
        diretorio_selecionado = filedialog.askdirectory()
        diretorio_var.set(diretorio_selecionado)

    # Cria os elementos da interface na janela secundária
    lbl_nome = tk.Label(subwindow, text="Nome do repositório:")
    lbl_nome.pack(pady=5)
    entry_nome = tk.Entry(subwindow, textvariable=nome_var)
    entry_nome.pack(pady=5)
    
    
    lbl_descricao = tk.Label(subwindow, text="Descrição do repositório:")
    lbl_descricao.pack(pady=5)
    entry_descricao = tk.Text(subwindow, height=5, width=30)
    entry_descricao.pack()

    lbl_diretorio = tk.Label(subwindow, text="Caminho para o diretório local:")
    lbl_diretorio.pack(pady=5)
    frame_diretorio = tk.Frame(subwindow)
    frame_diretorio.pack(pady=5)

    entry_diretorio = tk.Entry(frame_diretorio, textvariable=diretorio_var)
    entry_diretorio.pack(side=tk.LEFT)

    btn_procurar = tk.Button(frame_diretorio, text="...", command=btn_procurar_click)
    btn_procurar.pack(side=tk.LEFT)

    lbl_publico = tk.Label(subwindow, text="O repositório é público?")
    lbl_publico.pack(pady=5)

    frame_opcoes = tk.Frame(subwindow)
    frame_opcoes.pack(pady=5)

    entry_sim = tk.Radiobutton(frame_opcoes, text="Sim", variable=publico_var, value=True)
    entry_sim.pack(side=tk.LEFT)

    entry_nao = tk.Radiobutton(frame_opcoes, text="Não", variable=publico_var, value=False)
    entry_nao.pack(side=tk.LEFT)

    btn_criar = tk.Button(subwindow, text="Criar", command=btn_criar_click, bg="green", fg="white")
    btn_criar.pack(pady=10)

    btn_resetar = tk.Button(subwindow, text="Resetar", command=btn_resetar_click, bg="yellow")
    btn_resetar.pack(pady=5)

    btn_voltar = tk.Button(subwindow, text="Voltar", command=btn_voltar_click, bg="blue", fg="white")
    btn_voltar.pack(pady=5)



    # Define a janela secundária como filha da janela principal e modal
    subwindow.transient(window)
    subwindow.grab_set()


# Função para excluir um repositório
def excluir_repositorio():
    # Cria a janela secundária
    subwindow = tk.Toplevel(window)
    subwindow.title("Excluir Repositório")

    # Variáveis de entrada
    nome_var = tk.StringVar()

    # Função chamada quando o botão "Excluir" é clicado
    def btn_excluir_click():
        # Obtém o valor da variável de entrada
        nome = nome_var.get()

        # Verifica se o repositório existe
        try:
            repo = g.get_repo(f'{g.get_user().login}/{nome}')
        except Exception:
            messagebox.showerror("Erro", f"O repositório '{nome}' não existe.")
            return

        # Pergunta ao usuário se ele tem certeza que deseja excluir o repositório
        resposta = messagebox.askyesno("Excluir Repositório", "Tem certeza que deseja excluir o repositório?")
        if resposta:
            # Exclui o repositório
            repo.delete()
            messagebox.showinfo("Ação", f"Repositório '{nome}' excluído com sucesso!")
        else:
            messagebox.showinfo("Ação", "Operação de exclusão cancelada.")

        # Reseta a variável de entrada
        nome_var.set('')
        subwindow.destroy()  # Fecha a janela secundária
        window.deiconify()  # Exibe a janela principal novamente

    # Função chamada quando o botão "Cancelar" é clicado
    def btn_cancelar_click():
        subwindow.destroy()
        window.deiconify()  # Exibe a janela principal novamente

    # Cria os elementos da interface na janela secundária
    lbl_nome = tk.Label(subwindow, text="Nome do repositório:")
    lbl_nome.pack(pady=5)

    entry_nome = tk.Entry(subwindow, textvariable=nome_var)
    entry_nome.pack(pady=5)

    btn_excluir = tk.Button(subwindow, text="Excluir", command=btn_excluir_click, bg="red", fg="white")
    btn_excluir.pack(pady=10)

    btn_cancelar = tk.Button(subwindow, text="Cancelar", command=btn_cancelar_click, bg="blue", fg="white")
    btn_cancelar.pack(pady=5)

    # Define a janela secundária como filha da janela principal e modal
    subwindow.transient(window)
    subwindow.grab_set()


# Cria a janela principal
window = tk.Tk()
window.title("GitHub Manager")
window.geometry("200x250")
window.configure(bg="white")

# Função chamada quando o botão "Criar Repositório" é clicado
def btn_criar_repositorio_click():
    criar_repositorio()

# Função chamada quando o botão "Excluir Repositório" é clicado
def btn_excluir_repositorio_click():
    excluir_repositorio()

# Função chamada quando o botão "Sair" é clicado
def btn_sair_click():
    window.destroy()

# Função chamada quando o botão "Alterar Visibilidade" é clicado
def btn_alterar_visibilidade_click():
    # Cria a janela secundária
    subwindow = tk.Toplevel(window)
    subwindow.title("Alterar Visibilidade")

    # Variáveis de entrada
    nome_var = tk.StringVar()
    publico_var = tk.BooleanVar()

    def btn_alterar_click():
        # Obtém os valores das variáveis de entrada
        nome = nome_var.get()
        is_publico = publico_var.get()

        # Verifica se o repositório existe
        try:
            repo = g.get_repo(f'{g.get_user().login}/{nome}')
        except Exception:
            messagebox.showerror("Erro", f"O repositório '{nome}' não existe.")
            return

        # Altera a visibilidade do repositório
        repo.edit(private=not is_publico)

        tipo_repositorio = "público" if is_publico else "privado"
        messagebox.showinfo("Ação", f"Visibilidade do repositório '{nome}' alterada para: {tipo_repositorio}")

        # Reseta as variáveis de entrada
        nome_var.set('')
        publico_var.set(False)
        subwindow.destroy()  # Fecha a janela secundária
        window.deiconify()  # Exibe a janela principal novamente

    def btn_cancelar_click():
        subwindow.destroy()
        window.deiconify()  # Exibe a janela principal novamente

    # Cria os elementos da interface na janela secundária
    lbl_nome = tk.Label(subwindow, text="Nome do repositório:")
    lbl_nome.pack(pady=5)

    entry_nome = tk.Entry(subwindow, textvariable=nome_var)
    entry_nome.pack(pady=5)

    lbl_publico = tk.Label(subwindow, text="O repositório deve ser público?")
    lbl_publico.pack(pady=5)

    entry_sim = tk.Radiobutton(subwindow, text="Sim", variable=publico_var, value=True)
    entry_sim.pack(pady=5)

    entry_nao = tk.Radiobutton(subwindow, text="Não", variable=publico_var, value=False)
    entry_nao.pack(pady=5)

    btn_alterar = tk.Button(subwindow, text="Alterar", command=btn_alterar_click, bg="green", fg="white")
    btn_alterar.pack(pady=10)

    btn_cancelar = tk.Button(subwindow, text="Cancelar", command=btn_cancelar_click, bg="blue", fg="white")
    btn_cancelar.pack(pady=5)

 
# Cria os elementos da interface na janela principal
btn_criar_repositorio = tk.Button(window, text="Criar Repositório", command=btn_criar_repositorio_click)
btn_criar_repositorio.pack(pady=10)

btn_excluir_repositorio = tk.Button(window, text="Excluir Repositório", command=btn_excluir_repositorio_click)
btn_excluir_repositorio.pack(pady=10)

btn_alterar_visibilidade = tk.Button(window, text="Alterar Visibilidade", command=btn_alterar_visibilidade_click)
btn_alterar_visibilidade.pack(pady=10)

btn_sair = tk.Button(window, text="Sair", command=btn_sair_click, bg="red", fg="white")
btn_sair.pack(pady=10)

# Inicia a janela principal
window.mainloop()
