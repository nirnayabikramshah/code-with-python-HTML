import cv2
cap = cv2.VideoCapture(0)           # 0 = webcam, or 'video.mp4'
while True:
    ret, frame = cap.read()
    if not ret: break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
perim = cv2.arcLength(cnt, True)
cv2.destroyAllWindows()