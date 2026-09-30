# PRÁCTICA 8
# Realiza el  rograma que muestre un sms, si el estudiante
# es aprobado o reprobado usando números al azar.
#boton A, en el lenguaje Python

nota = 0

def on_button_pressed_a():
    global nota
    nota = randint(1, 100)
    basic.show_number(nota)
    basic.pause(1000)

    if nota >= 60:
        basic.show_string("APROBADO")
        basic.pause(500)
    else:
        basic.show_string("REPROBADO")
        basic.pause(500)

    basic.clear_screen()

input.on_button_pressed(Button.A, on_button_pressed_a)
