from pykinect import nui
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
x = nui.Vector(10)
def skeleton_frame_ready(frame):
    skeletons = frame.SkeletonData
    for index,data in enumerate(skeletons):
           HR=data.SkeletonPositions[nui.JointId.HandRight]
           #HR.x,HR.y,HR.z,HR.w=HR.x/10,HR.y/10,HR.z/10,HR.w/10
           return HR
def skeleton_frame_ready__(frame):
    skeletons = frame.SkeletonData
    for index,data in enumerate(skeletons):
           HR=data.SkeletonPositions[nui.JointId.ShoulderRight]
           return HR

f = open('KinectXYZW.txt','w')
f.write("X\t\tY\t\tZ\t\tW\n\n")

skeletonX=list()
skeletonY=list()
skeletonZ=list()
skeletonW=list()
ran=list(i for i in range(0,630,10))
'''
ax = fig.add_subplot(1,1)
ay = fig.add_subplot(1,2)
az = fig.add_subplot(2,1)
aw = fig.add_subplot(2,2)
'''
with nui.Runtime() as kinect :
    i=0
    kinect.skeleton_engine.enabled=True
    while True:
        frame = kinect.skeleton_engine.get_next_frame()
        for skeleton in frame.SkeletonData:
           if skeleton.eTrackingState==nui.SkeletonTrackingState.TRACKED:
               i=i+1
               if i%10==0:
                   print skeleton_frame_ready(frame)
                  
                   '''skeletonX.append(skeleton.Position.x)
                   skeletonY.append(skeleton.Position.y)
                   skeletonZ.append(skeleton.Position.z)
                   skeletonW.append(skeleton.Position.w)'''
                   skeletonX.append( skeleton_frame_ready(frame).x)
                   skeletonY.append(skeleton_frame_ready(frame).y)
                   skeletonZ.append(skeleton_frame_ready(frame).z)
                   #skeletonW.append(skeleton_frame_ready(frame).w)
                   #f.write(str(skeletonX)+","+str(skeletonY)+","+str(skeletonZ)+","+str(skeletonW)+"\n")
                   #ani = animation.FuncAnimation(fig, animate, interval=1000)
                   plt.plot(skeletonX,'red')
                   #plt.subplot(111)
                   plt.plot(skeletonY,'blue')
                   #plt.subplot(112)
                   plt.plot(skeletonZ,'green')
                   #plt.subplot(121)    
                   #plt.plot(skeletonW,'black')
                   #plt.subplot(122)
                   plt.show()
                   #plt.close()

                   
'''                 if i==750:
                        print "ENOUGH !! :<"
                       
                        break
                    '''
with open('KinectXYZW.txt','w') as f:
    f.write("DataX\n")
    for i in skeletonX:
        f.write(str(i)+'\n')
    f.write("\n\n")
    f.write("DataY\n")
    for i in skeletonY:
        f.write(str(i)+'\n')
    f.write("\n\n")
    f.write("DataZ\n")
    for i in skeletonZ:
        f.write(str(i)+'\n')
    f.write("\n\n")
    f.write("DataW\n")
    for i in skeletonW:
        f.write(str(i)+'\n')
    f.write("\n\n")

        

                   
        
