#!/usr/bin/env python
import sys
import json

def minify_json(input_file):
    try:
        with open(input_file, 'r') as f:
            data = json.load(f)

        output_file = input_file.replace('.json', '_min.json')
        with open(output_file, 'w') as f:
            json.dump(data, f, separators=(',', ':'), ensure_ascii=False)

        print(f"saved JSON as {output_file}")
    except FileNotFoundError:
        print(f"error: file not found {input_file}。")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python mini.py <input_file.json>")
    else:
        input_file = sys.argv[1]
        minify_json(input_file)
