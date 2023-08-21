import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

def landMarks(img, hand_LM):
    if hand_LM: 
        print('xyz')
        for landmark in hand_LM:
            print(landmark)
            mp_draw.draw_landmarks(img, landmark, mp_hands.HAND_CONNECTIONS)


while True:
    success, image = cap.read()
    image = cv2.flip(image, 1)
    results = hands.process(image)
    print(results)

    hand_LM = results.multi_hand_landmarks 
    print(hand_LM)
    
    landMarks(image, hand_LM)
    cv2.imshow("Media Controller", image)

    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()
