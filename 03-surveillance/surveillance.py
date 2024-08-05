# Bibliotecas necessárias
import os
import cv2
from ultralytics import YOLO

# Caminho do arquivo do modelo
model_path = 'C:/Users/ander/Documents/jupyter_notebooks/ppe_surveillance/02-training/runs/detect/train/weights/best.pt'

# Verificar se o arquivo existe
if not os.path.isfile(model_path):
    print(f"Erro: O arquivo '{model_path}' não foi encontrado.")
else:
    # Carregar o modelo treinado
    model = YOLO(model_path)

    # Inicializar a captura de vídeo
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erro ao abrir a câmera")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro ao capturar frame")
            break

        # Realizar a detecção
        results = model(frame)

        # Renderizar resultados na imagem
        annotated_frame = results[0].plot()

        # Mostrar a imagem com caixas
        cv2.imshow('YOLOv8 EPI Detection', annotated_frame)

        # Sair do loop ao pressionar a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar a captura e fechar janelas
    cap.release()
    cv2.destroyAllWindows()
