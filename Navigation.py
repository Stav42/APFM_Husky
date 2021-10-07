#!/usr/bin/env python3
import rospy
import math
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

class point:
    def __init__:
        self.x = None
        self.y = None

    def _set_x(x,y):
        self.x = x
        self.y = y

def optimizer(goal, curr, ranges)

def angle(point1, point2):
    trig = (point2.y - point1.y)/(point2.x - point1.x)
    return math.atan(trig)

def euler(curr):
    orientation_q = curr.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion(orientation_list)
    return yaw

def callback(data):
    flag = 0
    for index, entry in enumerate(data.ranges):
        if(index>300 and index<=420 and entry!=float('inf') and entry!=float('-inf')):
            flag=1
            break
    if flag:
        rospy.loginfo("Can see an object")
    else:
        rospy.loginfo("Can't see nothin")
    
def listener():

    rospy.init_node('Scan_counter', anonymous=True)

    rospy.Subscriber("scan", LaserScan , callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()



def optimizer(goal, curr, ranges):
    """
        Input Type: 
        curr - Odometry: pose
        goal - Point(x, y)
        ranges - LaserScan.ranges - Array of size 1x720 covering FOV from -135 degrees to 135 degrees
    """

    cost1 = theta - angle(goal, curr)
    cost2 = C2*potential_range
    cost3 = theta - euler(curr)

    optimize

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    listener()



