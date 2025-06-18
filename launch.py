from launch import LaunchDescription
from launch_ros.actions import Node
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sf_v2x_com',
            namespace='receiver',
            executable='receiver',
            name='sf_v2x_com'
        ),
        Node(
            package='sf_env',
            namespace='env_model',
            executable='env_model',
            name='sf_env'
        ),
        Node(
            package='sf_localization',
            namespace='sf_ego_localization',
            executable='sf_ego_localization',
            name='sf_localization'
        ),
        Node(
            package='sf_v2x_server',
            namespace='cam_server',
            executable='cam_server',
            name='sf_v2x_server'
        ),
        Node(
            package='sf_spot_request',
            namespace='spot_request',
            executable='spot_request',
            name='sf_spot_request'
        ),
        Node(
            package='ydlidar',
            namespace='ydlidar_node',
            executable='ydlidar_node',
            name='ydlidar' 
        ),
        Node(
            package='ros2_pcan',
            namespace='ros2pcan_node',
            executable='ros2pcan_node',
            name='ros2_pcan' 
        ),
        Node(
            package='sf_model_city_map',
            namespace='sf_viz_ego',
            executable='sf_viz_ego',
            name='sf_model_city_map' 
        ),
        Node(
            package='sf_model_city_map',
            namespace='sf_viz_cars',
            executable='sf_viz_cars',
            name='sf_model_city_map' 
        ),
        Node(
            package='sf_traffic_monitor',
            namespace='traffic_monitor',
            executable='traffic_monitor',
            name='sf_traffic_monitor' 
        )
    ])