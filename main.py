import os
import random
import string
import time
import ctypes

try:
    import requests
except ImportError:
    install_requests = input(
        f"El módulo requests no está instalado, ¿quieres instalarlo? [Y/n]")
    if install_requests == "n":
        exit()
    else:
        os.system(
            f"{'py -3' if os.name == 'nt' else 'python3'} -m pip install requests")

class PSNCodeGenerator:
    def __init__(self):
        self.fileName = "PSN Codes.txt"

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Generador y Verificador de Códigos PSN - Creado por [TU NOMBRE]")

        else:
            print(f'\33]0;Generador y Verificador de Códigos PSN - Creado por [TU NOMBRE]\a', end='', flush=True)

        print("""
Generador Rápido de Códigos PSN""")
        time.sleep(2)
        self.slowType("Creado por [TU NOMBRE]", .02)
        time.sleep(1)
        self.slowType("\n¿Cuántos códigos deseas generar y verificar?: ", .02, newLine = False)

        num = int(input(''))

        self.slowType("\nPor favor, ingresa la URL del webhook de Discord o deja en blanco para continuar aquí: ", .02, newLine = False)
        url = input('')
        webhook = url if url != "" else None

        valid = []
        invalid = 0

        for i in range(num):
            try:
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits,
                    k = 10
                ))
                url = f"https://store.playstation.com/store/api/chihiro/00_09_000/container/US/en/999/{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except Exception as e:
                print(f" Error | {url} ")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(f"Generador y Verificador de Códigos PSN - {len(valid)} Válidos | {invalid} Inválidos - Creado por [TU NOMBRE]")
                print("")

            else:
                print(f'\33]0;Generador y Verificador de Códigos PSN - {len(valid)} Válidos | {invalid} Inválidos - Creado por [TU NOMBRE]\a', end='', flush=True)

        print(f"""
Resultados:
 Códigos válidos: {len(valid)}
 Códigos inválidos: {invalid}
 Códigos PSN válidos: {', '.join(valid)}""")

        input("\n¡Fin del programa! Presiona Enter 5 veces para cerrarlo.")
        [input(i) for i in range(4,0,-1)]

    def slowType(self, text, speed, newLine = True):
        for i in text:
            print(i, end = "", flush = True)
            time.sleep(speed)
        if newLine:
            print()

    def quickChecker(self, url, notify = None):
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f" Válido | {url} ", flush=True, end="" if os.name == 'nt' else "\n")
            with open("PSN Codes.txt", "w") as file:
                file.write(url)
            if notify is not None:
                DiscordWebhook(
                    url = notify,
                    content = f"¡Código PSN válido detectado! @everyone \n{url}"
                ).execute()
            return True
        else:
            print(f" Inválido | {url} ", flush=True, end="" if os.name == 'nt' else "\n")
            return False

if __name__ == '__main__':
    Generator = PSNCodeGenerator()
    Generator.main()
