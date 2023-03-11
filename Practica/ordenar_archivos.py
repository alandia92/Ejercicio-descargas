import os
import shutil
# Definir tipos de archivos
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
software_types = ('.exe', '.pkg', '.dmg')

def acceder_descargas():
    if os.name == 'nt':  # Si el sistema operativo es Windows. 'C:\Users\<usuario>\Descargas'
        carpeta_descargas = os.path.expanduser('~\\Descargas') #expande el carácter ~ en la ruta del directorio
    elif os.name == 'posix':  # Si el sistema operativo es Linux o Mac ''home/<usuario>/Descargas
        carpeta_descargas = os.path.expanduser('~/Descargas') 
    else:
        raise RuntimeError('Sistema operativo no compatible')
    return carpeta_descargas

def clasificar_archivos():
    # Guardamos en una variable la ruta de de la carpeta de descargas
    descargas = acceder_descargas()
    # Iteramos sobre el path de descargas.
    for archivo in os.listdir(descargas):
            archivo_path = os.path.join(descargas, archivo) # En cada iteración se crea una ruta
            # Verificamos la extension del archivo
            if archivo.endswith(doc_types):
                # Comprovamos si existen las carpetas, si no se crean
                if not os.path.exists(os.path.join(descargas, 'Documentos')):
                    os.mkdir(os.path.join(descargas, 'Documentos'))
                # Lo movemos a la carpeta correspondiente
                shutil.move(archivo_path, os.path.join(descargas, 'Documentos'))
            elif archivo.endswith(img_types):
                if not os.path.exists(os.path.join(descargas, 'Imagenes')):
                    os.mkdir(os.path.join(descargas, 'Imagenes'))
                shutil.move(archivo_path, os.path.join(descargas, 'Imagenes'))
            elif archivo.endswith(software_types):
                if not os.path.exists(os.path.join(descargas, 'Software')):
                    os.mkdir(os.path.join(descargas, 'Software'))
                    shutil.move(archivo_path, os.path.join(descargas, 'Software'))
            else:
                if not os.path.exists(os.path.join(descargas, 'Otros')):
                    os.mkdir(os.path.join(descargas, 'Otros'))
                shutil.move(archivo_path, os.path.join(descargas, 'Otros'))

clasificar_archivos()