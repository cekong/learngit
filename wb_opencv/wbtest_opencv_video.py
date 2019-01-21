import cv2
videocapture=cv2.VideoCapture('/home/deepl/Documents/wb/opencv-3.0.0/samples/data/tree.avi')
fps=videocapture.get(cv2.CAP_PROP_FPS)
size=(int(videocapture.get(cv2.CAP_PROP_FRAME_WIDTH)),int(videocapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videowriter=cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('I','4','2','0'),fps,size)
success,frame=videocapture.read()
c=0
while success:
    videowriter.write(frame)
    success,frame=videocapture.read()
    c=c+1
    print(c)

