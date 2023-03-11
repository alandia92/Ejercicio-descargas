import os

def acceder_descargas():
    if os.name == 'nt':  # Si el sistema operativo es Windows. 'C:\Users\<usuario>\Descargas'
        downloads_folder = os.path.expanduser('~\\Descargas') #expande el carácter ~ en la ruta del directorio
    elif os.name == 'posix':  # Si el sistema operativo es Linux o Mac ''home/<usuario>/Descargas
        downloads_folder = os.path.expanduser('~/Descargas') 
    else:
        raise RuntimeError('Sistema operativo no compatible')
    return downloads_folder