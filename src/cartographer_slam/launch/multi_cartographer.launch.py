from launch import LaunchDescription
from launch_ros.actions import Node
import os 
from ament_index_python.packages import get_package_share_directory
def generate_launch_description():
    cartographer_config_dir = os.path.join(get_package_share_directory('cartographer_slam'), 'config')

    configuration_basename="cartographer_multi.lua"
    cartographer= Node(
    package='cartographer_ros',
    executable='cartographer_node',
    name='cartographer_node',
    output='screen',
    parameters=[{'use_sim_time': True}],
    arguments=['-configuration_directory', cartographer_config_dir,
    '-configuration_basename', configuration_basename],
    remappings=[
            ('/cmd_vel', '/tb3_0/cmd_vel'),
            ('/odom', '/tb3_0/odom'),
            ('/scan', '/tb3_0/scan'),]
    
    )
    occupancy=Node(
    package='cartographer_ros',
    executable='cartographer_occupancy_grid_node',
    output='screen',
    name='occupancy_grid_node',
    parameters=[{'use_sim_time': True}],
    arguments=['-resolution', '0.05', '-publish_period_sec', '1.0']

    )
    return LaunchDescription([
        cartographer,
        occupancy
    ])