#!/usr/bin/env python
import rospy
import moveit_commander
import time
from tf import transformations
from geometry_msgs.msg import Pose
rospy.init_node( 'move' )
robot = moveit_commander.RobotCommander()
ur_group = moveit_commander.MoveGroupCommander('manipulator')
print "============ Reference frame: %s" % ur_group.get_planning_frame()
print "============ End effector frame: %s" % ur_group.get_end_effector_link()
print "============ Robot Groups: %s" % ", ".join(robot.get_group_names())
print "============ Printing robot state"
print robot.get_current_state()
print "============ Current cartesian pose: %s" % ur_group.get_current_pose()
print "============ Current joint values: %s" % ur_group.get_current_joint_values()

print "Safe point"
safe_point = [2.35, -2, 0.69, -0.69, -1.57, 0]
ur_group.set_joint_value_target(safe_point)
rospy.loginfo( 'Planning movement' )
plan = ur_group.plan()
rospy.loginfo( 'Executing pl1an' )
ur_group.execute( plan )
raw_input('Pause')

rep=5

for i in range (rep):

	print "PICK"
	pick_arriba = [0, 0, 1,-2.36, 1.57, 0]
	ur_group.set_pose_target(pick_arriba)
	plan = ur_group.plan()
	ur_group.execute( plan )

	pick_abajo = [0, 0, 0.85,-2.36, 1.57, 0]
	ur_group.set_pose_target(pick_abajo)
	plan = ur_group.plan()
	ur_group.execute( plan )

	time.sleep(2)

	ur_group.set_pose_target(pick_arriba)
	plan = ur_group.plan()
	ur_group.execute( plan )

	print "Place"
	place_arriba = [0.5, 0.7, 1,-2.36, 1.57, 0]
	ur_group.set_pose_target(place_arriba)
	plan = ur_group.plan()
	ur_group.execute( plan )

	place_abajo = [0.5, 0.7, 0.85,-2.36, 1.57, 0]
	ur_group.set_pose_target(place_abajo)
	plan = ur_group.plan()
	ur_group.execute( plan )

	time.sleep(2)

	ur_group.set_pose_target(place_arriba)
	plan = ur_group.plan()
	ur_group.execute( plan )

print "Safe point"
safe_point = [2.35, -2, 0.69, -0.69, -1.57, 0]
ur_group.set_joint_value_target(safe_point)
rospy.loginfo( 'Planning movement' )
plan = ur_group.plan()
rospy.loginfo( 'Executing pl1an' )
ur_group.execute( plan )