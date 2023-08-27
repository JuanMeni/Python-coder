
import json

def verificar_cuenta():
    try:
        with open("Lista_de_usuarios.json", "r") as file:
            usuarios_registrados = json.load(file)
    except FileNotFoundError:
        # Si el archivo no existe, inicializamos la lista de usuarios
        usuarios_registrados = []

    while True:
        opcion = input("¿Tienes una cuenta registrada? (s/n): ")
        if opcion.lower() == 's':
            iniciar_sesion(usuarios_registrados)
            break
        elif opcion.lower() == 'n':
            usuario_nuevo = crea_usuario()
            usuarios_registrados.append(usuario_nuevo)
            guardar_en_archivo(usuarios_registrados)
            print("Usuario registrado exitosamente.")
            iniciar_sesion(usuarios_registrados)
            break
        else:
            print("Opción inválida. Por favor, responda 's' o 'n'.")

def iniciar_sesion(usuarios_registrados):
    while True:
        print("Bienvenido al login. ")
        usuario = input("Ingrese su nombre de usuario para login: ")
        contraseña = input("Ingrese su contraseña para login: ")

        for usuario_info in usuarios_registrados:
            if usuario_info["usuario"] == usuario and usuario_info["contraseña"] == contraseña:
                print("Inicio de sesión exitoso.")
                option = input("¿Desea ver la lista de usuarios? (s/n): ")
                if option.lower()== "s":
                    mostrar_archivo_json()
                elif option.lower()== "n":
                    print('Hasta luego.')
            else: 
                 print("Usuario inexistente o credenciales incorrectas. Intente nuevamente.")
        break

def crea_usuario():
    while True:
        usuario = input("Ingrese su nombre de usuario: ")
        if len(usuario) >= 6:
            break
        else:
            print("El usuario debe contener al menos 6 dígitos")

    while True:
        contraseña = input("Ingrese su contraseña: ")
        if valida_contraseña(contraseña):
            rcontraseña = input("Vuelva a ingresar la contraseña: ")
            if contraseña == rcontraseña:
                break
            else:
                print("Las contraseñas no coinciden. Inténtelo nuevamente.")
        else:
            print("La contraseña debe tener al menos 8 dígitos, una mayúscula, una minúscula y un número.")

    persona = {
        "usuario": usuario,
        "contraseña": contraseña
    }

    return persona

# Verificamos que la contraseña cumpla con los criterios

def valida_contraseña(contraseña):
    if len(contraseña) < 8:
        return False

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True

    return tiene_mayuscula and tiene_minuscula and tiene_numero


def guardar_en_archivo(usuarios_registrados):
    with open("Lista_de_usuarios.json", "w") as file:
        json.dump(usuarios_registrados, file, indent=4)

def mostrar_archivo_json():
    try:
        with open("Lista_de_usuarios.json", "r") as file:
            usuarios_registrados = json.load(file)
            print("Contenido del archivo JSON:")
            print(json.dumps(usuarios_registrados, indent=4))
    except FileNotFoundError:
        print("El archivo JSON no existe o está vacío.")

if __name__ == "__main__":
    verificar_cuenta()
    
