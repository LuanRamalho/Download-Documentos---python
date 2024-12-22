import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import os

def download_file():
    url = url_entry.get()
    if not url.strip():
        messagebox.showwarning("Entrada Inválida", "Por favor, insira um link válido.")
        return

    try:
        # Selecionar diretório para salvar o arquivo
        save_path = filedialog.askdirectory(title="Selecione o diretório para salvar o arquivo")
        if not save_path:
            return

        # Realizar o download
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Extraindo o nome do arquivo do link
        file_name = url.split("/")[-1]
        if not file_name:
            file_name = "documento_baixado"
        
        file_path = os.path.join(save_path, file_name)
        
        # Salvar o arquivo
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        messagebox.showinfo("Download Concluído", f"Arquivo salvo em:\n{file_path}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro no Download", f"Não foi possível baixar o arquivo.\n\n{str(e)}")

# Configurar a janela principal
root = tk.Tk()
root.title("Downloader de Documentos")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="#E3F2FD")

# Título
title_label = tk.Label(
    root, 
    text="Downloader de Documentos", 
    font=("Arial", 16, "bold"), 
    bg="#2196F3", 
    fg="white", 
    pady=10
)
title_label.pack(fill=tk.X)

# Instruções
instructions_label = tk.Label(
    root, 
    text="Insira o link do documento que deseja baixar:", 
    font=("Arial", 12), 
    bg="#E3F2FD", 
    fg="#0D47A1"
)
instructions_label.pack(pady=10)

# Campo de entrada para URL
url_entry = tk.Entry(root, font=("Arial", 12), width=40, bd=2, relief=tk.GROOVE)
url_entry.pack(pady=5)

# Botão para realizar o download
download_button = tk.Button(
    root, 
    text="Baixar Documento", 
    font=("Arial", 12, "bold"), 
    bg="#4CAF50", 
    fg="white", 
    relief=tk.RAISED, 
    command=download_file
)
download_button.pack(pady=20)

# Executar a aplicação
root.mainloop()
