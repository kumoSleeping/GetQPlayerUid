from flask import Flask, jsonify, request
import json
import os
from pathlib import Path


app = Flask(__name__)

current_dir = Path.cwd()

language_mapping = {"jp", "en", "tw", "cn", "kr"}

for lang in language_mapping:
    folder_path = current_dir / lang

    # 检查文件夹是否存在，如果不存在则创建
    if not folder_path.exists():
        folder_path.mkdir()


def save_data(user_id, uid, server):
    if server in language_mapping:
        folder_name = server
    else:
        return '错误的服务器'

    # 如果文件夹不存在，则创建
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_name = os.path.join(folder_name, str(user_id))

    # 如果文件已经存在，则读取文件内容，否则创建新文件
    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    # 更新数据并保存到文件
    data['uid'] = uid
    with open(file_name, 'w') as f:
        json.dump(data, f)

    return '数据保存成功'


def get_data(user_id, server):
    if server in language_mapping:
        folder_name = server
    else:
        return '错误的服务器'

    file_name = os.path.join(folder_name, str(user_id))

    # 如果文件不存在，则返回错误消息
    if not os.path.exists(file_name):
        return '找不到用户'

    # 读取文件内容并返回
    with open(file_name, 'r') as f:
        data = json.load(f)

    return str(data['uid'])


# 客户端通过 GET 请求调用此 API
@app.route('/api/data', methods=['GET'])
def handle_data():
    try:
        uid = int(request.args.get('uid'))
    except:
        pass
    # 获取请求中的参数
    mode = request.args.get('mode')
    user_id = int(request.args.get('user_id'))
    server = request.args.get('server')

    if mode == 'save':
        return save_data(user_id, uid, server)
    elif mode == 'get':
        return get_data(user_id, server)
    else:
        return '错误的请求'


if __name__ == '__main__':
    app.run(port=7722, host='0.0.0.0', debug=True, use_reloader=True)
