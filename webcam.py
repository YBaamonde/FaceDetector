import cv2

# Cargar el clasificador preentrenado para la detección de caras
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Obtener el stream de video de la primera cámara web
cap = cv2.VideoCapture(0)

# Configurar las propiedades del video
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')) # Establecer el códec a MJPG (Motion JPEG)
cap.set(cv2.CAP_PROP_FPS, 30) # Establecer la velocidad de fotogramas a 30 fps
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # Establecer el ancho del cuadro a 640 píxeles
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # Establecer la altura del cuadro a 480 píxeles

# Capturar cuadros de la cámara web de forma continua
while True:
    # Leer el cuadro actual de la cámara web
    ret, frame = cap.read()

    # Voltear el cuadro horizontalmente para eliminar el efecto espejo
    frame = cv2.flip(frame, 1)

    # Convertir el cuadro a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar caras en la imagen
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Dibujar un rectángulo alrededor de cada cara detectada y añadir el contador
    for i, (x, y, w, h) in enumerate(faces):
        colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0)]
        color = colors[i % len(colors)]  # Ciclar entre colores
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

        cv2.putText(frame, f'Total Faces: {len(faces)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Mostrar el cuadro actual en la pantalla
    cv2.imshow('Webcam', frame)

    # Comprobar si se ha pulsado la tecla 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos de la cámara web y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
