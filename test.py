import os
import sys


def run_command(command):
    with open('temp', 'a+'):
        pass
    command = '{} > {}'.format(command, 'temp')
    p = os.system(command)
    with open('temp') as temp:
        out_data = temp.read()
    os.remove('temp')
    return out_data


def run_tests(date, program=None):
    if not os.path.exists(date):
        print("date does not exist")
        return 0
    if program is None:
        ran = False
        for f in os.listdir(date):
            if '.py' in f and 'pr' in f:
                print(f)
                run_tests(date, f.replace('.py', ''))
                ran = True
        if not ran:
            print('No files exist')
            return 0
        return 1
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
        out = run_command('python {} < {}'.format(program_path, file))
        with open(file.replace('in', 'out')) as expected_out:
            e_out_split = expected_out.read().split('\n')
            if out == 'unimplemented\n':
                print('unimplemented')
                return 0
            out_split = out.split('\n')
            out_split = [split for split in out_split if split]
            for i in range(len(out_split)):
                if i >= len(e_out_split):
                    print(file, 'extra output', out_split[i])
                    return 0
                if e_out_split[i] != out_split[i]:
                    print(file, 'expected', e_out_split[i], 'got', out_split[i])
                    return 0
            if len(e_out_split) > len(out_split):
                print(file, 'not enough output')
                return 0
            print('passed {}'.format(file))
    return 1


if __name__ == "__main__":
    output = None
    if len(sys.argv) == 3:
        output = run_tests(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        output = run_tests(sys.argv[1])
    else:
        print("This must be called with exactly 3 arguments")
        exit(-1)
    if output:
        print("pass")
    else:
        print("failed")
