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
    participant_output_file_name = f'{env_dir_abspath}/participant_output.txt'

    write_mode = 'w'
    read_mode = 'r'

    os.chdir(env_dir_abspath)  # Смена рабочей директории на нашу

    participant_launch_command = get_launch_command(env_participant_solution_path,
                                                    input_file_name,
                                                    participant_output_file_name)

    if participant_launch_command is None:
        package.verdict = set_verdict('Ошибка компиляции')
        return package

    for test_number, test in enumerate(tests):
        input_file = open(input_file_name, write_mode)

        for line in test.content.split('\n'):
            input_file.write(line)

        input_file.close()

        if test.answer is None:
            test = get_judge_answer(test, env_solution_path, input_file_name, output_file_name)
            test.save()

        participant_solution_process = subprocess.Popen(
            participant_launch_command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        try:
            participant_solution_process.wait(task.time_limit)
        except subprocess.TimeoutExpired:
            participant_solution_process.kill()
            package.verdict = set_verdict(f'Превышено ограничение по времени на тесте {test_number + 1}')
            return package

        participant_solution_process.kill()
        stdout, stderr = participant_solution_process.communicate()

        if stderr:
            package.verdict = set_verdict(f'Ошибка исполнения на тесте {test_number + 1}')
            return package
        else:
            pass

            # Пока все идет успешно, осталось сравнить вывод

    os.chdir(work_path)


def get_launch_command(env_part_sol_path, input_, output_):
    command = None
    lang = get_solution_lang(env_part_sol_path)

    if lang == 'py':
        return f'python {env_part_sol_path} < {input_} > {output_}'

    if lang == 'pypy':
        return f'python {env_part_sol_path} < {input_} > {output_}'

    if lang == 'c':
        create_exe = subprocess.call(
            f'gcc -o participant_solution {env_part_sol_path}',
            shell=True,
            timeout=10,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        if create_exe == 0:
            return f'participant_solution.exe < {input_} > {output_}'

    if lang == 'cpp':
        create_exe = subprocess.call(
            f'g++ -o participant_solution {env_part_sol_path}',
            shell=True,
            timeout=10,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if create_exe == 0:
            return f'participant_solution.exe < {input_} > {output_}'

    return command


def get_judge_answer(test, judge_sol_abs_path, input_, output_):
    launch_command = get_launch_command(judge_sol_abs_path, input_, output_)

    process = subprocess.call(
        launch_command,
        shell=True,
        timeout=2,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if process == 0:
        output = open(output_, 'r')

        for line in output:
            if len(line) > 0:
                test.answer += line

        output.close()

    test.save()
    return test


def get_solution_lang(solution_abs_path):
    return solution_abs_path.split('.')[-1]


def get_unique_name():
    return str(uuid.uuid4())


def set_verdict(message):
    # Удалить папку

    return message
