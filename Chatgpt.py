import tkinter as tk
from tkinter import ttk

# Dados
code = [100, 101, 102, 103, 104, 105]
value = [1.20, 1.30, 1.50, 1.20, 1.30, 1.00]
lanche = ["Cachorro quente", "Bauru simples", "Bauru com ovo", "Hambúrguer", "Cheeseburger", "Refrigerante"]

root = tk.Tk()
root.title("Pedido de Lanches")
root.geometry("400x400")

# Label de instrução
label = tk.Label(root, text="Selecione o lanche e digite a quantidade", pady=10)
label.pack()

# Combobox e entry
combo = ttk.Combobox(root, values=lanche, state="readonly")
combo.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

# Listbox para mostrar o histórico de pedidos
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

label9 = tk.Label(text="", relief="solid", background="white")
label9.pack()
compras = []
lanches_selecionados = set()

def make_total():
    try:
        qtd = int(entry1.get())
        if qtd <= 0:
            raise ValueError
    except ValueError:
        label.config(text="Digite uma quantidade válida (número inteiro > 0).", fg="red")
        return

    lanche_selecionado = combo.get()
    if not lanche_selecionado:
        label.config(text="Selecione um lanche.", fg="red")
        return

    if lanche_selecionado in lanches_selecionados:
        label.config(text="Você já pediu isso antes", fg="red")
        return

    lanches_selecionados.add(lanche_selecionado)
    index = lanche.index(lanche_selecionado)
    preco = value[index]
    total = preco * qtd

    compras.append({
        'lanche': lanche_selecionado, 'qtd': qtd, 'preco': preco, 'total': total
    })

    listbox.insert(
        tk.END,
        f"{lanche_selecionado} x{qtd} — R$ {total:.2f}"
    )

    label.config(text=f"Pedido adicionado: {lanche_selecionado} x{qtd}", fg="green")
    entry1.delete(0, tk.END)

def fazer_compra():
    if not compras:
        label9.config(text="Nenhum pedido foi feito ainda.", fg="red")
        return

    resumo = "Lanche               Qtd    Valor     Total\n"
    resumo += "-" * 40 + "\n"
    total_geral = 0

    for item in compras:
        lanche_nome = item['lanche'][:18]
        qtd = item['qtd']
        preco = item['preco']
        total = item['total']
        resumo += f"{lanche_nome:<18} {qtd:^5}  R$ {preco:>5.2f}  R$ {total:>6.2f}\n"
        total_geral += total

    resumo += "-" * 40 + "\n"
    resumo += f"{'Total Geral':<27} R$ {total_geral:>6.2f}"

    label9.config(text=resumo, justify="left", font=("Courier", 10), fg="black", anchor="w")

def deletar_item():
    selecionado = listbox.curselection()
    if not selecionado:
        label.config(text="Selecione um item para deletar.", fg="red")
        return

    index = selecionado[0]
    item = compras[index]
    lanche_removido = item['lanche']

    # Remove dos dados
    del compras[index]
    lanches_selecionados.remove(lanche_removido)

    # Remove do Listbox
    listbox.delete(index)
    label.config(text=f"{lanche_removido} removido do pedido.", fg="blue")

# Botões
button = tk.Button(root, text="Fazer Pedido", command=make_total)
button.pack(pady=5)

button2 = tk.Button(root, text="Fazer Compra", command=fazer_compra)
button2.pack(pady=5)

botao_deletar = tk.Button(root, text="Deletar item selecionado", command=deletar_item)
botao_deletar.pack(pady=5)

root.mainloop()
