import subprocess
import shutil
import uuid
import os

solution_lang = {
    'GNU GCC': 'c',
    'GNU G++': 'cpp',
    'Kotlin': 'kt',
    'Python 3': 'py',
    'Ruby 2.7': 'rb',
}


def check_participant_solution(package, task, tests):
    jury_solution_lang = task.solution.name.split('.')[-1]
    print(jury_solution_lang)

    env_dir_name = get_unique_name()
    work_path = os.getcwd()
    env_dir_abspath = f'{work_path}/management/task-check-env/{env_dir_name}'

    solution_abspath = f'{work_path}/media/{task.solution.name}'
    participant_solution_abspath = f'{work_path}/media/{package.task_file.name}'

    env_solution_path = f'{env_dir_abspath}/solution.{jury_solution_lang}'
    env_participant_solution_path = f'{env_dir_abspath}/participant_solution.{solution_lang[package.language]}'

    os.mkdir(env_dir_abspath)

    shutil.copyfile(solution_abspath, env_solution_path)
    shutil.copyfile(participant_solution_abspath, env_participant_solution_path)

    input_file_name = f'{env_dir_abspath}/input.txt'
    output_file_name = f'{env_dir_abspath}/output.txt'
    participant_output_file_name = f'{env_dir_abspath}/solution_output.txt'


def get_unique_name():
    return str(uuid.uuid4())
