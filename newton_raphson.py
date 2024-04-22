import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, sympify, lambdify, diff
import tkinter as tk
from tkinter import ttk

x = symbols('x')


def plot_function():
    fn_str = function_entry.get()
    fn_str = fn_str.replace('^', '**')
    fn = sympify(fn_str)
    f = lambdify(x, fn)
    f_prime = lambdify(x, diff(fn))

    x0 = float(initial_x.get())
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

    table = ttk.Treeview(table_frame, columns=('i', 'xi', 'f(xi)', 'f\'(xi)', 'ea(%)'), show='headings')
    table.heading('i', text='i')
    table.heading('xi', text='xi')
    table.heading('f(xi)', text='f(xi)')
    table.heading('f\'(xi)', text='f\'(xi)')
    table.heading('ea(%)', text='ea(%)')
    table.pack()

    while ea > crit:
        xi = x0 - f(x0) / f_prime(x0)
        ea = abs((xi - x_prev) / xi)
        f_xi = f(xi)
        f_prime_xi = f_prime(xi)
        table.insert('', 'end', values=(i, round(xi, 9), round(f_xi, 9), round(f_prime_xi, 9), round(ea * 100, 9)))
        x_prev = xi
        x0 = xi
        i += 1

    plt.scatter(xi, 0, c='red')
    plt.annotate(round(xi, 9), xy=(xi, 0.5))
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Búsqueda de raíces con el método de Newton-Raphson')
    plt.grid(True, which='both')
    plt.ylim([-15, 15])
    plt.show()


def newton_raphson_gui():
    global root, main_frame, function_entry, initial_x, criterion, result_label

    root = tk.Tk()
    root.title("MÉTODO DE NEWTON-RAPHSON")

    main_frame = ttk.Frame(root, padding="20")
    main_frame.grid(column=0, row=0)

    function_label = ttk.Label(main_frame, text="Función (ejemplo: x**3 + 3*x - 2):")
    function_label.grid(column=0, row=0, sticky="W")

    function_entry = ttk.Entry(main_frame, width=30)
    function_entry.grid(column=1, row=0)

    initial_x_label = ttk.Label(main_frame, text="Valor inicial:")
    initial_x_label.grid(column=0, row=1, sticky="W")

    initial_x = ttk.Entry(main_frame, width=10)
    initial_x.grid(column=1, row=1)

    criterion_label = ttk.Label(main_frame, text="Criterio de diferencia:")
    criterion_label.grid(column=0, row=2, sticky="W")

    criterion = ttk.Entry(main_frame, width=10)
    criterion.grid(column=1, row=2)

    plot_button = ttk.Button(main_frame, text="Aceptar", command=plot_function)
    plot_button.grid(column=1, row=3)

    result_label = ttk.Label(main_frame, text="")
    result_label.grid(column=0, row=4, columnspan=2)

    root.mainloop()
