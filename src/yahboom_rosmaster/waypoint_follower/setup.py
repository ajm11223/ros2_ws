from setuptools import setup
import os
from glob import glob

package_name = 'waypoint_follower'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
         glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ajm',
    maintainer_email='ajm1122383@gmail.com',
    description='Waypoint follower for mecanum-wheel robot',
    license='BSD-3-Clause',
    entry_points={
        'console_scripts': [
            'waypoint_follower = waypoint_follower.waypoint_follower_node:main',
            'gz_pose_tf_publisher = waypoint_follower.gz_pose_tf_publisher:main',
            'keyboard_teleop = waypoint_follower.keyboard_teleop_node:main',
        ],
    },
)
