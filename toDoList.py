import tkinter as tk
# importando do tkinter a função messagebox
from tkinter import messagebox

# função para quando apertar o botão de adicionar tarefa
def addTarefa():
    items = caixaTexto.get() # recebe o que tem na Entry

    if items != "": 
        listaTarefas.insert(tk.END, items) # adiciona a tarefa na listbox e o coloca no ultimo indice da lista
        caixaTexto.delete(0, tk.END) # remove o que tem escrito na Entry do começo ao fim
    else:
        messagebox.showerror("Inválido", "Escreva uma tarefa para ser adicionado") # erro se não foi adicionado nada

# função para quando apertar o botão de concluir tarefa
def concluirTarefa():
    concluido = listaTarefas.curselection() # pega o que o usuário selecionou com o cursor

    if concluido:
        items = listaTarefas.get(concluido) # recebe o que o usuário selecionou e guarda na variavel items
        listaTarefas.delete(concluido) # deleta o que foi selecionado
        listaTarefas.insert(tk.END, f"{items} (Concluída)") # adiciona o item junto com a string "(Concluída)"
    else:
        messagebox.showerror("Inválido", "Escolha a tarefa para concluir") # erro se não selecionar nenhuma tarefa

    # impedir repetições da string "(Concluída)"
    if "(Concluída)" in items: 
        messagebox.showerror("Inválido", "Tarefa já concluída")
        listaTarefas.delete(concluido) # deleta o que foi selecionado
        listaTarefas.insert(tk.END, f"{items}") # adiciona o item novamente que ja esta armazenado com a string "(Concluída)"
        
        
# função para quando apertar o botão de remover tarefa
def removerTarefa():
    deletar = listaTarefas.curselection()
    
    if deletar:
        items = listaTarefas.get(deletar) 
        listaTarefas.delete(deletar) # apaga o que foi selecionado
        messagebox.showinfo("Deletar", "Tarefa deletada com sucesso")
    else:
      messagebox.showerror("Inválido", "Escolha a tarefa para apagar") # erro se não selecionar nenhuma tarefa 


# configurações da janela
janela = tk.Tk()
janela.title("To-Do List")
janela.geometry("600x700")
janela.configure(background="#E0A757")


# configurações do rótulo
rotulo = tk.Label(janela, text="Gerenciador de Tarefas", font=("Arial", 14, "bold"), background="#E0A757")
rotulo.pack(pady=20)

# configurações da listbox
listaTarefas = tk.Listbox(janela, height=25, width=80, font=("Arial", 9), fg="black", foreground="#0A0A24", relief="flat")
listaTarefas.pack(pady=0)

# configurações da Entry
caixaTexto = tk.Entry(janela, width=50, bg="#BBBCC3", font=("Arial", "11"), fg = "#0A0A24", relief="ridge")
caixaTexto.place(x=105,y=475)

# configurações dos botões
botaoTarefa = tk.Button(janela, text="Adicionar Tarefa", command=addTarefa, bg="#46B45E", font=("Arial", 10, "bold")).place(x=237, y=500)
botaoConcluido = tk.Button(janela, text="Concluir Tarefa", command=concluirTarefa, bg="#5A5DF8", font=("Arial", 10, "bold")).place(x=240, y=540)
botaoRemover = tk.Button(janela, text="Remover Tarefa", command=removerTarefa, bg="#B44646", font=("Arial", 10, "bold")).place(x=238, y=580)


janela.mainloop()

