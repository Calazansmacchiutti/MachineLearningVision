import math
import torch
import cv2 as cv
import numpy as np
from ultralytics import YOLO
import datetime
import os

# Verifica se a GPU está disponível e carrega o modelo YOLOv8n
if torch.cuda.is_available():
    model = YOLO("yolov8n.pt").to("cuda")
else:
    model = YOLO("yolov8n.pt").to("cpu")

# Nomes das classes do modelo YOLOv8n
class_names = model.names  # Obtém os nomes das classes diretamente do modelo

# Lista de objetos proibidos que você deseja detectar
objetos_proibidos = ["cell phone", "laptop", "book"]  # Ajuste conforme necessário

# Cores para as classes
color_permitido = (0, 255, 0)  # Verde para objetos permitidos
color_proibido = (0, 0, 255)   # Vermelho para objetos proibidos

# Certifique-se de que a pasta 'detecções' existe
if not os.path.exists('detecções'):
    os.makedirs('detecções')

# Configurar a captura de vídeo da webcam
webcam_capture = cv.VideoCapture(0)
webcam_capture.set(3, 800)   # Largura
webcam_capture.set(4, 600)   # Altura

if not webcam_capture.isOpened():
    print("Erro ao abrir a webcam.")
    exit()

while True:
    # Ler a imagem da webcam
    ret, img = webcam_capture.read()
    if not ret:
        print("Falha ao capturar a imagem.")
        break

    # Fazer a inferência com o modelo YOLO
    results = model(img)
    detections = results[0]
    if detections:
        boxes = detections.boxes
        for box in boxes:
            # Obter a classe detectada
            classe = int(box.cls.item())
            class_name = class_names[classe]

            # Obter coordenadas da caixa delimitadora
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Obter a confiança
            confidence = round(box.conf.item(), 2)

            # Verificar se é um objeto proibido
            if class_name in objetos_proibidos:
                color = color_proibido

                # Desenhar a caixa delimitadora para objetos proibidos
                cv.rectangle(img, (x1, y1), (x2, y2), color, 2)

                # Desenhar o texto com a classe e a confiança
                cv.putText(
                    img,
                    f"{class_name}: {confidence}",
                    (x1, y1 - 10),
                    cv.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    color,
                    2
                )

                # Emitir alerta sonoro (opcional)
                # winsound.Beep(1000, 500)  # Frequência e duração em milissegundos (Windows)
                # os.system('play -nq -t alsa synth 0.5 sine 1000')  # (Linux/macOS)

                # Salvar imagem da detecção
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                cv.imwrite(f"detecções/deteccao_{class_name}_{timestamp}.jpg", img)

                # Registrar detecção em um arquivo de log
                with open("log_deteccoes.txt", "a") as log_file:
                    log_file.write(f"{timestamp}: {class_name} detectado com confiança {confidence}\n")
            else:
                # Cor para objetos permitidos
                color = color_permitido

                # Desenhar a caixa delimitadora para objetos permitidos
                cv.rectangle(img, (x1, y1), (x2, y2), color, 2)

                # Desenhar o texto com a classe e a confiança
                cv.putText(
                    img,
                    f"{class_name}: {confidence}",
                    (x1, y1 - 10),
                    cv.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    color,
                    2
                )

    # Exibir a imagem na janela
    cv.imshow('Detecção de Objetos', img)

    # Verificar se a tecla 'q' foi pressionada para sair
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a webcam e fechar as janelas
webcam_capture.release()
cv.destroyAllWindows()
