#!/usr/bin/env python

import sys
import rospy
import copy, math

from moveit_commander import RobotCommander, MoveGroupCommander
from moveit_commander import PlanningSceneInterface, roscpp_initialize, roscpp_shutdown
from geometry_msgs.msg import PoseStamped
from moveit_msgs.msg import Grasp, GripperTranslation, PlaceLocation, MoveItErrorCodes
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import random

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
        count=0
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
        #print("Going to initial pose")
        #right_gripper.set_named_target("s0")
        #right_gripper.go(wait=True)
        # clean the scene
        #scene.remove_world_object("table")
        #scene.remove_world_object("part")
        right_gripper.set_named_target("open")
        right_gripper.go(wait=True)
        print("Going to default pose")
        right_arm.set_named_target("final1")
        right_arm.go(wait=True)
        # print("Going to initial pose")
        # right_arm.set_named_target("s4")
        # right_arm.go(wait=True)
      
        right_gripper.set_named_target("close")
        right_gripper.go(wait=True)

        rospy.sleep(1)
        # count=count+1
        # print("s2",count)
        # right_arm.set_named_target("s2")
        # right_arm.go(wait=True)

        # print("s3",count)
        # rospy.sleep(1)
        # right_arm.set_named_target("s3")
        # right_arm.go(wait=True)
        # rospy.sleep(1)


        
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
        print("end of pose")
        rospy.spin()
        roscpp_shutdown()
        
       
 

if __name__=='__main__':
    TestPick()

