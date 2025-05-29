# Filtro de Efecto Cómic con Python y OpenCV

Este proyecto aplica un efecto de estilo cómic a una imagen utilizando Python y las bibliotecas OpenCV y NumPy.

## Descripción

El script carga una imagen, aumenta la saturación de color, detecta los bordes y luego combina estos elementos para crear una imagen con un aspecto similar al de un cómic. Finalmente, añade un texto sobre la imagen resultante.

## Librerías Utilizadas

* **OpenCV (cv2):** Para el procesamiento de imágenes (lectura, conversión de color, detección de bordes, filtros, etc.).
* **NumPy:** Para operaciones numéricas eficientes, especialmente con los arrays de imagen.

## Instalación

Para poder ejecutar este script, necesitarás tener Python instalado y luego instalar las librerías requeridas. Puedes instalarlas usando pip:

```bash
pip install opencv-python numpy