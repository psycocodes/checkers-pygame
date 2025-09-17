import json
import os

def load_preset(file_path, preset_name='BASE'):
    with open(file_path, 'r') as file:
        try:
            return json.load(file)[preset_name]
        except (TypeError, KeyError):
            return {}


def add_preset(file_path, preset_name, data):
    with open(file_path, 'r') as read_file:
        try:
            previous_content = json.load(read_file)
        except json.decoder.JSONDecodeError:
            previous_content = {}
        with open(file_path, 'w') as write_file:
            json.dump(previous_content | {preset_name: data}, write_file, indent=4)


def clear_file(file_path):
    with open(file_path, 'w') as file:
        json.dump(None, file)


def delete_preset(file_path, preset_name):
    with open(file_path, 'r') as read_file:
        try:
            previous_content = json.load(read_file)
        except json.decoder.JSONDecodeError:
            previous_content = {}
        with open(file_path, 'w') as write_file:
            if preset_name in previous_content:
                del previous_content[preset_name]
            json.dump(previous_content, write_file, indent=4)


def add_data(file_path, data):
    with open(file_path, 'r') as read_file:
        try:
            previous_content = json.load(read_file)
        except json.decoder.JSONDecodeError:
            previous_content = {}
        with open(file_path, 'w') as write_file:
            new_data = {}
            index = len(previous_content)
            for element in data:
                index += 1
                new_data[index] = element
            json.dump(previous_content | new_data, write_file, indent=4)


def delete_data(file_path, index):
    with open(file_path, 'r') as read_file:
        try:
            previous_content = json.load(read_file)
        except json.decoder.JSONDecodeError:
            previous_content = {}
        with open(file_path, 'w') as write_file:
            if index in previous_content:
                del previous_content[index]
            json.dump(previous_content, write_file, indent=4)


def update_data(file_path, data):
    with open(file_path, 'w') as write_file:
        data = {index + 1: value for index, value in enumerate(data)}
        json.dump(data, write_file, indent=4)


def load_data(file_path):
    with open(file_path, 'r') as file:
        try:
            return json.load(file)
        except json.decoder.JSONDecodeError:
            return {}