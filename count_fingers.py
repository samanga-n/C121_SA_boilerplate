import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

tipIds = [4, 8, 12, 16, 20]

def countFingers(image, hand_landmarks, handNo=0):
    if hand_landmarks:
        # Get all Landmarks of the FIRST Hand VISIBLE
        
        # print(landmarks)
        
        # Count Fingers 
         
        for lm_index in tipIds:
             
             # Get Finger Tip and Bottom y Position Value
             
             
             # Get Thumb Tip and Bottom y Position Value
             
             
              # Check if ANY FINGER is OPEN or CLOSED
              
        
        # print(fingers)
        totalFingers = fingers.count(1)

        # Display Text
        text = f'Fingers: {totalFingers}'

def drawHandLanmarks(image, hand_landmarks):
      if hand_landmarks:

        for landmarks in hand_landmarks:
                
            mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)


while True:
    success, image = cap.read()
    
    image = cv2.flip(image, 1)
    
    # Detect the Hands Landmarks 
    results = hands.process(image)
    
     # Get landmark position from the processed result
    hand_landmarks = results.multi_hand_landmarks
    
    # Draw Landmarks
    drawHandLanmarks(image, hand_landmarks)
    
    # Get Hand Fingers Position        
    countFingers(image, hand_landmarks)

    
    

    cv2.imshow("Media Controller", image)

    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()

