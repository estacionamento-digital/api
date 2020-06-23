# API da cancela

Criado uma API em Python para controlar a cancela feita em Arduino e receber atualizações do Firebase para abrir ou fechar a cancela.

## Requisitos
- Python 3 ou superior
- Módulos pyserial e firebase-admin

Instalação do pyserial:
```
pip install pyserial
```

Instalação do firebase-admin:
```
pip install firebase-admin
```

## Como usar
Alterar a porta que seu Arduino está utilizando:
```
arduino = serial.Serial('PORTA', 9600)
```

Alterar o certificado em JSON gerado no Firebase:
```
cred = credentials.Certificate("Arquivo")
```
