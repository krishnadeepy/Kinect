from pykinect import nui
import matplotlib.pyplot as plt

class body(object):
    def __init__(self):
        self.ankleL=nui.JointId.AnkleLeft
        self.ankleR=nui.JointId.AnkleRight
        self.elbowL=nui.JointId.ElbowLeft
        self.elbowR=nui.JointId.ElbowRight
        self.footL=nui.JointId.FootLeft
        self.footR=nui.JointId.FootRight
        self.handR=nui.JointId.HandRight
        self.handL=nui.JointId.HandLeft
        self.head=nui.JointId.Head
        self.hipC=nui.JointId.HipCenter
        self.hipL=nui.JointId.HipLeft
        self.hipR=nui.JointId.HipRight
        self.kneeL=nui.JointId.KneeLeft
        self.kneeR=nui.JointId.KneeRight
        self.shoulderC=nui.JointId.ShoulderCenter
        self.shoulderL=nui.JointId.ShoulderLeft
        self.shoulderR=nui.JointId.ShoulderRight
        self.spine=nui.JointId.Spine
        self.wristL=nui.JointId.WristLeft
        self.wristR=nui.JointId.WristRight

        
class bodypart(object):
    def __init__(self,*args):
        
        self.X=list()
        self.Y=list()
        self.Z=list()
        self.W=list()
        
    def getData(x):
        skeletons = frame.SkeletonData
        for index,data in enumerate(skeletons):
            partPOS=data.SkeletonPositions[x]
            return partPOS

    def data(self,part):
        X.append( skeleton_frame_ready(frame).x)
        skeletonY.append(skeleton_frame_ready(frame).y)
        skeletonZ.append(skeleton_frame_ready(frame).z)
        
    #def graph(self,):
human=body()
armR= bodypart(human.elbowR,human.shoulderR,human.wristR)

with nui.Runtime() as kinect :
    FrameCount = 0
    kinect.skeleton_engine.enabled=True
    while True:
        frame = kinect.skeleton_engine.get_next_frame()
        for skeleton in frame.SkeletonData:
           if skeleton.eTrackingState==nui.SkeletonTrackingState.TRACKED:
               FrameCount += 1
               if FrameCount%10==0:
                   
                   print arm.getData(arm.shoulderR)
                   
