import socket
from datetime import datetime

def motor_scan(alvo):
    try:
        ip_alvo = socket.gethostbyname(alvo)
    except:
        print(f"Erro: Não consegui encontrar o servidor {alvo}")
        return
        
    print("-" * 50)
    print(f"Verificando o alvo: {ip_alvo}")
    print(f"Início da varredura: {datetime.now()}")
    print("-" * 50)
    
    portas = [20, 21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306, 3389, 8080]
    
    try:
        for porta in portas:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            resultado = sock.connect_ex((ip_alvo, porta))
            
            if resultado == 0:
                try:
                    servico = socket.getservbyport(porta)
                except:
                    servico = "Desconhecido"
                print(f"[+] Porta {porta} aberta - Serviço: {servico}")
            sock.close()
            
    except KeyboardInterrupt:
        print("\nVarredura interrompida.")
    except socket.error:
        print("\nErro de conexão com o servidor.")
        
    print("-" * 50)
    print("Fim da execução.")

if __name__ == "__main__":
    endereco = input("Digite o IP ou site para escanear: ")
    motor_scan(endereco)