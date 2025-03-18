# Reloj Alarma

[English language](./readme-english.md)

Es un reloj alarma hecho en Tkinter con el propósito de tener una alarma en mi computadora. Fue desarrollado en Windows, pero aún no ha sido probado en Linux. Las imagenes e iconos fueron hechos por mi.

|<img src="https://cdn.discordapp.com/attachments/697811476362035251/1351421123249569832/image.png?ex=67da507f&is=67d8feff&hm=bf4df0a62c1490f26fab8b7e236d57515a2cf40da1d503963f12f3c40aba4df1&">|<img src="https://cdn.discordapp.com/attachments/697811476362035251/1351421186701262889/image.png?ex=67da508f&is=67d8ff0f&hm=05142fd563346a5d82daf928690de3ad039ac88b818e2b0f15fb20a9830202ad&">|
|:-:|:-:|
|Interfaz en tema claro|Interfaz en tema oscuro|

## Funciones

* Reproduce un sonido en segundo plano que se puede personalizar o desactivar.
* Muestra un mensaje en pantalla que se puede desactivar o personalizar.
* Permite elegir si se quiere ejecutar un programa o no.
* Permite seleccionar entre el formato de 24 horas o el de 12 horas en la interfaz.
* Permite elegir entre tema claro u oscuro en la interfaz.
* Permite elegir si mostrar la hora, minutos o segundos en la interfaz.

## Posibles Errores

### Las fuentes no se muestran bien

En la carpeta raiz hay una carpeta llamada **fonts**, en donde están las fuentes usadas en el proyecto. Instálalas, y reinicia la aplicación.

### Dependencias
Este proyecto usa **Pillow** para las imágenes (widgets personalizados), y **PyGame** (sonido). Asegurate de tenerlas instaladas antes de la ejecución.

Puedes usar el siguiente comando dentro del directorio raíz para instalar dichas librerías:
```
pip install -r requirements.txt
```
