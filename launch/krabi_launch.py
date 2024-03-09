from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
import os
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution, TextSubstitution
from launch.substitutions import Command, LaunchConfiguration, PythonExpression

def generate_launch_description():
    isBlue_value = LaunchConfiguration('isBlue')
    xRobotPos_value = LaunchConfiguration('xRobotPos')
    yRobotPos_value = LaunchConfiguration('yRobotPos')
    zRobotOrientation_value = LaunchConfiguration('zRobotOrientation')
    
    isBlue_launch_arg = DeclareLaunchArgument(
        'isBlue',
        default_value='false'
    )
    xRobotPos_launch_arg = DeclareLaunchArgument(
        'xRobotPos',
        default_value='1.25'
    )
    yRobotPos_launch_arg = DeclareLaunchArgument(
        'yRobotPos',
        default_value='0.5'
    )
    zRobotOrientation_launch_arg = DeclareLaunchArgument(
        'zRobotOrientation',
        default_value='0.0'
    )


    return LaunchDescription([isBlue_launch_arg, xRobotPos_launch_arg, yRobotPos_launch_arg, zRobotOrientation_launch_arg,
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('krabi_bringup'),
                    'launch',
                    'krabi_simu_launch.py'
                ])
            ])
            ,launch_arguments={
                'isBlue': isBlue_value,
                'xRobotPos': xRobotPos_value,
                'yRobotPos': yRobotPos_value,
                'zRobotOrientation_value': zRobotOrientation_value
            }.items()
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('krabi_bringup'),
                    'launch',
                    'krabi_main_launch.py'
                ])
            ])
            #,launch_arguments={
            #    'turtlesim_ns': 'turtlesim2',
            #    'use_provided_red': 'True',
            #    'new_background_r': TextSubstitution(text=str(colors['background_r']))
            #}.items()
        )
    
        
    ])