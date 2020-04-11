import subprocess
import shutil
import uuid
import os

solution_lang = {
    'GNU GCC': 'c',
    'GNU G++': 'cpp',
    # 'Kotlin': 'kt',
    'Python 3': 'py',
    'PyPy': 'pypy',
    # 'Ruby 2.7': 'rb',
}


def check_participant_solution(package, task, tests):
    judge_solution_lang = task.solution.name.split('.')[-1]

    env_dir_name = get_unique_name()
    work_path = os.getcwd()
    env_dir_abspath = f'{work_path}/management/task-check-env/{env_dir_name}'

    solution_abspath = f'{work_path}/media/{task.solution.name}'
    participant_solution_abspath = f'{work_path}/media/{package.task_file.name}'

    env_solution_path = f'{env_dir_abspath}/solution.{judge_solution_lang}'
    env_participant_solution_path = f'{env_dir_abspath}/participant_solution.{solution_lang[package.language]}'

    os.mkdir(env_dir_abspath)

    shutil.copyfile(solution_abspath, env_solution_path)
    shutil.copyfile(participant_solution_abspath, env_participant_solution_path)

    input_file_name = f'{env_dir_abspath}/input.txt'
    output_file_name = f'{env_dir_abspath}/output.txt'
    participant_output_file_name = f'{env_dir_abspath}/solution_output.txt'

    write_mode = 'w'
    read_mode = 'r'

    os.chdir(env_dir_abspath)  # Смена рабочей директории на нашу

    command = get_launch_command(package, env_participant_solution_path)
    print(command)

    for test_number, test in enumerate(tests):
        input_file = open(input_file_name, write_mode)

        for line in test.content.split('\n'):
            input_file.write(line)

        input_file.close()

        if test.answer is None:
            test = get_judge_answer(test)
            test.save()

    os.chdir(work_path)


def get_launch_command(package, env_part_sol_path):
    command = None

    if solution_lang[package.language] == 'py':
        return f'python {env_part_sol_path}'

    if solution_lang[package.language] == 'pypy':
        return f'python {env_part_sol_path}'

    if solution_lang[package.language] == 'c':
        create_exe = subprocess.call(
            f'gcc -o participant_solution {env_part_sol_path}',
            shell=True,
            timeout=10,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        if create_exe == 0:
            return f'./participant_solution'
        else:
            return command

    if solution_lang[package.language] == 'cpp':
        create_exe = subprocess.call(
            f'g++ -o participant_solution {env_part_sol_path}',
            shell=True,
            timeout=10,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if create_exe == 0:
            return f'./participant_solution'
        else:
            return command


def get_judge_answer(test):
    test.save()
    return test


def get_solution_lang(solution_abs_path):
    return solution_abs_path.split('.')[-1]


def get_unique_name():
    return str(uuid.uuid4())
