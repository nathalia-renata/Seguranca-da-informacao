from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def demonstracao_assimetrica():
    print("--- Iniciando Criptografia Assimétrica ---")
    
    chave_privada = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    chave_publica = chave_privada.public_key()
    
    texto = b"Este dado viajou de forma segura."
    
    cifrado = chave_publica.encrypt(
        texto,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    decifrado = chave_privada.decrypt(
        cifrado,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    print(f"Texto recuperado com sucesso: {decifrado.decode()}")

demonstracao_assimetrica()