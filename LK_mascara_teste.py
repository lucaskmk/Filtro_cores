import cv2
import numpy as np

def main():
    # Substitua pelo caminho da sua imagem
    image_path = "img/hall_box_battery1.jpg"
    img = cv2.imread(image_path)
    if img is None:
        print("Erro ao carregar a imagem.")
        return
    
    # Converte a imagem para o espaço HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Defina os valores low e high obtidos
    # Exemplo: para segmentar uma faixa de verde
    low_values = np.array([0, 49, 119])    # [Hue_min, Saturação_min, Valor_min]
    high_values = np.array([21, 255, 255])   # [Hue_max, Saturação_max, Valor_max]
    
    # Cria a máscara com base nos limites definidos
    mask = cv2.inRange(hsv, low_values, high_values)
    
    # Aplica a máscara à imagem original para isolar a região de interesse
    resultado = cv2.bitwise_and(img, img, mask=mask)
    
    # Exibe a imagem original, a máscara e o resultado
    cv2.imshow("Imagem Original", img)
    cv2.imshow("Máscara", mask)
    cv2.imshow("Resultado", resultado)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()