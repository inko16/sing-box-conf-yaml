#!/usr/bin/env python
# this file converts yaml/json, but not functional to this branch. only for testing purpose.
# if you want to contribute, you may open a PR, thank you very much

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

def yaml_to_json_min(yaml_str):
    try:
        data = yaml.safe_load(yaml_str)
        json_str = json.dumps(data, separators=(',', ':'), ensure_ascii=False) 
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
                if len(sys.argv) >= 3 : # publish
                    if sys.argv[2]=="min":
                        print(
                            yaml_to_json_min(file.read())
                        )
                else:
                    print(
                        convert_stdin_to_stdout(file.read())
                    )
        else:
            print(
                convert_stdin_to_stdout(sys.stdin.read())
            )
    except Exception as e:
        sys.stderr.write(f"convertion error: {str(e)}\n")
