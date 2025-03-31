import cv2
import numpy as np

# Lista global para armazenar os valores dos pontos coletados
clicked_values = []

def mouse_event(event, x, y, flags, param):
    global clicked_values
    # A imagem convertida (arr) e a imagem exibida (img_display) foram passadas via param
    arr = param['arr']
    img_display = param['img_display']
    
    # Registra o valor no clique ou enquanto o botão esquerdo está pressionado
    if event == cv2.EVENT_LBUTTONDOWN or (event == cv2.EVENT_MOUSEMOVE and flags & cv2.EVENT_FLAG_LBUTTON):
        pixel_value = arr[y, x]
        clicked_values.append(pixel_value)
        cv2.circle(img_display, (x, y), 3, (0, 255, 0), -1)
        cv2.imshow("Imagem", img_display)
        print(f"Posição: ({x}, {y}) - Valor: {pixel_value}")

def main():
    # Solicita ao usuário que escolha o espaço de cor
    mode = input("Escolha o modo de cor (hsv, rgb ou bgr): ").strip().lower()
    
    # Caminho da imagem (substitua se necessário)
    image_path = "img/cores.jpg"
    img = cv2.imread(image_path)
    if img is None:
        print("Erro ao carregar a imagem.")
        return

    # Cria uma cópia para exibição e para desenhar os pontos (sempre em BGR para exibir corretamente)
    img_display = img.copy()
    
    # Converte a imagem conforme o modo escolhido
    if mode == 'hsv':
        arr = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    elif mode == 'rgb':
        arr = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    elif mode == 'bgr':
        arr = img.copy()
    else:
        print("Modo inválido. Usando BGR por padrão.")
        arr = img.copy()
        mode = 'bgr'
    
    print(f"Modo escolhido: {mode}")
    
    # Exibe a imagem e configura o callback do mouse
    cv2.imshow("Imagem", img_display)
    cv2.setMouseCallback("Imagem", mouse_event, param={'arr': arr, 'img_display': img_display})
    
    print("Clique ou segure o botão esquerdo para coletar os valores.")
    print("Quando terminar, pressione 'q' para exibir os valores low e high.")
    
    # Aguarda até que o usuário pressione 'q'
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    cv2.destroyAllWindows()
    
    # Se valores foram coletados, calcula os mínimos e máximos
    if clicked_values:
        collected = np.array(clicked_values)
        low_values = collected.min(axis=0)
        high_values = collected.max(axis=0)
        
        print("\nValores coletados:")
        if mode == 'hsv':
            print(f"Low (mínimo): Hue: {low_values[0]}, Saturação: {low_values[1]}, Valor: {low_values[2]} -> {tuple(low_values)}")
            print(f"High (máximo): Hue: {high_values[0]}, Saturação: {high_values[1]}, Valor: {high_values[2]} -> {tuple(high_values)}")
        elif mode == 'rgb':
            print(f"Low (mínimo): R: {low_values[0]}, G: {low_values[1]}, B: {low_values[2]} -> {tuple(low_values)}")
            print(f"High (máximo): R: {high_values[0]}, G: {high_values[1]}, B: {high_values[2]} -> {tuple(high_values)}")
        else:  # BGR
            print(f"Low (mínimo): B: {low_values[0]}, G: {low_values[1]}, R: {low_values[2]} -> {tuple(low_values)}")
            print(f"High (máximo): B: {high_values[0]}, G: {high_values[1]}, R: {high_values[2]} -> {tuple(high_values)}")
    else:
        print("Nenhum valor foi coletado.")

if __name__ == '__main__':
    main()
