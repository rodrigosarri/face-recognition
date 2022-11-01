# Projeto de reconhecimento facial

Esse é um projeto de reconhecimento facial desenvolvido em Python para desenvolvimento da trilha EY Fast Track

## Pré-requisitos

- Python 3.10.2
- pip 22.3

## Instalação

```console
git clone https://github.com/rodrigosarri/face-recognition.git
cd face-recognition
pip install -r requirements.txt
```

Podem ocorrer problemas com a instalação da biblioteca `cmake` e `dlib`. Caso ocorram, na pasta install existem recursos para resolver esse problema.

### Resolvendo o problema Cmake
O arquivo `cmake-3.25.0-rc2-windows-x86_64` (Windows) pode ser utilizado para instalar individualmente (e stand alone) a biblioteca `cmake`, caso utilize um sistema operacional diferente, poderá baixar essa biblioteca através do link: https://cmake.org/download/.

### Resolvendo o problema dlib
Nessa mesma pasta **install**, poderá utilizar através desse pacote com o comando `python setup.py install` (dentro da pasta `dlib`). Para maiores informações pode visitar o repositório: https://github.com/davisking/dlib


## Funcionamento do Projeto
Na pasta **faces** são colocadas imagens com o nome de cada rosto. Essa é uma parte essencial do funcionamento, pois através dessas imagens que serão identificados em qualquer outra imagem rostos e a quem pertence esse rosto. O nome da imagem será o nome aplicado no reconhecimento.

A imagem de teste utilizada para identificação fica localizada na raiz do projeto com o nome de teste.jpg.

### Aprimoramentos futuros
- Aplicar aprendizado de máquina para melhor classificar os rostos
- Otimizar o código

## Executando o projeto

```console
python face_rec.py
```

## Após a execução do projeto é gerado um novo arquivo com nome de resultado.jpg

Abaixo é possível visualizar "antes e depois" da classificação de rosto.

**Antes**
![alt text](https://github.com/rodrigosarri/face-recognition/blob/main/tests/donald-trump.jpg?raw=true)

**Depois**
![alt text](https://github.com/rodrigosarri/face-recognition/blob/main/results/donald-trump.jpg?raw=true)


## Contribuindo
Solicitações pull são bem-vindas. Para mudanças importantes, abra um problema primeiro para discutir o que você gostaria de mudar.

Certifique-se de atualizar os testes conforme apropriado.

## Licença
[MIT](https://choosealicense.com/licenses/mit/)