#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan


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



