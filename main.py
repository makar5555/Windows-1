import os
import sys
import random
import calendar
import requests
from datetime import datetime
from bs4 import BeautifulSoup

# Almacenamiento de usuarios
usuarios = {
    "admin": "admin"
}

# Usuario autenticado
usuario_actual = None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    clear_screen()
    print(f"Bienvenido, {usuario_actual}!")
    print("****************************")
    print("*  Simulador de Windows 1.0  *")
    print("****************************")
    print("1. 📝 Bloc de notas")
    print("2. 🕒 Reloj")
    print("3. ➗ Calculadora")
    print("4. 🎲 Adivina el Número (Juego)")
    print("5. 📅 Calendario")
    print("6. 🌐 Internet")
    print("7. 🎨 Paint")
    print("8. 💾 Guardar Archivo")
    print("9. ⚙️ Ajustes")
    print("10. 🔒 Cerrar sesión")
    print("****************************")

def bloc_de_notas():
    clear_screen()
    print("📝 ************ Bloc de Notas ************")
    print("Escribe tu texto (escribe 'exit' para salir y guardar):")
    texto = []
    while True:
        text = input()
        if text.lower() == 'exit':
            break
        texto.append(text)

    if texto:
        save_option = input("¿Quieres guardar el texto en un archivo? (s/n): ").lower()
        if save_option == 's':
            filename = input("Introduce el nombre del archivo (sin extensión): ")
            with open(f"{filename}.txt", "w") as file:
                file.write("\n".join(texto))
            print(f"Texto guardado en {filename}.txt")

def reloj():
    import time
    clear_screen()
    print("🕒 ************ Reloj ************")
    print("Presiona Ctrl+C para volver al menú.")
    try:
        while True:
            clear_screen()
            print("🕒 ************ Reloj ************")
            print(time.strftime("%H:%M:%S"))
            time.sleep(1)
    except KeyboardInterrupt:
        pass

def calculadora():
    clear_screen()
    print("➗ ************ Calculadora ************")
    print("Escribe tu operación matemática (o 'exit' para salir):")
    while True:
        expression = input()
        if expression.lower() == 'exit':
            break
        try:
            result = eval(expression)
            print(f"Resultado: {result}")
        except Exception as e:
            print(f"Error: {e}")

def adivina_el_numero():
    clear_screen()
    print("🎲 ************ Adivina el Número ************")
    print("He elegido un número entre 1 y 100. ¿Puedes adivinar cuál es?")
    
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        intento = input("Introduce tu intento (o 'exit' para salir): ")
        if intento.lower() == 'exit':
            break
        try:
            intento = int(intento)
            intentos += 1
            if intento < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

def mostrar_calendario():
    clear_screen()
    print("📅 ************ Calendario ************")
    now = datetime.now()
    year = now.year
    month = now.month
    print(calendar.month(year, month))
    input("Presiona Enter para volver al menú.")

def internet():
    clear_screen()
    print("🌐 ************ Internet ************")
    query = input("Introduce tu búsqueda: ")
    response = requests.get(f"https://www.google.com/search?q={query}")
    soup = BeautifulSoup(response.text, 'html.parser')

    print("Resultados de la búsqueda:")
    for i, result in enumerate(soup.find_all('h3')[:5], 1):
        print(f"{i}. {result.get_text()}")
        print(result.find_parent('a')['href'])
        print()

    input("Presiona Enter para volver al menú.")

def paint():
    clear_screen()
    width, height = 20, 10
    canvas = [[' ' for _ in range(width)] for _ in range(height)]
    x, y = 0, 0

    def print_canvas():
        clear_screen()
        print("🎨 ************ Paint ************")
        for row in canvas:
            print(''.join(row))
        print(f"Posición del cursor: ({x}, {y})")
        print("Usa las teclas W/A/S/D para mover, P para pintar, y Q para salir.")

    while True:
        print_canvas()
        command = input().lower()
        if command == 'q':
            break
        elif command == 'w' and y > 0:
            y -= 1
        elif command == 's' and y < height - 1:
            y += 1
        elif command == 'a' and x > 0:
            x -= 1
        elif command == 'd' and x < width - 1:
            x += 1
        elif command == 'p':
            canvas[y][x] = '#'

def guardar_archivo():
    clear_screen()
    print("💾 ************ Guardar Archivo ************")
    contenido = []
    print("Escribe tu texto (Escribe 'exit' para salir y guardar):")
    while True:
        linea = input()
        if linea.lower() == 'exit':
            break
        contenido.append(linea)

    if contenido:
        nombre_archivo = input("Introduce el nombre del archivo (sin extensión): ")
        with open(f"{nombre_archivo}.txt", "w") as archivo:
            archivo.write("\n".join(contenido))
        print(f"Texto guardado en {nombre_archivo}.txt")

def cambiar_contraseña():
    global usuarios, usuario_actual
    clear_screen()
    print("⚙️ ************ Cambiar Contraseña ************")
    while True:
        contraseña_actual = input("Introduce tu contraseña actual: ")
        if usuarios[usuario_actual] == contraseña_actual:
            nueva_contraseña = input("Introduce tu nueva contraseña: ")
            confirmar_contraseña = input("Confirma tu nueva contraseña: ")
            if nueva_contraseña == confirmar_contraseña:
                usuarios[usuario_actual] = nueva_contraseña
                print("Contraseña cambiada exitosamente.")
                break
            else:
                print("Las contraseñas no coinciden. Inténtalo de nuevo.")
        else:
            print("Contraseña actual incorrecta. Inténtalo de nuevo.")
        if input("¿Quieres intentar de nuevo? (s/n): ").lower() != 's':
            break

def login():
    global usuario_actual
    clear_screen()
    print("************ Iniciar Sesión ************")
    while True:
        nombre = input("Nombre de usuario: ")
        contraseña = input("Contraseña: ")
        if nombre in usuarios and usuarios[nombre] == contraseña:
            usuario_actual = nombre
            break
        else:
            print("Usuario o contraseña incorrectos. Inténtalo de nuevo.")

def registrar():
    global usuarios
    clear_screen()
    print("************ Registrar Usuario ************")
    while True:
        nombre = input("Elige un nombre de usuario: ")
        if nombre in usuarios:
            print("El nombre de usuario ya existe. Elige otro.")
        else:
            contraseña = input("Elige una contraseña: ")
            usuarios[nombre] = contraseña
            print("Usuario registrado exitosamente.")
            break

def cerrar_sesion():
    global usuario_actual
    usuario_actual = None

def main():
    while True:
        if not usuario_actual:
            clear_screen()
            print("1. Iniciar sesión")
            print("2. Registrar usuario")
            print("3. Salir")
            choice = input("Selecciona una opción: ")
            if choice == '1':
                login()
            elif choice == '2':
                registrar()
            elif choice == '3':
                sys.exit()
            else:
                print("Opción no válida, por favor intenta de nuevo.")
        else:
            print_menu()
            choice = input("Selecciona una opción: ")
            if choice == '1':
                bloc_de_notas()
            elif choice == '2':
                reloj()
            elif choice == '3':
                calculadora()
            elif choice == '4':
                adivina_el_numero()
            elif choice == '5':
                mostrar_calendario()
            elif choice == '6':
                internet()
            elif choice == '7':
                paint()
            elif choice == '8':
                cambiar_contraseña()
            elif choice == '9':
                cerrar_sesion()
            else:
                print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()