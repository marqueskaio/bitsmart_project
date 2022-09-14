import tkinter as tk
import sqlite3
import pandas as pd

# conexao = sqlite3.connect('banco_serviços.db')0
#
# c = conexao.cursor()
#
# c.execute(''' CREATE TABLE serviços (
#     data text,
#     marca text,
#     modelo text,
#     serviço text,
#     total text,
#     peça text
#     )
# ''')
#
# conexao.commit()
#
# conexao.close()

def cadastrar_serviço():
    conexao = sqlite3.connect('banco_serviços.db')

    c = conexao.cursor()

    c.execute(" INSERT INTO serviços VALUES (:data, :marca, :modelo, :serviço, :total, :peça)",
                {
                    'data': entry_data.get(),
                    'marca': entry_marca.get(),
                    'modelo': entry_modelo.get(),
                    'serviço': entry_serviço.get(),
                    'total': entry_total.get(),
                    'peça': entry_peça.get()
                }
                )

    conexao.commit()

    conexao.close()

    entry_data.delete(0, "end")
    entry_marca.delete(0, "end")
    entry_modelo.delete(0, "end")
    entry_serviço.delete(0, "end")
    entry_total.delete(0, "end")
    entry_peça.delete(0, "end")

def exportar_serviços():
    conexao = sqlite3.connect('banco_serviços.db')

    c = conexao.cursor()

    c.execute("SELECT *, oid FROM serviços")
    serviços_cadastrados = c.fetchall()
    serviços_cadastrados = pd.DataFrame(serviços_cadastrados, columns=['data', 'marca', 'modelo', 'serviço', 'total', 'id_banco', ''])
    serviços_cadastrados.to_excel('banco_serviços.xlsx')

    conexao.commit()

    conexao.close()




janela = tk.Tk()
janela.title('ferramenta de cadastro de serviços')

# Labels:

label_data = tk.Label(janela, text='data')
label_data.grid(row=0, column=0, padx=10, pady=10)

label_marca = tk.Label(janela, text='marca')
label_marca.grid(row=1, column=0, padx=10, pady=10)

label_modelo = tk.Label(janela, text='modelo')
label_modelo.grid(row=2, column=0, padx=10, pady=10)

label_serviço = tk.Label(janela, text='serviço')
label_serviço.grid(row=3, column=0, padx=10, pady=10)

label_total = tk.Label(janela, text='total')
label_total.grid(row=4, column=0, padx=10, pady=10)

label_peça = tk.Label(janela, text='peça')
label_peça.grid(row=5, column=0, padx=10, pady=10)



# ENTRYS:

entry_data = tk.Entry(janela, text='data', width=30)
entry_data.grid(row=0, column=1, padx=10, pady=10)

entry_marca = tk.Entry(janela, text='marca', width=30)
entry_marca.grid(row=1, column=1, padx=10, pady=10)

entry_modelo = tk.Entry(janela, text='modelo', width=30)
entry_modelo.grid(row=2, column=1, padx=10, pady=10)

entry_serviço = tk.Entry(janela, text='serviço', width=30)
entry_serviço.grid(row=3, column=1, padx=10, pady=10)

entry_total = tk.Entry(janela, text='total', width=30)
entry_total.grid(row=4, column=1, padx=10, pady=10)

entry_peça = tk.Entry(janela, text='peça', width=30)
entry_peça.grid(row=5, column=1, padx=10, pady=10)



#botões:

botao_cadastrar = tk.Button(janela, text='cadastrar serviço', command = cadastrar_serviço)
botao_cadastrar.grid(row=7, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

botao_exportar = tk.Button(janela, text='exportar base de serviços', command = exportar_serviços)
botao_exportar.grid(row=8, column=0, padx=10, pady=10, columnspan=2, ipadx=80)


janela.mainloop()