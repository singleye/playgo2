import cv2
import sys

net_if = sys.argv[1]

gstreamer_src = f"udpsrc address=230.1.1.1 port=1720 multicast-iface={net_if} ! application/x-rtp, media=video, encoding-name=H264 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! video/x-raw,width=1280,height=720,format=BGR ! appsink drop=1"

cap = cv2.VideoCapture(gstreamer_src, cv2.CAP_GSTREAMER)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print('Read frame error')
        continue
    cv2.imshow('go2', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        print('Bye!')
        break

cap.release()
cv2.destroyAllWindows()
