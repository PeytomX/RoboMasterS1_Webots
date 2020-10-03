"""S1_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor


# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

# ds = []
# dsNames = ['ds_right', 'ds_left']
# for i in range(2):
    # ds.append(robot.getDistanceSensor(dsNames[i]))
    # ds[i].enable(TIME_STEP)
# wheels = []
# wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
# for i in range(4):
   #  wheels.append(robot.getMotor(wheelsNames[i]))
   #  wheels[i].setPosition(float('inf'))
    # wheels[i].setVelocity(0.0)
# avoidObstacleCounter = 0
#class Camera ('camera'):
    #def enable(self, samplingPeriod):
    #def getSamplingPeriod(self):
    # ...
from controller import Robot, Motor, Camera, Keyboard, Mouse
# create the Robot instance.
robot = Robot()
# get the time step of the current world.
TIME_STEP = 64
print("请用键盘和鼠标控制RoboMaster S1:")
print("- 'W': 前进。")
print("- 'S': 后退。")
print("- 'D': 向右平移。")
print("- 'A': 向左平移。")
print("- '左': YAW逆时针旋转。")
print("- '右': YAW顺时针旋转。")
print("- '上': pitch轴抬高。")
print("- '下': pitch轴下降。")
keyboard = robot.getKeyboard()
keyboard.enable(10)
maincamera = robot.getCamera('camera') #获取相机
maincamera.enable(10) #开启相机，并定义刷新间隔为10ms
yawmotor = robot.getMotor('yaw_motor') #获取yaw轴电机
yawmotor.setPosition(float('inf')) #定义旋转位置为无穷远
yawmotor.setVelocity(0.0) #定义初始速度为0
pitchmotor = robot.getMotor('pitch_motor')
pitchmotor.setPosition(float('inf'))
pitchmotor.setVelocity(0.0)
wheels = []
wheelsNames = ['wheel_fl_motor', 'wheel_fr_motor', 'wheel_br_motor', 'wheel_bl_motor']
for i in range(4):
    wheels.append(robot.getMotor(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)
# 定义ID
# 1-------0
#     |
#     |
#     |
# 2-------3
# y
# |
# |
# -------->X   w为逆时针
Vx=0
Vy=0
w=0  
def Mecanum(Vx,Vy,w,i):  #速度解算子函数
    motorVelocity=[0,0,0,0]
    motorVelocity[0]=Vy-Vx+w
    motorVelocity[1]=Vy+Vx-w
    motorVelocity[2]=Vy-Vx-w
    motorVelocity[3]=Vy+Vx+w
    return motorVelocity[i]
    
while robot.step(TIME_STEP) != -1:
      # yawmotor.setVelocity(1.0)
      # pitchmotor.setVelocity(1.0)
      
      key=keyboard.getKey()
      if (key==ord('W')):
        Vy=5
        print('前进')
      if (key==ord('S')):
        Vy=-5
        print('后退')
      if (key==ord('A')):
        Vx=-5
        print('前进')  
      if (key==ord('D')):
        Vx=5
        print('前进')
      if (key==Keyboard.UP):
        pitchmotor.setVelocity(-1.0)
        print('pitch轴抬高')
      if (key==Keyboard.DOWN):
        pitchmotor.setVelocity(1.0)
        print('pitch轴下降')  
      if (key==Keyboard.LEFT):
        yawmotor.setVelocity(1.0)
        print('YAW逆时针旋转')  
      if (key==Keyboard.RIGHT):
        yawmotor.setVelocity(-1.0)
        print('YAW顺时针旋转')  
      if (key==-1):
        Vx=0
        Vy=0
        w=0
        pitchmotor.setVelocity(0)
        yawmotor.setVelocity(0)
        print('停止')
      # print(key)
      wheels[0].setVelocity(Mecanum(Vx,Vy,w,0))
      wheels[1].setVelocity(Mecanum(Vx,Vy,w,1))
      wheels[2].setVelocity(Mecanum(Vx,Vy,w,2))
      wheels[3].setVelocity(Mecanum(Vx,Vy,w,3))



#     leftSpeed = 1.0
#     rightSpeed = 1.0
#     if avoidObstacleCounter > 0:
#         avoidObstacleCounter -= 1
#         leftSpeed = 1.0
#         rightSpeed = -1.0
#     else:  # read sensors
#         for i in range(2):
#             if ds[i].getValue() < 950.0:
#                 avoidObstacleCounter = 100
#     wheels[0].setVelocity(leftSpeed)
#     wheels[1].setVelocity(rightSpeed)
#     wheels[2].setVelocity(leftSpeed)
#     wheels[3].setVelocity(rightSpeed)
