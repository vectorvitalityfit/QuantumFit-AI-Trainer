import cv2
import numpy as np
from ultralytics import YOLO

class PoseDetector:
    def __init__(self,model_path):
        self.model=YOLO(model_path) # Load YOLOv8 pose model for pose detection
    def detect_poses(self,frame):
        results=self.model(frame)
        keypoints=[]
        for result in results: # Exract keypoints for each detected person
            if hasattr(result,'keypoints'): # Adjust for model's output format
                keypoints.append(result.keypoints.xy)
        return keypoints
    
    def draw_keypoints(self,frame,keypoints):
        for person_kp in keypoints: # Draw circles on keypoints
            for x,y in person_kp:
                cv2.circle(frame,(int(x),int(y)),5,(0,255,0),-1)
        return frame
    
def main():
    cap=cv2.VideoCapture(0)
    detector=PoseDetector('model_weights/yolov8-post.pt')
    while True:
        ret,frame=cap.read()
        if not ret:
            break
        keypoints=detector.detect_pose(frame)
        frame=detector.draw_keypoints(frame,keypoints)
        cv2.imshow('Pose Detection',frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__=='__main__':
    main()

