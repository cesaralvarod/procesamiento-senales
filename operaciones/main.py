import cv2 as cv
import numpy as np


if __name__ == "__main__":
    # Crear imagen 400x400
    img1 = np.ones((300, 300, 3), np.uint8)*255
    img2 = np.ones((300, 300, 3), np.uint8)*255

    # Crear una imagen blanca de 400x400
    width, height = 400, 400

    # definimos el tamano del rectangulo
    rect_width, rect_height = 200, 160

    # calcular centro de la imagen
    center_x, center_y = width//2, height//2

    # definir radio y color del circulo
    circle_radius = 100
    color = (0, 0, 0)

    # dibujar circulo
    cv.circle(img1, (center_x, center_y), circle_radius, color, -1)

    # calculamos corrdenadas del rectangulo para que este centrado en la imagen
    x1, y1 = center_x-rect_width//2, center_y-rect_height//2
    x2, y2 = x1+rect_width, y1+rect_height

    # dibujar el rectangulo de la imagen
    cv.rectangle(img2, (x1, y1), (x2, y2), color, -1)

    # operaciones
    result_and = cv.bitwise_and(img1, img2)
    result_or = cv.bitwise_or(img1, img2)
    result_xor = cv.bitwise_xor(img1, img2)
    result_not = cv.bitwise_not(img1)

    # show
    while True:
        cv.imshow('Imagen 2', img2)

        cv.imshow('AND', result_and)
        cv.imshow('OR', result_or)
        cv.imshow('XOR', result_xor)
        cv.imshow('NOT', result_not)

        if cv.waitKey(33) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()

    pass
