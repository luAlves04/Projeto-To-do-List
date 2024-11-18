import tkinter as tk
# importando do tkinter a função messagebox
from tkinter import messagebox

# função pra quando apertar o botão
def addTarefa():
    items = caixaTexto.get()
    if items != "":
        listaTarefas.insert(tk.END, items)
        caixaTexto.delete(0, tk.END)
    else:
        messagebox.showerror("Inválido", "Escreva algo para ser adicionado")

def concluirTarefa():
    concluido = listaTarefas.curselection()

    if concluido:
        items = listaTarefas.get(concluido)
        listaTarefas.delete(concluido)
        listaTarefas.insert(tk.END, f"{items} (Concluída)")
        concluido == True
    else:
        messagebox.showerror("Inválido", "Escolha a tarefa para concluir")

    if "(Concluída)" in items:
        
        

def removerTarefa():
    deletar = listaTarefas.curselection()
    
    if deletar:
        items = listaTarefas.get(deletar)
        listaTarefas.delete(deletar)
        messagebox.showinfo("Deletar", "Tarefa deletada com sucesso")
    else:
      messagebox.showerror("Inválido", "Escolha a tarefa para deletar")


# configurações da janela
janela = tk.Tk()
janela.title("To-Do List")
janela.geometry("600x700")

# configurações do rótulo
rotulo = tk.Label(janela, text="Gerenciador de Tarefas")
rotulo.pack(pady=20)

listaTarefas = tk.Listbox(janela, height=25, width=80, font=("Arial", 9), fg="black")
listaTarefas.pack(pady=0)

caixaTexto = tk.Entry(janela, width=50)
caixaTexto.place(x=140,y=475)

# configurações do botão
botaoTarefa = tk.Button(janela, text="Adicionar Tarefa", command=addTarefa).place(x=240, y=500)
botaoConcluido = tk.Button(janela, text="Concluir Tarefa", command=concluirTarefa).place(x=242, y=540)
botaoRemover = tk.Button(janela, text="Remover Tarefa", command=removerTarefa).place(x=242, y=580)

janela.mainloop()