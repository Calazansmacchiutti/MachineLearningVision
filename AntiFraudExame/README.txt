# ExamShield - Sistema de Detecção de Objetos Proibidos em Provas

Este projeto, **ExamShield**, utiliza o modelo YOLOv8 e OpenCV para detectar objetos em tempo real, destacando objetos proibidos durante provas, como celulares, laptops, livros e outros dispositivos eletrônicos.

## **Descrição**

O programa captura vídeo da webcam e aplica o modelo YOLOv8 para detectar objetos em cada frame. Todos os objetos identificados são exibidos, porém os objetos proibidos são destacados em vermelho, enquanto os objetos permitidos são mostrados em verde. Quando um objeto proibido é detectado, o sistema pode emitir alertas sonoros, salvar imagens das detecções e registrar informações em um log.

## **Funcionalidades**

- **Detecção em Tempo Real:** Identifica e exibe todos os objetos detectados pela câmera.
- **Destaque de Objetos Proibidos:** Objetos proibidos são destacados em vermelho, enquanto os permitidos são exibidos em verde.
- **Alertas Sonoros e Visuais:** Emite alertas quando um objeto proibido é detectado.
- **Registro de Detecções:** Salva imagens e logs das detecções com data e hora.
- **Personalização:** Permite adicionar ou remover objetos proibidos conforme necessário.

## **Pré-requisitos**

- **Python 3.7** ou superior
- **Bibliotecas Python:**
  - torch
  - ultralytics
  - opencv-python
  - numpy

## **Instalação**

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu_usuario/examshield.git
   cd examshield
