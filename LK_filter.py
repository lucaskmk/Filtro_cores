import cv2
import numpy as np

# Lista global para armazenar os valores HSV dos pontos
clicked_hsv = []

def mouse_event(event, x, y, flags, param):
    global clicked_hsv
    hsv = param['hsv']
    img = param['img']
    
    # Registra tanto no clique quanto enquanto o botão estiver pressionado
    if event == cv2.EVENT_LBUTTONDOWN or (event == cv2.EVENT_MOUSEMOVE and flags & cv2.EVENT_FLAG_LBUTTON):
        pixel_hsv = hsv[y, x]
        clicked_hsv.append(pixel_hsv)
        cv2.circle(img, (x, y), 3, (0, 255, 0), -1)
        cv2.imshow("Imagem", img)
        print(f"Posição: ({x}, {y}) - HSV: {pixel_hsv}")

def main():
    # Substitua pelo caminho da sua imagem
    image_path = "img/hall_box_battery1.jpg"
    img = cv2.imread(image_path)
    if img is None:
        print("Erro ao carregar a imagem.")
        return

    # Cria uma cópia para desenhar os pontos
    img_copy = img.copy()
    
    # Converte a imagem para HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Exibe a imagem e configura o callback do mouse
    cv2.imshow("Imagem", img_copy)
    cv2.setMouseCallback("Imagem", mouse_event, param={'hsv': hsv, 'img': img_copy})
    
    print("Clique ou segure o botão esquerdo para coletar os valores HSV.")
    print("Quando terminar, pressione 'q' para exibir os valores low e high.")
    
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    
    cv2.destroyAllWindows()
    
    if clicked_hsv:
        # Cria um array a partir dos valores coletados sem reatribuir a variável global
        collected = np.array(clicked_hsv)
        low_values = collected.min(axis=0)
        high_values = collected.max(axis=0)
        print("\nValores coletados:")
        print(f"Low (mínimo): Hue: {low_values[0]}, Saturação: {low_values[1]}, Valor: {low_values[2]} -> {low_values[0] , low_values[1] ,low_values[2] }")
        print(f"High (máximo): Hue: {high_values[0]}, Saturação: {high_values[1]}, Valor: {high_values[2]} -> {high_values[0] , high_values[1] ,high_values[2] }")
    else:
        print("Nenhum valor foi coletado.")

if __name__ == '__main__':
    main()
