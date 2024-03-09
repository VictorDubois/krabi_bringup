from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
import os
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution, TextSubstitution

def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('main_strategy'),
                    'launch',
                    'main_strat_launch.py'
                ])
            ])
            #,launch_arguments={
            #    'turtlesim_ns': 'turtlesim2',
            #    'use_provided_red': 'True',
            #    'new_background_r': TextSubstitution(text=str(colors['background_r']))
            #}.items()
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('goal_strategy'),
                    'launch',
                    'goal_strat_launch.py'
                ])
            ])
            #,launch_arguments={
            #    'turtlesim_ns': 'turtlesim2',
            #    'use_provided_red': 'True',
            #    'new_background_r': TextSubstitution(text=str(colors['background_r']))
            #}.items()
        )
    
        
    ])