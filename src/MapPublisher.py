#!/usr/bin/env python
# # license removed for brevity
import rospy
from std_msgs.msg import String
from ma_rrt_path_plan.msg import Map, Cone


def map_publisher():
    """Publish the Map message to the /map_topic topic"""
    pub = rospy.Publisher("/map_topic", Map, queue_size=1)
    rospy.init_node("map_publisher_node", anonymous=True)
    rate = rospy.Rate(1)  # 10hz
    while not rospy.is_shutdown():
        map_to_send = create_map()
        rospy.loginfo(map_to_send)
        pub.publish(map_to_send)
        rate.sleep()


def create_map() -> Map:
    """Creates a dummy map

    Returns:
        Map: the created dummy map
    """

    my_map = Map()

    # create a straight track consisting of 20 cones, separated by 1 meter each, width of 4 meter
    for i in range(10):
        # left side
        cone_left = Cone()
        cone_left.x = -2
        cone_left.y = i
        my_map.cones.append(cone_left)

        # right side
        cone_right = Cone()
        cone_right.x = 2
        cone_right.y = i
        my_map.cones.append(cone_right)

    return my_map


if __name__ == "__main__":
    try:
        map_publisher()
    except rospy.ROSInterruptException:
        pass