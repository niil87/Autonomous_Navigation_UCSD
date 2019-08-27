print("Hello!!")
import numpy as np

print("The good thing about Px approach is that we can use P only to get initial detection, and then number using same size/angle/etc")

print("For our model, we will break down the possible image sizes starting with 0.5 Feet and spacing each image 1 feet apart\nThe image size is about 1 Feet with ")

letterLength = 10.0 # cm, this will be square grid type per character
Separation = 20.0 #cm
initialLength = 10.0 #cm
heightCamera = 30.0 #cm, roughly 1 feet off ground

AffectiveLength = []
for i in range (0,10) :
    Theta = np.arctan((i*Separation + initialLength)/(0.5*letterLength))
    ObservedLength = 2*initialLength/np.tan(Theta)
    AffectiveLength.append(ObservedLength)
    if ObservedLength > 1.0 :
        print ("Letter length value at distance from observation:" + str(i*Separation + initialLength) + " is:" + str(ObservedLength))
    #else :
        #print ("letter length size too small to be considered:" str(ObservedLength))

print ("there will be vertical compression but horizontal will stay same if image allowed to be placed on floor\nWe will rely on Angle of observation to determine the related length.")

Ratio = letterLength/np.tan(letterLength/(2*initialLength))
print ("Ratio:",Ratio)

EffectiveFloorLength = []
for i in range(0,10) :
    minAngle = np.tan((initialLength-(AffectiveLength[i]/2))/(heightCamera))
    maxAngle = np.tan((initialLength+(AffectiveLength[i]/2))/(heightCamera))
    diffAngle = maxAngle - minAngle
    FloorLength = Ratio*diffAngle
    EffectiveFloorLength.append(FloorLength)
    if FloorLength > 1.0 :
        print ("Letter Floor length value at distance from observation:" + str(i*Separation + initialLength) + " is:" + str(FloorLength))
    #else :
        #print ("letter length size too small to be considered:" str(FloorLength))

print ("Now time for final numbers of compression rations for different images.")
for i in range(0,10) :
    if EffectiveFloorLength[i] > 1.0 :
        HorizontalScale = np.around(AffectiveLength[i]/10.0,decimals=2)
        VerticalScale = np.around(EffectiveFloorLength[i]/10.0,decimals=2)
        print("Final Scaling Factor!! Horizonatal:" + str(HorizontalScale) + ", Vertical:" + str(VerticalScale))
