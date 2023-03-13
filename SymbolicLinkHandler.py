import os
import constants
from constants import *


class SymbolicLinkHandler:
    def __init__(self):
        pass

    @staticmethod
    def type_checker(sym_link: str):
        fd_type = sym_link.split(" ")[2].split(":")[0]

        match fd_type:
            case constants.ANON_INODE_MATCH:
                fd_type = ANON_INODE
            case constants.SOCKET_MATCH:
                fd_type = NETWORK_SOCKET
            case constants.MEM_FD_MATCH:
                fd_type = MEM_FD
            case constants.PIPE_MATCH:
                fd_type = PIPE
            case _:
                fd_type = FILE

        return fd_type

    @staticmethod
    def get_socket_id(sym_link: str):
        filtered_sym_link = sym_link.split(" ")[2].split(":")

        if filtered_sym_link[0] == SOCKET_MATCH:  # ['socket', '[XXXXX]']
            return filtered_sym_link[1].replace("[", "").replace("]", "")
        else:
            return None

    @staticmethod
    def port_checker(lsof_list: list[str], sock_id: str, path: str):
        pid = path.split("/")[2]
        socket_type = ""
        port = NOT_AVAILABLE

        for line in lsof_list:
            print(line.strip().split(" "))
            # if line.strip().split(" ").count(pid) and line.strip().split(" ").count(sock_id):
            #     return NETWORK_SOCKET, port
            # else:
            #     socket_type = IPC_SOCKET

        return socket_type, port

    @staticmethod
    def get_lsof_list():
        stream = os.popen(LSOF_GET_ACTIVE_SOCKETS)
        output = stream.readlines()[1:]

        return output
