Ejecucion del programa:

En la linea 145 del codigo se utiliza el metodo -procesarArchivo('Ruta del archivo')-,
se debe ingresar como parametro la ruta donde se encuentra el archivo 'dataset.csv'.
Nota: unicamente se aceptan archivos con el formato .csv

Como el lenguaje utilizado es python
para ejecutarlo desde la terminal se usa el siguiente comando:

python Principal.py

Se utiliza la libreria requests, la cual permite obtener un resultado a nuestra peticion, 
pero se necesita intalarlo para lo cual ejecuta los siguientes comandos para linux:

sudo apt install python-pip
pip install requests

Aparecerá una lista con todas las ciudades y su respectivo clima donde se detalla la 
siguiente informacion:

-Temperatura
-Presion
-Humedad

