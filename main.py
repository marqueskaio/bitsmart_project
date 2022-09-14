import speech_recognition as sr


import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-4T4GLKV;"
    "Database=pie_dream;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem sucedida")


rec = sr.Recognizer()

with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)
    print('pode falar que eu vou gravar')
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)

cursor = conexao.cursor()
comando = ("""INSERT INTO sonhos(texto) VALUES ('{}')""").format(texto)

cursor.execute(comando)
cursor.commit()