#!/usr/bin/env python

import json
import yaml
import sys

def json_to_yaml(json_str):
    try:
        data = json.loads(json_str)
        yaml_str = yaml.dump(data)
        return yaml_str
    except Exception as e:
        raise e

def yaml_to_json(yaml_str):
    try:
        data = yaml.safe_load(yaml_str)
        json_str = json.dumps(data, indent=4)
        return json_str
    except Exception as e:
        raise e

def convert_stdin_to_stdout(input_data):
    try:
        # Determine format based on the first character
        if input_data.startswith("{"):
            output_data = json_to_yaml(input_data)
        else:
            output_data = yaml_to_json(input_data)

        # Print output data to stdout
        # print(output_data)
        return output_data
    except Exception as e:
        raise e

if __name__ == "__main__":
    try:
        if len(sys.argv) >= 2:
            with open(sys.argv[1], 'r', encoding='utf-8') as file:
                print(convert_stdin_to_stdout(file.read()))
        else:
            print(convert_stdin_to_stdout(sys.stdin.read()))
    except Exception as e:
        sys.stderr.write(f"convertion error: {str(e)}\n")
