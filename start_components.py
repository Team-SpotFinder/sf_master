import PySimpleGUI as sg
import os
import subprocess

def func(message):
    print(message)

layout = [[sg.Button('sf_env')],
          [sg.Button('sf_localization')],
          [sg.Button('sf_model_city_map')],
          [sg.Button('sf_driving_controller')],
          [sg.Button('sf_path_plan')],
          [sg.Button('sf_traffic_monitor')],
          [sg.Button('sf_ui')],
          [sg.Button('sf_v2x_com')],
          [sg.Button('sf_v2x_server')],
          [sg.Button('detectnet')],
          [sg.Button('cam_server')],
        ]

window = sg.Window("Spotfinder").Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    if event in (None, 'Exit'):
        break

    elif event == 'sf_env':
        print("sf_env")
        layout[0][0].update(disabled=True)
        command="ros2 run sf_env env_model"
        os.system("gnome-terminal --title=Env-Model -e 'bash -c \""+command+";bash\"'")

        command="ros2 run ydlidar ydlidar_node"
        os.system("gnome-terminal --title=YDLIDAR -e 'bash -c \""+command+";bash\"'")

    elif event == 'sf_localization':
        print("sf_localization")
        layout[1][0].update(disabled=True)
        command="ros2 run sf_localization sf_ego_localization"
        os.system("gnome-terminal --title=Localization -e 'bash -c \""+command+";bash\"'")

    elif event == 'sf_model_city_map':
        print("sf_model_city_map")
        layout[2][0].update(disabled=True)
        command="ros2 run sf_model_city_map sf_viz_ego"
        os.system("gnome-terminal --title=Viz-Ego -e 'bash -c \""+command+";bash\"'")

        command="ros2 run sf_model_city_map sf_viz_cars"
        os.system("gnome-terminal --title=Viz-Cars -e 'bash -c \""+command+";bash\"'")

    elif event == 'sf_driving_controller':
        print("sf_driving_controller")
        layout[3][0].update(disabled=True)
        command="ros2 run sf_driving_controller driving_controller"
        os.system("gnome-terminal --title=Driving-Controller -e 'bash -c \""+command+";bash\"'")

        command="ros2 run ros2_pcan ros2pcan_node"
        os.system("gnome-terminal --title=Pcan -e 'bash -c \""+command+";bash\"'")

    elif event == 'sf_path_plan':
        print("sf_path_planning")
        layout[4][0].update(disabled=True)
        command="ros2 run sf_path_plan path_planning"
        os.system("gnome-terminal --title=Path-Plan -e 'bash -c \""+command+";bash\"'")

    elif event == 'sf_traffic_monitor':
        print("sf_traffic_monitor")
        layout[5][0].update(disabled=True)
        command="ros2 run sf_traffic_monitor traffic_monitor"
        os.system("gnome-terminal --title=Traffic-Monitor -e 'bash -c \""+command+";bash\"'")

    elif event == 'sf_ui':
        print("sf_ui")
        layout[6][0].update(disabled=True)
        command="ros2 run sf_ui ui"
        os.system("gnome-terminal --title=UI -e 'bash -c \""+command+";bash\"'")

    elif event == 'sf_v2x_com':
        print("sf_v2x_com")
        layout[7][0].update(disabled=True)
        command="ros2 run sf_v2x_com receiver"
        os.system("gnome-terminal --title=Com-Receiver -e 'bash -c \""+command+";bash\"'")

        command="ros2 run sf_v2x_com transmitter"
        os.system("gnome-terminal --title=Com-Transmitter -e 'bash -c \""+command+";bash\"'")

    elif event == 'sf_v2x_server':
        print("sf_v2x_server")
        layout[8][0].update(disabled=True)
        command="ros2 run sf_v2x_server v2x_server"
        os.system("gnome-terminal --title=V2x-Server -e 'bash -c \""+command+";bash\"'")

    elif event == 'detectnet':
        print("realsense")
        layout[9][0].update(disabled=True)
        command="ros2 launch realsense2_camera rs_launch.py"
        os.system("gnome-terminal --title=Reaslense -e 'bash -c \""+command+";bash\"'")

        command="ros2 launch ros_deep_learning detectnet.ros2.launch"
        os.system("gnome-terminal --title=Detectnet -e 'bash -c \""+command+";bash\"'")

    elif event == 'cam_server':
        print("cam_server")
        layout[10][0].update(disabled=True)
        command="ros2 run sf_v2x_server cam_server"
        os.system("gnome-terminal --title=Cam-Server -e 'bash -c \""+command+";bash\"'")

window.Close()