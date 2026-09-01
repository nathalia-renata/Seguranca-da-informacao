import time
from pynput import keyboard

ARQUIVO_LOG = "log_teclas.txt"

def salvar_em_arquivo(tecla: str) -> None:
    with open(ARQUIVO_LOG, "a", encoding="utf-8") as arquivo:
        arquivo.write(tecla + "\n")

def ao_pressionar(tecla) -> None:
    try:
        salvar_em_arquivo(tecla.char)
        print(f"Tecla registrada: {tecla.char}")
    except AttributeError:
        salvar_em_arquivo(str(tecla))
        print(f"Tecla especial registrada: {tecla}")

def iniciar_captura(limite: int = 20) -> None:
    print("Captura de teclas iniciada (Professor).")
    
    contador = {"valor": 0}
    
    def ao_pressionar_limitado(tecla):
        ao_pressionar(tecla)
        contador["valor"] += 1
        if contador["valor"] >= limite:
            return False
            
    with keyboard.Listener(on_press=ao_pressionar_limitado) as listener:
        listener.join()
        
    print("Captura finalizada.")

if __name__ == "__main__":
    iniciar_captura()