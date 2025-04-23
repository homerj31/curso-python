import os

def limpiar_pantalla():
    """
    Limpia la pantalla de la consola.
    Funciona tanto en Windows como en sistemas Unix (Linux, macOS).
    """
    # Comando para limpiar la pantalla
    # "cls" para Windows y "clear" para Unix/Linux/Mac
    os.system("cls" if os.name == "nt" else "clear")