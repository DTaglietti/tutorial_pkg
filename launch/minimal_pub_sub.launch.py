from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    return LaunchDescription([
        Node(
            package='tutorial_pkg',
            executable='minimal_publisher',   # nome console_script
            name='minimal_publisher',
            output='screen',
        ),
        Node(
            package='tutorial_pkg',
            executable='minimal_subscriber', # nome console_script
            name='minimal_subscriber',
            output='screen',
        ),
    ])
