robot_name = "Astron GEN 1"
robot_battery = 100
robot_speed = 0
robot_distance_origin = 0
robot_temperature = 0
robot_status = "OFF"
print("----- ROBOT INFO -----")
print(f"Name: {robot_name}\nBattery: {robot_battery}%\nSpeed: {robot_speed}km/h\nDistance: {robot_distance_origin}m\nStatus: {robot_status}")
print(f"Temperature: {robot_temperature}C")
ask_user = input("Do you wanna start the ROBOT? (yes/no): ")
if ask_user == "yes":
   robot_status = "ON"
   while True:
    print("------ MAIN CONTROL ------\n\t1. Move Forward\n\t2.Move Backward\n\t3. Stop\n\t4. Shutdown\n\t5. Current State")
    user_command = int(input("Choose your operation \n(use SI.NO only): "))
    ### command 1 means movew forward
    if user_command == 1:
      print("Robot is moving forward..")
      robot_battery -= 5
      robot_speed = 23
      robot_distance_origin += 5
      robot_temperature += 4
      ### command 2 means moves backward
    if user_command == 2:
      print("Robot is moving backward...")
      robot_battery -= 5
      robot_speed = 23
      robot_distance_origin += 5
      robot_temperature += 4
      ### commmand 3 , stops right there
    if user_command == 3:
      print("Robot is stopped...")
      ### command 4 , shuts down the  robot 
    if user_command == 4:
      print("Shutting down......\n\tRobot is turned off..")
      break
    ### gives the updated information of the robot
    if user_command == 5:
      print("----- ROBOT INFO -----")
      print(f"Name: {robot_name}\nBattery: {robot_battery}%\nSpeed: {robot_speed}km/h\nDistance: {robot_distance_origin}m\nStatus: {robot_status}")
      print(f"Temperature: {robot_temperature}C")
    if robot_battery <=20:
      print("battery is low ... charge as soon as possible")
    if robot_battery <= 5:
      print("battery is low..\n\t Robot can no longer operate")
      break
    if robot_temperature >= 30:
      print("Robot is overheating... \n\t\t wait until robot gets cool down") 
else:
   print("Robot is not turned on, Thanks for visiting!!")
