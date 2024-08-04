# Training

Após a categorização (_labelling_) das imagens será possível executar o modelo `YOLO` de detecção de objetos.

## 1. Pré-requisitos

A instalação da biblioteca `dlib` é o mais trabalhoso, pois requer a instalação do `CMAKE`. A instalação do `CMAKE` já foi esclarecida.

## 2. Estrutura de Treinamento

O _script_ é muito simples:

```py
# Carrega a Biblioteca YOLO
from ultralytics import YOLO

# Carregar o modelo YOLOv8s
model = YOLO('yolov8s.pt')

# Treinar o modelo com os dados
model.train(data='C:/Users/ander/Documents/ppe_surveillance/01-dataset/data.yaml',
            epochs=100, # Quantidade de vezes que o modelo irá iterar cada imagem do dataset
            imgsz=640)  # Dimensão que as imagens do dataset serão redimensionadas (640x640 pixels)

# Avaliar o modelo
metrics = model.val()

# Imprime na tela o resultado
print(metrics)
```

Quanto maior o número de `epochs` maior será o tempo de processamento.

Quanto maior o número de `imgsz` maior será o tempo de processamento.

## 3. Resultado

O resultado ficará armazenado na pasta `runs`. Portanto, para acessar o modelo treinado você deverá navegar até a seguinte pasta.

> runs > detect > train2 > weights > `best.pt`

O arquivo `best.pt` contém todos os parâmetros do algoritmo treinado e ele será a base para a identificação dos equipamentos de segurança.
