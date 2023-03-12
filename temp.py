def user_defined_int():
    global variable_i
    global variable_op
    global variable_x
    global variable_y
    global variable_error_x
    global variable_turn_angle_x
    global variable_turn_angle_y
    global variable_ID
    global list_maker_list
    global list_number_list
    global list_shoot_list
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    list_maker_list.clear()
    list_number_list.clear()
    list_shoot_list.clear()
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    vision_ctrl.marker_detection_color_set(rm_define.marker_detection_color_red)
    vision_ctrl.set_marker_detection_distance(3)

ef user_defined_shoot_ID():
    global variable_i
    global variable_op
    global variable_x
    global variable_y
    global variable_error_x
    global variable_turn_angle_x
    global variable_turn_angle_y
    global variable_ID
    global list_maker_list
    global list_number_list
    global list_shoot_list
    variable_x = list_maker_list[(list_maker_list.index(variable_ID)) + 1]
    variable_y = list_maker_list[(list_maker_list.index(variable_ID)) + 2]
    variable_error_x = variable_x - 0.5
    variable_turn_angle_x = variable_error_x * 108
    variable_turn_angle_y = (0.5 - variable_y) * 68 - abs(variable_error_x) * 10
    gimbal_ctrl.angle_ctrl(variable_turn_angle_x, variable_turn_angle_y + 19)
    time.sleep(0.08)
    gun_ctrl.fire_once()
    time.sleep(0.08)
    if variable_ID < 25:
        list_maker_list.pop((list_maker_list.index(variable_ID)))

def user_defined_get_number_list():
    global variable_i
    global variable_op
    global variable_x
    global variable_y
    global variable_error_x
    global variable_turn_angle_x
    global variable_turn_angle_y
    global variable_ID
    global list_maker_list
    global list_number_list
    global list_shoot_list
    gimbal_ctrl.pitch_ctrl(15)
    time.sleep(0.1)
    gimbal_ctrl.set_rotate_speed(200)
    list_number_list.clear()
    list_maker_list=RmList(vision_ctrl.get_marker_detection_info())
    while not len(list_maker_list) >= 26:
        list_maker_list=RmList(vision_ctrl.get_marker_detection_info())
    media_ctrl.play_sound(rm_define.media_sound_scanning)
    variable_i = 2
    for count in range(5):
        if list_maker_list[variable_i] < 20:
            list_number_list.append(list_maker_list[variable_i] - 10)
        else:
            variable_op = list_maker_list[variable_i]
        variable_i = variable_i + 5

