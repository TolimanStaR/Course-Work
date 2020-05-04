import subprocess
import shutil
import time
import uuid
import os

solution_lang = {
    'GNU GCC C99': 'c',
    'GNU G++ 17': 'cpp',
    # 'Kotlin': 'kt',
    'Python 3': 'py',
    'PyPy': 'pypy',
    # 'Ruby 2.7': 'rb',
}

verdict = {
    True: 'Правильное решение',
}

write_mode = 'w'
read_mode = 'r'


def check_participant_solution(package, task, tests):
    judge_solution_lang = task.solution.name.split('.')[-1]

    env_dir_name = get_unique_name()
    work_path = 'G:\\Projects\Coursework'  # Хардкод из-за возникающей ошибки

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

    os.chdir(env_dir_abspath)

    participant_launch_command = get_launch_command(env_participant_solution_path,
                                                    input_file_name,
                                                    participant_output_file_name)

    if participant_launch_command is None:
        return set_verdict('Ошибка компиляции', work_dir=work_path, env_dir=env_dir_abspath)

    for test_number, test in enumerate(tests):
        package.verdict = f'Выполняется на тесте {test_number + 1}'
        package.save()

        input_file = open(input_file_name, write_mode)

        for line in test.content.split('\n'):
            input_file.write(line)

        input_file.close()

        if len(test.answer) == 0:
            test.answer = get_judge_answer(test, env_solution_path, input_file_name, output_file_name)
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
            time.sleep(1)

            return set_verdict(f'Превышено ограничение по времени на тесте {test_number + 1}', work_dir=work_path,
                               env_dir=env_dir_abspath)

        participant_solution_process.kill()
        stdout, stderr = participant_solution_process.communicate()

        if stderr:
            return set_verdict(f'Ошибка исполнения на тесте {test_number + 1}', work_dir=work_path,
                               env_dir=env_dir_abspath)

        else:
            participant_out = open(participant_output_file_name, read_mode)

            participant_answer = []

            for line in participant_out.readlines():
                participant_answer.append(line.replace('\n', ''))

            participant_out.close()

            judge_answer = test.answer.split('\n')
            if type(judge_answer) == list:
                if '' in judge_answer:
                    judge_answer.remove('')

            participant_solution_length = len(participant_answer)
            judge_solution_length = len(judge_answer)

            correct_lines_counter = 0

            if participant_solution_length == judge_solution_length:
                for participant_line, judge_line in zip(participant_answer, judge_answer):

                    if participant_line.split() == judge_line.split():
                        correct_lines_counter += 1
                    else:
                        return set_verdict(f'Неправильный ответ на тесте {test_number + 1}', work_dir=work_path,
                                           env_dir=env_dir_abspath)

            else:
                return set_verdict(f'Неправильный ответ на тесте {test_number + 1}', work_dir=work_path,
                                   env_dir=env_dir_abspath)

            participant_out.close()

    return set_verdict(verdict[True], work_dir=work_path, env_dir=env_dir_abspath)


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
            f'g++ -std=c++17 -o participant_solution {env_part_sol_path}',
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
        output = open(output_, read_mode)

        for line in output.readlines():
            test.answer += line

        output.close()

    test.save()
    return test.answer


def get_solution_lang(solution_abs_path):
    return solution_abs_path.split('.')[-1]


def get_unique_name():
    return str(uuid.uuid4())


def set_verdict(message, work_dir=None, env_dir=None):
    os.chdir(work_dir)
    shutil.rmtree(env_dir)
    return message
