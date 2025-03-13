# Proyecto WebCam

Este es un proyecto sencillo que utiliza OpenCV para capturar video desde una cámara web y detectar caras en tiempo real.

## Dependencias

Para ejecutar este proyecto, necesitas tener instaladas las siguientes dependencias:

- Python 3.x
- OpenCV

Instala OpenCV ejecutando el siguiente comando en tu terminal:

```bash
pip install opencv-python
```

## Cómo funciona

El script `webcam.py` realiza las siguientes acciones:

1. Carga un clasificador preentrenado para la detección de caras.
2. Obtiene el stream de video de la primera cámara web disponible.
3. Configura las propiedades del video (códec, velocidad de fotogramas, ancho y altura del cuadro).
4. Captura cuadros de la cámara web de forma continua.
5. Convierte cada cuadro a escala de grises y detecta caras en la imagen.
6. Dibuja un rectángulo alrededor de cada cara detectada y muestra el número total de caras detectadas.
7. Muestra el cuadro actual en la pantalla.

> [!IMPORTANT]
> Cierra el programa de captura pulsando la tecla 'q'.

## Cómo ejecutar

Para ejecutar el script, simplemente abre una terminal y navega al directorio donde se encuentra el archivo `webcam.py`. Luego, ejecuta el siguiente comando:

```bash
python webcam.py
```

Esto abrirá una ventana que muestra el video capturado por la cámara web con las caras detectadas resaltadas.

> [!NOTE]
> - Asegúrate de tener una cámara web conectada y funcionando.
> - Puedes ajustar los parámetros del clasificador y las propiedades del video según tus necesidades.

> [!IMPORTANT]
> - Obviamente el rendimiento y los resultados del script dependen de las características de tu sistema.