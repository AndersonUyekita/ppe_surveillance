# Detector de EPI

Esse script visa observar pessoas e identificar se há falta ou não do EPI.

## 1. Requisitos

Vamos usar o pacote `YOLO` versão 8 e será necessário fotos e imagens de EPI's para o treino no algoritmo.

### 1.1. Preparativos

Será necessário a prévia instalação do `CMAKE`, a forma mais fácil encontrada foi instando o `Visual Studio Build Tools` ou atualizando o `Visual Studio`.

Após a instalação ou atualização do `Visual Studio` será possível instalar o `CMAKE` no ambiente Python.

Abra o prompt do conda.

```
pip install cmake
```

O `CMAKE` é usado para "compilar" o _package_ `dlib` que possui a particularidade de parte de seu código ser em `C++`.

```
conda install -c conda-forge dlib
```

### 1.2. Bibliotecas

Seguindo as orientações do [1.1. Preparativos](#11-preparativos), os seguintes _packages_ devem estar disponíveis.

* [cmake](https://pypi.org/project/cmake/)
* [dlib](https://pypi.org/project/dlib/)
* [cv2](https://pypi.org/project/opencv-python/)
* [ultralytics](https://pypi.org/project/ultralytics/)

## 2. Processo

1. Aquisição de imagens de EPI's.
2. Fotos reais de pessoas usando EPI's.
3. Marcação (_Labelling_) de todas as fotos e imagens.
4. Treinamento do algoritmo.
5. Início dos teste.

## 3. Organização do Repositório

Esse repositório armazenará todas os dados e informações necessárias para o treinamento e operacionalização do detector de EPI's.

Por este motivo, ele será subdividido em pastas para deixar o local mais organizado.

Pastas:

```
01-dataset
02-trainning
03-surveillance
```
