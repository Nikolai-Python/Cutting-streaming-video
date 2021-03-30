import cv2

# Webcam Yuzhnoye Butovo (metro Skobelevskaya) in Moscow

cap = cv2.VideoCapture("http://cam.butovonet.ru/axis-cgi/mjpg/video.cgi?resolution=480x576&dummy=1460609511992")
success, image = cap.read()
count = 1
success = True

while success:
    cv2.imwrite("frame\\frame%d.jpg" % count, image)
    success, image = cap.read()
    print('Read a new frame: ', success)
    count += 1
    
    if count > 12:
        # 12 frames/15 seconds/3 minutes
        break
        
    if cv2.waitKey(15000) & 0xFF == ord('q'):
        break

# blob:https://matchtv.ru/224ed02c-178a-4830-a973-13ce7a575544