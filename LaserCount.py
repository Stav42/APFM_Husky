#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

def callback(data):
    count = 0
    for entry in data.ranges:
        if(entry!=float("inf") and entry!=float('-inf')):
            count+=1
    rospy.loginfo("Length of data is %d and number of non-inf is: %d", len(data.ranges), count)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('Scan_counter', anonymous=True)

    rospy.Subscriber("scan", LaserScan , callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
