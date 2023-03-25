#! /usr/bin/python3
import rospy
from nav_msgs.msg import Odometry


def callback(data):
    # Write odometry data to file
    with open("/home/q/workspace/src/LIO-SAM/data/liosam_odometry.txt", "a") as f:
        f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(rospy.Time.now(), data.pose.pose.position.x,
                                                              data.pose.pose.position.y, data.pose.pose.position.z,
                                                              data.pose.pose.orientation.x,
                                                              data.pose.pose.orientation.y,
                                                              data.pose.pose.orientation.z,
                                                              data.pose.pose.orientation.w, data.twist.twist.linear.x))


def listener():
    rospy.init_node('liosam_odometry_listener', anonymous=True)

    rospy.Subscriber('lio_sam/mapping/odometry', Odometry, callback)

    rospy.spin()


if __name__ == '__main__':
    listener()
