# Carrega a Biblioteca YOLO
from ultralytics import YOLO

# Carregar o modelo YOLOv8s
model = YOLO('yolov8s.pt')

# Treinar o modelo com os dados
model.train(data='C:/Users/ander/Documents/ppe_surveillance/01-dataset/data.yaml',
            epochs=100, # Quantidade de vezes que o modelo irá iterar cada imagem do dataset
            imgsz=640)  # Dimensão que as imagens do dataset serão redimensionadas (640x640 pixels)
