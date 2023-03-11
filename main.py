import constants
from constants import *
import os
import sys


def _check_if_root_user():
    if not os.geteuid() == 0:
        sys.exit(USER_NOT_ROOT_ERROR)


def _parse_proc():
    # Access all process and their contents
    for process in os.listdir(PROC_DIRECTORY):
        if process.isdigit():
            proc_dir = os.path.join(PROC_DIRECTORY, process)  # Concatenate string with /proc/<process>...

            # Accessing process contents
            for item in os.listdir(proc_dir):
                _get_selected_proc_info(item, proc_dir)

            # Comment out later
            print(f"cmdline: {cmdline}")
            print(f"comm: {comm}")
            print(f"pid: {pid}")
            print(f"ppid: {ppid}")
            print(fd)

            return


def _get_selected_proc_info(item: str, proc_directory: str):
    global cmdline, comm, fd, ppid, pid
    path = os.path.join(proc_directory, item)

    match item:
        case constants.CMD_LINE:
            file = open(path, "r")
            cmdline = file.readline().strip()
        case constants.COMM:
            file = open(path, "r")
            comm = file.readline().strip()
        case constants.FD:
            stream = os.popen(f'sudo -S ls {path} -l')  # EXECUTE CMD: sudo ls /proc/1/fd/ -l
            output = stream.readlines()[1:]
            for sym_link in output:
                fd.append(" ".join(sym_link.strip().split(" ")[8:]))
        case constants.STATUS:
            file = open(path, "r")
            for line in file:
                if line.replace("	", "").strip()[:4] == PID:
                    pid = line.replace("	", "").strip().split(":")[1]
                if line.replace("	", "").strip()[:4] == PPID:
                    ppid = line.replace("	", "").strip().split(":")[1]


if __name__ == '__main__':
    cmdline, comm, fd, ppid, pid = "", "", [], "", ""
    _parse_proc()
