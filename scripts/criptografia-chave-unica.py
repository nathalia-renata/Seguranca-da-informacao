from cryptography.fernet import Fernet

def demonstracao_simetrica():
    print("--- Iniciando Criptografia Simétrica ---")
    
    chave = Fernet.generate_key()
    ferramenta = Fernet(chave)
    
    mensagem = b"Texto confidencial que nao deve ser lido."
    
    token_cifrado = ferramenta.encrypt(mensagem)
    print(f"Mensagem cifrada: {token_cifrado}")
    
    mensagem_recuperada = ferramenta.decrypt(token_cifrado)
    print(f"Mensagem original: {mensagem_recuperada.decode()}")

demonstracao_simetrica()