"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Keyboard
from controller import DistanceSensor
from controller import Camera

speed=4

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 64

keyboard=Keyboard()
keyboard.enable(timestep)

wheel1_left=robot.getDevice("wheel1_left")
wheel1_left.setPosition(float("inf"))
wheel1_left.setVelocity(0.0)

wheel2_left=robot.getDevice("wheel2_left")
wheel2_left.setPosition(float("inf"))
wheel2_left.setVelocity(0.0)

wheel1_right=robot.getDevice("wheel1_right")
wheel1_right.setPosition(float("inf"))
wheel1_right.setVelocity(0.0)

wheel2_right=robot.getDevice("wheel2_right")
wheel2_right.setPosition(float("inf"))
wheel2_right.setVelocity(0.0)

ds1=robot.getDevice("ds1")
ds2=robot.getDevice("ds2")
ds1.enable(timestep)
ds2.enable(timestep)

cam_slider=robot.getDevice("cam_slider")
cam=robot.getDevice("camera")
cam.enable(timestep)


# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    key_pressed=keyboard.getKey()
    print("which key is clicked:",key_pressed)
    #a
    if(key_pressed==65):
        wheel1_left.setVelocity(-speed)
        wheel1_right.setVelocity(speed)
        wheel2_left.setVelocity(-speed)
        wheel2_right.setVelocity(speed)
        #d
    if(key_pressed==68):
        wheel1_left.setVelocity(speed)
        wheel1_right.setVelocity(-speed)
        wheel2_left.setVelocity(speed)
        wheel2_right.setVelocity(-speed)
        
        #w
    if(key_pressed==87):
        wheel1_left.setVelocity(speed)
        wheel1_right.setVelocity(speed)
        wheel2_left.setVelocity(speed)
        wheel2_right.setVelocity(speed)
        
        #s
    if(key_pressed==83):
        wheel1_left.setVelocity(-speed)
        wheel1_right.setVelocity(-speed)
        wheel2_left.setVelocity(-speed)
        wheel2_right.setVelocity(-speed)
        
        #w
    if(key_pressed==-1):
        wheel1_left.setVelocity(0.0)
        wheel1_right.setVelocity(0.0)
        wheel2_left.setVelocity(0.0)
        wheel2_right.setVelocity(0.0)
   
    

# Enter here exit cleanup code.a



