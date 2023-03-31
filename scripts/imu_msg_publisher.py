#!/usr/bin/env python
# license removed for brevity
import rospy
from sensor_msgs.msg import Imu

def talker():
    rospy.init_node('imu_msg_pub', anonymous=True)
    imu_topic = rospy.get_param('~imu_topic', '/imu/data_raw')
    pub = rospy.Publisher(imu_topic, Imu, queue_size=1)
    world_frame = rospy.get_param('~world_frame', 'world')
    rate = rospy.Rate(100) # 100hz
    imu = Imu()
    while not rospy.is_shutdown():
        imu.header.stamp = rospy.Time.now()
        imu.header.frame_id = world_frame
        imu.linear_acceleration.z = 9.81
        pub.publish(imu)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
