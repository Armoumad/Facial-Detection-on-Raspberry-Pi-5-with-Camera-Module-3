#!/usr/bin/env python3

import cv2
import mediapipe as mp
import time
from picamera2 import Picamera2

# Initialiser MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

# Initialiser la caméra
picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (640, 480)})
picam2.configure(config)
picam2.start()

print("Démarrage de la détection faciale avec MediaPipe...")

try:
    while True:
        # Capturer une image
        frame = picam2.capture_array()
        
        # Convertir l'image de BGR à RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Traiter l'image avec MediaPipe
        results = face_detection.process(rgb_frame)
        
        # Compter les visages détectés
        face_count = 0
        
        # Dessiner les détections
        if results.detections:
            for detection in results.detections:
                face_count += 1
                
                # Obtenir les coordonnées du cadre du visage
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                             int(bboxC.width * iw), int(bboxC.height * ih)
                
                # Dessiner un rectangle autour du visage
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                # Afficher le score de confiance
                cv2.putText(frame, f'Confiance: {int(detection.score[0] * 100)}%', 
                            (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Afficher le nombre de visages détectés
        cv2.putText(frame, f'Visages detectes: {face_count}', (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Afficher le résultat
        cv2.imshow('Detection Faciale avec MediaPipe', frame)
        
        # Sortir avec la touche 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        time.sleep(0.01)  # Petit délai pour réduire l'utilisation CPU

except KeyboardInterrupt:
    print("Arrêt de la détection...")
finally:
    cv2.destroyAllWindows()
    picam2.stop()
    face_detection.close()
    print("Programme terminé.")
