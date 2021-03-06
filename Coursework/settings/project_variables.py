PROJECT_NAME = 'Olympus Programming'
DEBUG_PROJECT_NAME = 'Coursework'

IP = '185.255.132.221'
PORT = '80'

WORKING_DIRECTORY = '/root/project'  # Only for server
LOCAL_WORKING_DIRECTORY = 'G://Projects/Coursework'  # On my pc

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

    # Codes of status of task checking:
    # WANNA ENUM...
    # But I am too lazy to use it

    'process': 'Выполняется проверка',

}

valid_image_formats = [
    'png',
    'jpg',
    'jpeg',
]

annotation = {
    'task_manager': {
        'package': 'It must be a class inherited from the class SolutionCaseBase',
        'task': 'It must be a class inherited from the class TaskBase',
        'tests': 'It must be a class inherited from the class TestBase',
    }
}
