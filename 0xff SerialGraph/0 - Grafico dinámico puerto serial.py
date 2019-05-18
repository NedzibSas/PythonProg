import serial
import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import numpy as np

global COUNT
COUNT = 0
# Puerto Serial
port = serial.Serial('/dev/ttyACM0', 115200, timeout = 1.)

# Creemos los ejes y la figura donde graficaremos.
fig, ax = plt.subplots()

# Este diccionario almacenara los datos del sensor.
signal = {'x': [], 'y': [], 'z': []}

# Estas lineas dibujaran los datos en la figura.
lines = [ax.plot([], [])[0] for _ in signal.keys()]

# Usaremos esta variable para detectar autoescalado de la grafica.
ylim = ()
xlim = ()

# La funcion stream sera llamada periodicamente por el timer
# cada numero determinado de milisegundos definido por la variable
# rate.
def stream():
    # Esta es la cadena de caracteres leida por el puerto serial
    # en formato JSON.
    raw_data = port.readline()
    try:
        # El modulo json permite convertir un string en formato JSON a
        # diccionarios de Python. Si el string no viene en el formato adecuado
        # o la informacion se corrompe, el programa nos lo reporta en
        # el bloque de excepcion ValueError;.
        json_data = json.loads(raw_data)
        for k in signal.keys():
            signal[k].append(json_data[k])
        print(raw_data)
    except ValueError:
        print('Could not read data: %s', raw_data)
    # Si el puerto sigue abierto, programamos otra llamada a la funcion para
    # volver a leer el puerto serial.
    if port.is_open:
        threading.Timer(10 / 1000., stream).start()
    else:
        print('Not streaming anymore!')

def animate(i):
    # Las siguientes dos lineas de codigo auto ajustan el eje
    # de las Y en funcion del contenido de la grafica. Me tomo
    # algo de tiempo encontrar estas funciones. Cuidenlo con su
    # alma y compartanlo!
    global COUNT
    global ylim, xlim

    ax.relim()
    ax.autoscale_view()
    if ax.get_ylim() != ylim or ax.get_xlim() != xlim:
        # Esta parte del codigo lo que hace es monitorear los valores
        # del limite del eje Y para detectar cuando la grafica ha sido
        # reajustada. Esto para redibujar las etiquetas del eje Y a
        # medida que se reajusta. Si no, las etiquetas permanecen mientras
        # el eje se reajusta. Por lo que los valores no coinciden con lo
        # desplegado en el eje. Los invito a removerlo para que vean a
        # lo que me refiero.
        if ax.get_xlim() != xlim:
            xlim = ax.get_xlim()
        if ax.get_ylim() != ylim:
            ylim = ax.get_ylim()
        fig.canvas.draw()

    for name, line in zip(signal.keys(), lines):
    # Si no hay datos nuevos, ni siquiera nos molestamos en intentar
    # graficar.
        if len(signal[name]) > 0:
            _, ly = line.get_data()
            ly = np.append(ly, signal[name])
            _xdata = np.arange(ly.size)
            line.set_data(_xdata, ly)
            #Cambia el rango de los x
            COUNT+=1
            ax.set_xlim(COUNT-20, COUNT+200)
            # La informacion ha sido graficada. Ya nos podemos deshacer
            # de ella.
            signal[name] = []
        else:
            print('No data')
    return lines

if __name__ == '__main__':

    ani = animation.FuncAnimation(fig, animate, interval=50, blit=True)
    plt.title('Random Test')
    stream()
    plt.show()
    while input('Hit Q to exit.\n\r> ').lower() != 'q':
        pass
port.close()
