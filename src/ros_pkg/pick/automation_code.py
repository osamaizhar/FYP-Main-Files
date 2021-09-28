#!/usr/bin/env python

import sys
import rospy
import copy, math
import serial

from moveit_commander import RobotCommander, MoveGroupCommander
from moveit_commander import PlanningSceneInterface, roscpp_initialize, roscpp_shutdown
from geometry_msgs.msg import PoseStamped
from moveit_msgs.msg import Grasp, GripperTranslation, PlaceLocation, MoveItErrorCodes
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import random
arduino=serial.Serial("/dev/ttyUSB0",9600)

def serial():
    serial.x=arduino.readline()
    try:
        serial.x = serial.x.decode('ascii').strip()
    except UnicodeDecodeError:
        print("Garbage value")
        pass
    print(serial.x)
    #return(x)

ROBOT_NAME = "six_dof_arm"

if ROBOT_NAME == "six_dof_arm":
    GROUP_NAME_ARM ='arm'
    GROUP_NAME_GRIPPER ='gripper'

    GRIPPER_FRAME = 'claw_base'

    FIXED_FRAME = 'base_link'

    GRIPPER_CLOSED = 0.3
    GRIPPER_OPEN = 0.0

    GRIPPER_JOINT_NAMES = ['finger_joint1','finger_joint2']
   
    GRIPPER_EFFORT = [1.0]

class TestPick():
    def __init__(self):
        roscpp_initialize(sys.argv)
        rospy.init_node('moveit_py_demo', anonymous=True)
      
        scene = PlanningSceneInterface()
        robot = RobotCommander()
       
        right_arm = MoveGroupCommander(GROUP_NAME_ARM)
        right_gripper = MoveGroupCommander(GROUP_NAME_GRIPPER)
        #right_arm.set_goal_position_tolerance(0.005)
        right_arm.set_goal_orientation_tolerance(0.005)
	right_arm.set_planning_time(5)
	right_arm.set_num_planning_attempts(5) 
        gripper = right_arm.get_end_effector_link()

        rospy.sleep(2)
        # Allow replanning to increase the odds of a solution
        right_arm.allow_replanning(True)
        #scene.remove_attached_object(GRIPPER_FRAME, "part")

   
        # clean the scene
        #scene.remove_world_object("table")
        #scene.remove_world_object("part")
        #serial()
        #if serial.x=="Counter Reset":
            #print("connected!!")
        while True:
            serial()
            
            right_gripper.set_named_target("open")
            right_gripper.go(wait=True)
            print("going to pickup pose")
            right_arm.set_named_target("p1")
            right_arm.go(wait=True)
        
            rospy.sleep(1)    

            if serial.x=="Counter Reset":
                right_gripper.set_named_target("close")
                right_gripper.go(wait=True)
                print("p2")
                right_arm.set_named_target("p2")
                right_arm.go(wait=True)

                print("p3")
                rospy.sleep(1)
                right_arm.set_named_target("p3")
                right_arm.go(wait=True)
                right_gripper.set_named_target("open")
                right_gripper.go(wait=True)
                rospy.sleep(1)

                
                #right_gripper.set_named_target("open")
                #right_gripper.go(wait=True)
            
                #rospy.sleep(1)
        
            
                #start_pose = PoseStamped()
                #start_pose.header.frame_id = FIXED_FRAME
            
                #rospy.sleep(1)
                



            #right_arm.set_pose_target(next_pose)
                #right_gripper.set_named_target("close")
                #right_gripper.go(wait=True)

                #rospy.sleep(1)

                #right_arm.set_named_target("straight leg")
                #right_arm.go(wait=True)
                #print("end of pose")
                #rospy.spin()
                #roscpp_shutdown()
        
       
 

if __name__=='__main__':
    TestPick()

