# 远程控制系统：服务端
# 作者：Lanbin

import socket


def create_server_socket(address, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((address, port))
    server_socket.listen(5)
    return server_socket


def accept_client(server_socket):
    client_socket, client_address = server_socket.accept()
    print(f"已连接客户端：{client_address}")
    return client_socket, client_address


def generate_unique_id(clients_dict):
    return len(clients_dict)


def send_command_to_client(client_socket, command):
    client_socket.send(command.encode())


def run_server():
    # 创建服务器套接字
    server_socket = create_server_socket('127.0.0.1', 8888)

    # 创建保存已连接客户端套接字的字典
    clients_dict = {}
    try:
        while True:
            try:
                # 接受客户端连接请求
                client_socket, client_address = accept_client(server_socket)

                # 生成唯一识别码
                unique_id = generate_unique_id(clients_dict)

                # 将客户端套接字保存到字典中，其唯一识别码是它的索引
                clients_dict[unique_id] = client_socket

                # 向客户端发送生成的唯一识别码
                client_socket.send(str(unique_id).encode())

                # 建立连接
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    print(f"来自客户端[{unique_id}]：{data.decode()}")

                    # 向客户端发送指令
                    command = input("请输入指令：")
                    send_command_to_client(client_socket, command)
            except ConnectionResetError:
                print(f"客户端[{unique_id}]已断开连接")
                del clients_dict[unique_id]
                continue
            except Exception as e:
                print(f"服务器出现错误：{str(e)}")
                continue
    
    except KeyboardInterrupt:
        answer = input("是否关闭服务器？(y/n)")
        if answer == 'y':
            server_socket.close()
            print("服务器已关闭")
            return


if __name__ == '__main__':
    run_server()
