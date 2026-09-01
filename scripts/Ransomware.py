import os
from cryptography.fernet import Fernet

def cifrar_arquivo_txt(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print("Erro: Arquivo não encontrado.")
        return
        
    chave = Fernet.generate_key()
    fernet = Fernet(chave)
    
    try:
        with open(caminho_arquivo, 'rb') as file:
            dados_originais = file.read()
            
        dados_encriptados = fernet.encrypt(dados_originais)
        novo_nome = caminho_arquivo + ".secreto"
        
        with open(novo_nome, 'wb') as file:
            file.write(dados_encriptados)
            
        print(f"Sucesso! O arquivo {novo_nome} foi criado.")
        print(f"ATENÇÃO - Guarde esta chave para decifrar: {chave.decode()}")
        
    except Exception as e:
        print(f"Ocorreu um erro durante o processo: {e}")

arquivo_teste = "relatorio_final.txt"
with open(arquivo_teste, "w") as f:
    f.write("Conteúdo extremamente sensível do trabalho ABNT.")
    
cifrar_arquivo_txt(arquivo_teste)