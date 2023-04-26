import cv2
import mediapipe as mp
from pynput.keyboard import Key, Controller
import pyautogui
keyboard = Controller()

cap = cv2.VideoCapture(0)

width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
height  = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

tipIds = [4, 8, 12, 16, 20]


# Define una función para contar los dedos.
def countFingers(image, hand_landmarks, handNo=0):

    
        totalFingers = fingers.count(1)
        
        # REPRODUCE o PAUSA un video
        if totalFingers == 4:
            state = "Play"

        if totalFingers == 0 and state == "Play":
            state = "Pause"
            keyboard.press(Key.space)


        
        finger_tip_y = (landmarks[8].y)*height
        if totalFingers == 2:
            if  finger_tip_y < height-400:
                print("Disminuir volumen")
                pyautogui.press("volumedown")

            if finger_tip_y > height-50:
                print("Incrementar volumen")
                pyautogui.press("volumeup")
        
        # ADELANTA o REGRESA el video    
        finger_tip_x = (landmarks[8].x)*width        
         
        ################################

             # AGREGACÓDIGO AQUÍ #

        ################################ 

# Dedina una función para 

               
        mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)



while True:
    success, image = cap.read()

    image = cv2.flip(image, 1)
    
    # Detecta los puntos de referencia en las manos 
    results = hands.process(image)

    # Obtén la posición del punto de referencia del resultado procesado
    hand_landmarks = results.multi_hand_landmarks

    

    # Sal de la ventana al presionar la barra espaciadora
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
