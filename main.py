from constants import *
import constants
import os
import Print
import sys
from SymbolicLinkHandler import SymbolicLinkHandler


def _check_if_root_user():
    if not os.geteuid() == 0:
        sys.exit(USER_NOT_ROOT_ERROR)


def _parse_proc():
    # Access all process and their contents
    for process in os.listdir(PROC_DIRECTORY):
        if process.isdigit():  # /prod/pid
            proc_dir = os.path.join(PROC_DIRECTORY, process)  # Concatenate string with /proc/<process>...

            try:  # Accessing process contents
                for item in os.listdir(proc_dir):
                    _get_selected_proc_info(item, proc_dir)  # Get proc data for table

                Print.print_processes(ppid, pid, comm, cmdline, fd)

                fd.clear()  # Flush out FD table for next process in iteration
            except FileNotFoundError:
                pass


def _get_selected_proc_info(item: str, proc_directory: str):
    global cmdline, comm, fd, ppid, pid
    path = os.path.join(proc_directory, item)

    match item:
        case constants.CMD_LINE:
            file = open(path, "r")
            cmdline = file.readline().strip().replace('\0', "")
            if len(cmdline) is ZERO:
                cmdline = NOT_AVAILABLE
        case constants.COMM:
            file = open(path, "r")
            comm = file.readline().strip()
        case constants.FD:
            stream = os.popen(f'sudo -S ls {path} -l')  # EXECUTE CMD: sudo ls /proc/1/fd/ -l
            output = stream.readlines()[1:]
            lsof_list = SymbolicLinkHandler.get_lsof_list()

            for sym_link in output:
                port = NOT_AVAILABLE
                parsed_sym_link = " ".join(sym_link.strip().split(" ")[8:])
                socket_id = SymbolicLinkHandler.get_socket_id(parsed_sym_link)
                fd_type = SymbolicLinkHandler.type_checker(parsed_sym_link)

                if socket_id is not None:  # Gets only sym_links that points to sockets
                    fd_type, port = SymbolicLinkHandler.port_checker(lsof_list, socket_id, path)

                fd.append([parsed_sym_link, fd_type, port])  # Sym_link, fd_type (file/socket/mem_fd), port
        case constants.STATUS:
            file = open(path, "r")
            for line in file:
                if line.replace("	", "").strip()[:4] == PID:
                    pid = line.replace("	", "").strip().split(":")[1]
                if line.replace("	", "").strip()[:4] == PPID:
                    ppid = line.replace("	", "").strip().split(":")[1]


# Run Command: sudo python main.py | less
if __name__ == '__main__':
    cmdline, comm, fd, ppid, pid = "", "", [], "", ""
    _parse_proc()


