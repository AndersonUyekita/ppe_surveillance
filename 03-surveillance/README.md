# Surveillance

O sistema de vigilância de EPI utilizará a priori a câmera de laptop para identificar se o usuário está usando o EPI.

Note que a origem da filmagem é de livre escolha, para ser didático estamos usando a câmera do laptop.

## 1. Requisitos

Vamos precisar acessar a câmera do laptop e navegar pelas pastas do computador.

* `cv2`: Package de Visão Computacional (vamos acessar a câmera);
* `os`: Package do Sistema Operacional (acessar as pastas), e;
* `ultralytics`: É onde o YOLO fica hospedado.

## 2. Modelo treinado

O sistema de vigilância de EPI será executado a partir do modelo treinado e armazenado em `02-training`.

## 3. Funcionamento

A câmera do laptop irá fornecer em tempo real a filmagem do ambiente, automaticamente o script analisará os frames do vídeo e irá sobrepor à imagem um enquadramento do EPI.

A lógica do que se fazer após a identificação da ausência do EPI será tratado posteriormente.

O fechamento da janela da videofilmagem é feita apertando a tecla <kbd>Q</kbd>.

## 4. Script

```py
# Bibliotecas necessárias
import os
import cv2
from ultralytics import YOLO

# Caminho do arquivo do modelo
model_path = 'C:/Users/ander/Documents/jupyter_notebooks/ppe_surveillance/02-training/runs/detect/train2/weights/best.pt'

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
```
