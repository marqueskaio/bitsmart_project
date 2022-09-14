import tkinter as tk
import sqlite3
import pandas as pd

#1 Criar banco de dados
#2 Criar tabela
#3 Comentar a criação do banco
#4 Criar a interface gráfica
#        labels, campos, botão, botão exportar
#5 integrar com banco de dados
#        cadastrar (INSERT INTO)
#        exportar (SELECT*)
#        PANDAS

# conexao = sqlite3.connect('banco_clientes1.db')
#
# c = conexao.cursor()
#
# c.execute(''' CREATE TABLE clientes1 (
#     nome text,
#     email text,
#     telefone text,
#     cpf text
#     )
# ''')
#
# conexao.commit()
#
# conexao.close()


def cadastrar_cliente():
    conexao = sqlite3.connect('banco_clientes1.db')

    c = conexao.cursor()

    c.execute(" INSERT INTO clientes1 VALUES (:nome, :email, :telefone, :cpf)",
                {
                    'nome':entry_nome.get(),
                    'email':entry_email.get(),
                    'telefone':entry_telefone.get(),
                    'cpf':entry_cpf.get()
                }
                )

    conexao.commit()

    conexao.close()

    entry_nome.delete(0, "end")
    entry_email.delete(0, "end")
    entry_telefone.delete(0, "end")
    entry_cpf.delete(0, "end")

def exportar_clientes():
    conexao = sqlite3.connect('banco_clientes1.db')

    c = conexao.cursor()

    c.execute("SELECT *, oid FROM clientes1")
    clientes_cadastrados = c.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['nome', 'email', 'telefone', 'id_banco', ''])
    clientes_cadastrados.to_excel('banco_clientes1.xlsx')

    conexao.commit()

    conexao.close()




janela = tk.Tk()
janela.title('ferramenta de cadastro de clientes')

# Labels:

label_nome = tk.Label(janela, text='nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='email')
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=10)

label_cpf = tk.Label(janela, text='cpf')
label_cpf.grid(row=4, column=0, padx=10, pady=10)


# ENTRYS:

entry_nome = tk.Entry(janela, text='nome', width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, text='email', width=30)
entry_email.grid(row=2, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, text='telefone', width=30)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

entry_cpf = tk.Entry(janela, text='cpf', width=30)
entry_cpf.grid(row=4, column=1, padx=10, pady=10)



#botões:

botao_cadastrar = tk.Button(janela, text='cadastrar cliente', command = cadastrar_cliente)
botao_cadastrar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

botao_exportar = tk.Button(janela, text='exportar base de clientes', command = exportar_clientes)
botao_exportar.grid(row=6, column=0, padx=10, pady=10, columnspan=2, ipadx=80)


janela.mainloop()