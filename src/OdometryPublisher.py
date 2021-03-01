#!/usr/bin/env python
# # license removed for brevity
import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovariance, TwistWithCovariance


def odometry_publisher():
    """Publishes an Odometry message to the /odometry topic"""

    pub = rospy.Publisher("/odometry", Odometry, queue_size=1)
    rospy.init_node("map_publisher_node", anonymous=True)
    rate = rospy.Rate(0.5)  # 10hz
    while not rospy.is_shutdown():
        odometry_to_send = create_odometry()
        rospy.loginfo(odometry_to_send)
        pub.publish(odometry_to_send)
        rate.sleep()


def create_odometry() -> Odometry:
    """Creates A dummy Odometry object

    Returns:
        Odometry: A dummy Odometry object
    """

    # create dummy odometry object
    my_odometry = Odometry()

    return my_odometry


if __name__ == "__main__":
    try:
        odometry_publisher()
    except rospy.ROSInterruptException:
        pass