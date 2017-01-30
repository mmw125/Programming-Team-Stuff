from bs4 import BeautifulSoup
import json
import requests
import os
import sys


def load_problem(folder, problem_id, letter):
    req = requests.get('https://pcs.cs.cloud.vt.edu/api/problems/{}/'.format(problem_id))
    bs = BeautifulSoup(json.loads(req.text)['content'])
    i = 0
    python_file_path = os.path.join(folder, 'pr{}.py'.format(letter))

    def remove_last_nl(string):
        return string[:len(string) - 1] if string[len(string) - 1] == '\n' else string

    if not os.path.exists(python_file_path):
        with open(python_file_path, 'w+') as python_file:
            python_file.write("""\nif __name__ == '__main__':\n    print("unimplemented")""")
    for table in bs.find_all('table'):
        in_val, out = [str(i).replace('<pre>', '').replace('</pre>', '') for i in table('pre')]
        in_val = remove_last_nl(in_val)
        out = remove_last_nl(out)
        with open(os.path.join(folder, 'pr{}_in_{}'.format(letter, i)), 'w+') as in_file:
            in_file.write(in_val)
        with open(os.path.join(folder, 'pr{}_out_{}'.format(letter, i)), 'w+') as out_file:
            out_file.write(out)
        i += 1


def load_contest(folder, contest_number):
    if not os.path.exists(folder):
        os.mkdir(folder)
    req = requests.get('https://pcs.cs.cloud.vt.edu/api/contests/{}/'.format(contest_number))
    letter = ord('A')
    for problem in req.json()['problems']:
        load_problem(folder, problem['id'], chr(letter))
        letter += 1


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('This can only be called with 2 arguments. Date, and contest number')
        exit(-1)
    load_contest(sys.argv[1], sys.argv[2])