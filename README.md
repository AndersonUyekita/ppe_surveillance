# Detector de EPI

Esse script visa observar pessoas e identificar se há falta ou não do EPI.

## 1. Requisitos

Vamos usar o pacote `YOLO` versão 8 e será necessário fotos e imagens de EPI's para o treino no algoritmo.

### 1.1. Preparativos

Será necessário a prévia instalação do `CMAKE`, a forma mais fácil encontrada foi instando o `Visual Studio Build Tools` ou atualizando o `Visual Studio`.

Após a instalação/atualização do `Visual Studio` será possível instalar o `CMAKE` no ambiente Python pelo `prompt` do Anaconda.

```
pip install cmake
```

O `CMAKE` é usado para "compilar" o _package_ `dlib` que possui a particularidade de parte de seu código ser em `C++`.

```
conda install -c conda-forge dlib
```

Os demais _packages_ são de simples instalação.

### 1.2. Bibliotecas

Seguindo as orientações do [1.1. Preparativos](#11-preparativos), os seguintes _packages_ devem estar disponíveis no ambiente de desenvolvimento do Python.

* [cmake](https://pypi.org/project/cmake/)
* [dlib](https://pypi.org/project/dlib/)
* [cv2](https://pypi.org/project/opencv-python/)
* [ultralytics](https://pypi.org/project/ultralytics/)
* [labelimg](https://pypi.org/project/labelImg/)

### 1.3. _Environment_

Talvez seja necessário a criação de um ambiente específico para o projeto.

Quando tentei usar o ambiente `(base)` o _script_ alegava que não um problema de kernel.

Só consegui treinar o algoritmo após a criação do ambiente dedicado para o treinamento. Pode ser que um ambiente muito carregado como o `(base)` interfira negativamente como a instalação de _packages_ corrompidos.

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
02-training
03-surveillance
```
