#!/usr/bin/env python
import sys
import json

def minify_json(input_file):
    try:
        # 读取输入的 JSON 文件
        with open(input_file, 'r') as f:
            data = json.load(f)

        # 将压缩后的 JSON 写入新文件
        output_file = input_file.replace('.json', '_min.json')
        with open(output_file, 'w') as f:
            json.dump(data, f, separators=(',', ':'), ensure_ascii=False)

        print(f"压缩后的 JSON 已保存为 {output_file}")
    except FileNotFoundError:
        print(f"错误：找不到文件 {input_file}。")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法：python minify_json.py <input_file.json>")
    else:
        input_file = sys.argv[1]
        minify_json(input_file)
