import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, sympify, lambdify
import tkinter as tk
from tkinter import ttk

x = symbols('x')


def plot_function():
    fn_str = function_entry.get()
    fn_str = fn_str.replace('^', '**')
    fn = sympify(fn_str)
    f = lambdify(x, fn)

    a = float(initial_a.get())
    b = float(initial_b.get())
    crit = float(criterion.get())

    if f(a) * f(b) < 0:
        plt.figure()
        xpts = np.linspace(a, b, 1000)
        plt.plot(xpts, f(xpts))
        plt.axhline(color='black')
        plt.axvline(color='black')

        i = 0
        ea = 1
        x_prev = 0

        # Crear la tabla
        table_frame = ttk.Frame(main_frame)
        table_frame.grid(column=0, row=6, columnspan=2)

        table = ttk.Treeview(table_frame, columns=('i', 'a', 'b', 'xr', 'ea(%)'), show='headings')
        table.heading('i', text='i')
        table.heading('a', text='a')
        table.heading('b', text='b')
        table.heading('xr', text='xr')
        table.heading('ea(%)', text='ea(%)')
        table.pack()

        while ea > crit:
            xr = (a + b) / 2
            ea = abs((xr - x_prev) / xr)
            if f(xr) * f(a) < 0:
                b = xr
            else:
                a = xr
            x_prev = xr
            i += 1
            # Insertar fila en la tabla
            table.insert('', 'end', values=(i, round(a, 9), round(b, 9), round(xr, 9), round(ea * 100, 9)))
        
        plt.scatter(xr, 0, c='red')
        plt.annotate(round(xr, 9), xy=(xr, 0.5))
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Búsqueda de raíces con el método de bisección')
        plt.grid(True, which='both')
        plt.ylim([-15, 15])
        plt.show()
    else:
        result_label.config(text="La función no tiene una raíz en el intervalo dado.")


def biseccion_gui():
    global root, main_frame, function_entry, initial_a, initial_b, criterion, result_label

    root = tk.Tk()
    root.title("MÉTODO DE BISECCIÓN")

    main_frame = ttk.Frame(root, padding="20")
    main_frame.grid(column=0, row=0)

    function_label = ttk.Label(main_frame, text="Función (ejemplo: x**3 + 3*x - 2):")
    function_label.grid(column=0, row=0, sticky="W")

    function_entry = ttk.Entry(main_frame, width=30)
    function_entry.grid(column=1, row=0)

    initial_a_label = ttk.Label(main_frame, text="Valor inicial A:")
    initial_a_label.grid(column=0, row=1, sticky="W")

    initial_a = ttk.Entry(main_frame, width=10)
    initial_a.grid(column=1, row=1)

    initial_b_label = ttk.Label(main_frame, text="Valor inicial B:")
    initial_b_label.grid(column=0, row=2, sticky="W")

    initial_b = ttk.Entry(main_frame, width=10)
    initial_b.grid(column=1, row=2)

    criterion_label = ttk.Label(main_frame, text="Criterio de diferencia:")
    criterion_label.grid(column=0, row=3, sticky="W")

    criterion = ttk.Entry(main_frame, width=10)
    criterion.grid(column=1, row=3)

    plot_button = ttk.Button(main_frame, text="Aceptar", command=plot_function)
    plot_button.grid(column=1, row=4)

    result_label = ttk.Label(main_frame, text="")
    result_label.grid(column=0, row=5, columnspan=2)

    root.mainloop()
