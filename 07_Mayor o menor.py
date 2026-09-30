# PRÁCTICA 7
# Programa que muestra si una persona es mayor o menor de edad
# usando números al azar.
# Botón B

edad = 0

def on_button_pressed_b():
    global edad
    edad = randint(1, 30)
    basic.show_number(edad)
    basic.pause(1000)

    if edad >= 18:
        basic.show_string("MAYOR DE EDAD")
        basic.pause(500)
    else:
        basic.show_string("MENOR DE EDAD")
        basic.pause(500)

    basic.clear_screen()

input.on_button_pressed(Button.B, on_button_pressed_b)
