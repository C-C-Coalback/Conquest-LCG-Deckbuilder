import os
import ast


def get_current_light_dark_dict():
    temp_cwd = os.getcwd()
    light_mode_dir = temp_cwd + '/light_mode_dict.txt'
    with open(light_mode_dir, "r") as data:
        light_dark_dict = ast.literal_eval(data.read())
    return light_dark_dict


def get_light_mode(username):
    temp_cwd = os.getcwd()
    light_mode_dir = temp_cwd + '/light_mode_dict.txt'
    if not os.path.exists(light_mode_dir):
        my_dict = {'alex': 'Light', 'Test': 'Dark'}
        with open(light_mode_dir, 'w') as file:
            file.write(str(my_dict))
    with open(light_mode_dir, "r") as data:
        light_dark_dict = ast.literal_eval(data.read())
    if username in light_dark_dict:
        print(light_dark_dict[username] == "Light")
        return light_dark_dict[username] == "Light"
    return False


def update_light_mode(username, new_val):
    temp_cwd = os.getcwd()
    light_mode_dir = temp_cwd + '/light_mode_dict.txt'
    with open(light_mode_dir, "r") as data:
        light_dark_dict = ast.literal_eval(data.read())
    light_dark_dict[username] = new_val
    with open(light_mode_dir, 'w') as file:
        file.write(str(light_dark_dict))
