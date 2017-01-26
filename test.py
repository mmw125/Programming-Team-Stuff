import os
import sys


def run_tests(date, program):
    if not os.path.exists(date):
        print("date does not exist")
        return 0
    program_path = os.path.join(date, program) + '.py'
    if not os.path.exists(program_path):
        print("program does not exist")
        return 0
    files = []
    for f in os.listdir(date):
        if program not in f or '.py' in f or 'in' not in f:
            continue
        file_path = os.path.join(date, f)
        if os.path.isfile(file_path):
           files.append(file_path)
    for file in files:
        with open(file) as open_file:
            pass
    return 1


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) != 3:
        print("This must be called with exactly 3 arguments")
        exit(-1)
    if run_tests(sys.argv[1], sys.argv[2]):
        print("pass")
    else:
        print("failed")