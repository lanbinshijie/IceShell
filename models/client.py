# 远程控制系统：客户端
# 作者：Lanbin

import socket
import subprocess


def create_client_socket(address, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((address, port))
    return client_socket


def run_client():
    # 创建客户端套接字
    client_socket = create_client_socket('127.0.0.1', 8888)

    # 接收唯一识别码
    unique_id = int(client_socket.recv(1024).decode())
    print(f"已连接到服务端，唯一识别码为：{unique_id}")

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            command = data.decode()
            print(f"接收到来自服务端的命令：{command}")

            if command.startswith('msg'):
                # 显示消息文本
                print(command[4:])
            elif command.startswith('ping'):
                # 执行Ping命令并返回结果
                result = subprocess.Popen(command[4:], shell=True, stdout=subprocess.PIPE)
                output = result.stdout.read().decode()
                client_socket.send(output.encode())
                print(f"已向服务端发送结果：{output}")
            else:
                # 未知命令
                print("Unknown command")

    except KeyboardInterrupt:
        client_socket.close()
        print("客户端已关闭")
        return


if __name__ == '__main__':
    run_client()

