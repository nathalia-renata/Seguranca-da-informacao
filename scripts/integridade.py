import hashlib

def gerar_assinatura_sha256(texto):
    texto_bytes = texto.encode('utf-8')
    hash_objeto = hashlib.sha256(texto_bytes)
    return hash_objeto.hexdigest()

entrada = "Segurança da Informação na Prática"
print(f"Entrada: {entrada}")
print(f"Hash: {gerar_assinatura_sha256(entrada)}")