#El módulo controlador.py permite lanzar la ventana de la aplicación.

#La clase Control, mediante su constructor, permite pasar por parametro un objeto. 
#que instancia a la clase Tk() [la ventana] y lanza, mediante la clase Ventana, la aplicación.

#Importamos Tk de tkinter para definir el inicio-fin de la ventana.
#Importamos la clase Ventana del módulo vista que contiene toda la parte visual de la app.
from tkinter import Tk
from vista import Ventana

class Control():
    
    def __init__(self, windows):
        self.windows_controler = windows
        self.objeto_vista = Ventana(self.windows_controler)

#Se lanza la ventana principal de la aplicación.
if __name__ == "__main__":
    windows = Tk()
    almacen_ventana = Control(windows)
    windows.mainloop()