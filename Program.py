from __future__ import division

import QuatMath
import matplotlib.pyplot as plt
import Tkinter as tk

one = [1, 0, 0, 0]


def calculate_fractal_set(resolutionX, resolutionY, infinity, r1, r3, xmin, xmax, ymin, ymax):
    # intervalo ilgiai
    hx = (xmax - xmin) / (resolutionX - 1)
    hy = (ymax - ymin) / (resolutionY - 1)

    #Inicializuojama matrica
    matrix = [[0 for x in range(resolutionX)] for y in range(resolutionY)]

    for j in range(0, resolutionY):
        r4 = ymin + (hy * j)
        for k in range(0, resolutionX):
            r2 = xmin + (hx * k)
            r = [r1, r2, r3, r4]
            count = 0
            z = [0.5, 0.0, 0.0, 0.0]

            while count < 255 and QuatMath.absquat(z) < infinity:
                sub = QuatMath.subtraction(one, z)
                mul = QuatMath.multiplication(r, z)
                z = QuatMath.multiplication(mul, sub)
                count += 1

            matrix[resolutionY - 1 - j][k] = count
            print (count)
    return matrix


def show_fractal_from_matrix(matrix, xmin, xmax, ymin, ymax):
    plt.imshow(matrix, cmap="gray", vmin=0, vmax=255, interpolation='none', extent=[xmin, xmax, ymin, ymax])
    plt.show()


def calculate_and_show(resolutionX, resolutionY, infinity, r1, r3, xmin, xmax, ymin, ymax):
    matrix = calculate_fractal_set(resolutionX, resolutionY, infinity, r1, r3, xmin, xmax, ymin, ymax)
    show_fractal_from_matrix(matrix, xmin, xmax, ymin, ymax)


master = tk.Tk()
master.title("Mandelbroto Fraktalas")
tk.Label(master, text="Paveikslelio rezoliucija: " + u"\u2192").grid(row=0, column=0, sticky='E')
tk.Label(master, text=u"\u2191").grid(row=0, column=2, sticky='E')
tk.Label(master, text="Riba ties kuria sustoti. (Dirbtine begalybe)").grid(row=1, column=0, sticky='E')
tk.Label(master, text="\'r\' kvaterniono (r1,x,r3,y) nekintamos reiksmes: r1").grid(row=2, column=0, sticky='E')
tk.Label(master, text="r3").grid(row=2, column=2, sticky='E')
tk.Label(master, text="X intervalo reziai: X_min").grid(row=3, column=0, sticky='E')
tk.Label(master, text="X_max").grid(row=3, column=2, sticky='E')
tk.Label(master, text="Y intervalo reziai: Y_min").grid(row=4, column=0, sticky='E')
tk.Label(master, text="Y_max").grid(row=4, column=2, sticky='E')

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)
e8 = tk.Entry(master)
e9 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=0, column=3)
e3.grid(row=1, column=1)
e4.grid(row=2, column=1)
e5.grid(row=2, column=3)
e6.grid(row=3, column=1)
e7.grid(row=3, column=3)
e8.grid(row=4, column=1)
e9.grid(row=4, column=3)

tk.Button(master, text='Baigti darba', command=master.quit).grid(row=5, column=0, sticky='E')
tk.Button(master, text='Vaizduoti fraktala', command= lambda : calculate_and_show(int(e1.get()),
                                                                                  int(e2.get()),
                                                                                  float(e3.get()),
                                                                                  float(e4.get()),
                                                                                  float(e5.get()),
                                                                                  float(e6.get()),
                                                                                  float(e7.get()),
                                                                                  float(e8.get()),
                                                                                  float(e9.get())
                                                                                  )).grid(row=5,
                                                                                          column=1,
                                                                                          sticky='W')

tk.mainloop()
