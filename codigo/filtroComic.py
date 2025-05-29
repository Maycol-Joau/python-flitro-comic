import cv2
import numpy as np

#Cargar la imagen
imagen = cv2.imread("../imagenes/TomyCoquete.jpg")

#Verificar si la imagen se cargo correctamente
if imagen is None:
    print("Error: no se pudo cargar la imagen")
    exit()

#Aplicar efecto cómic
hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
hsv[:, :, 1] = hsv[:, :, 1] * 1.5  # Aumentar saturación
hsv[:, :, 1] = np.clip(hsv[:, :, 1], 0, 255)
color_reducido = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

#2. Detectar bordes
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
bordes = cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

#3. Suavizar la imagen
suavizado = cv2.medianBlur(color_reducido, 3)

#4. Combinar bordes con la imagen suavizada
bordes_bgr = cv2.cvtColor(bordes, cv2.COLOR_GRAY2BGR)
comic = cv2.bitwise_and(suavizado, bordes_bgr)

#Agregar un nombre sobre la imagen
cv2.putText(comic, "Tomy Coquete", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,255), 2)

#Mostrar la imagen
cv2.imshow("Original", imagen)
cv2.imshow("Comic", comic)

#Guardar la imagen
cv2.imwrite("../imagenes/TomyCoqueteComic.jpg", comic)
print("Tu imagen fue guardada con éxito")

cv2.waitKey(0)
cv2.destroyAllWindows()