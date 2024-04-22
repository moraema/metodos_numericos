import tkinter as tk
from tkinter import ttk
import secante
import biseccion
import falsa_posicion
import newton_raphson


def open_secante_gui():
    secante.secante_gui()


def open_biseccion_gui():
    biseccion.biseccion_gui()


def open_falsa_posicion_gui():
    falsa_posicion.falsa_posicion_gui()


def open_newton_raphson_gui():
    newton_raphson.newton_raphson_gui()


def main():
    root = tk.Tk()
    root.title("Menú Principal")

    # Definir un nuevo estilo para los botones
    style = ttk.Style()
    style.configure('TButton', background='#0598E8')

    main_frame = ttk.Frame(root, padding="100")
    main_frame.grid(column=0, row=0)

    secante_button = ttk.Button(main_frame, text="Método de la Secante", command=open_secante_gui, style='TButton')
    secante_button.grid(column=0, row=0, pady=5)

    biseccion_button = ttk.Button(main_frame, text="Método de Bisección", command=open_biseccion_gui, style='TButton')
    biseccion_button.grid(column=0, row=1, pady=5)

    falsa_posicion_button = ttk.Button(main_frame, text="Método de la Falsa Posición", command=open_falsa_posicion_gui, style='TButton')
    falsa_posicion_button.grid(column=0, row=2, pady=5)

    newton_raphson_button = ttk.Button(main_frame, text="Método de Newton-Raphson", command=open_newton_raphson_gui, style='TButton')
    newton_raphson_button.grid(column=0, row=3, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
