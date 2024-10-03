import cv2
from ultralytics import YOLO, solutions

model = YOLO("yolo11n.pt")
names = model.model.names

cap = cv2.VideoCapture("/Users/glenn/speed_estimator yolo/speed_esti_yolov11/4261469-uhd_2560_1440_25fps.mp4")
assert cap.isOpened(), "Error reading the file"