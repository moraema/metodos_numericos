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

    x0 = float(initial_x0.get())
    x1 = float(initial_x1.get())
    crit = float(criterion.get())

    plt.figure()
    xpts = np.linspace(x0 - 10, x0 + 10, 1000)
    plt.plot(xpts, f(xpts))
    plt.axhline(color='black')
    plt.axvline(color='black')

    i = 0
    ea = 1
    x_prev = 0

    # Crear la tabla
    table_frame = ttk.Frame(main_frame)
    table_frame.grid(column=0, row=6, columnspan=2)

    table = ttk.Treeview(table_frame, columns=('i', 'x0', 'x1', 'f(x0)', 'f(x1)', 'xi', 'f(xi)'), show='headings')
    table.heading('i', text='i')
    table.heading('x0', text='x0')
    table.heading('x1', text='x1')
    table.heading('f(x0)', text='f(x0)')
    table.heading('f(x1)', text='f(x1)')
    table.heading('xi', text='xi')
    table.heading('f(xi)', text='f(xi)')
    table.pack()

    while ea > crit:
        xi = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        ea = abs((xi - x_prev) / xi)
        f_xi = f(xi)
        table.insert('', 'end', values=(i, round(x0, 9), round(x1, 9), round(f(x0), 9), round(f(x1), 9), round(xi, 9), round(f_xi, 9)))
        x_prev = xi
        x0 = x1
        x1 = xi
        i += 1

    plt.scatter(xi, 0, c='red')
    plt.annotate(round(xi, 9), xy=(xi, 0.5))
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Búsqueda de raíces con el método de la secante')
    plt.grid(True, which='both')
    plt.ylim([-15, 15])
    plt.show()


def secante_gui():
    global root, main_frame, function_entry, initial_x0, initial_x1, criterion

    root = tk.Tk()
    root.title("MÉTODO DE LA SECANTE")

    main_frame = ttk.Frame(root, padding="20")
    main_frame.grid(column=0, row=0)

    function_label = ttk.Label(main_frame, text="Función (ejemplo: x**3 + 3*x - 2):")
    function_label.grid(column=0, row=0, sticky="W")

    function_entry = ttk.Entry(main_frame, width=30)
    function_entry.grid(column=1, row=0)

    initial_x0_label = ttk.Label(main_frame, text="Valor inicial x0:")
    initial_x0_label.grid(column=0, row=1, sticky="W")

    initial_x0 = ttk.Entry(main_frame, width=10)
    initial_x0.grid(column=1, row=1)

    initial_x1_label = ttk.Label(main_frame, text="Valor inicial x1:")
    initial_x1_label.grid(column=0, row=2, sticky="W")

    initial_x1 = ttk.Entry(main_frame, width=10)
    initial_x1.grid(column=1, row=2)

    criterion_label = ttk.Label(main_frame, text="Criterio de diferencia:")
    criterion_label.grid(column=0, row=3, sticky="W")

    criterion = ttk.Entry(main_frame, width=10)
    criterion.grid(column=1, row=3)

    plot_button = ttk.Button(main_frame, text="Aceptar", command=plot_function)
    plot_button.grid(column=1, row=4)

    result_label = ttk.Label(main_frame, text="")
    result_label.grid(column=0, row=5, columnspan=2)

    root.mainloop()
