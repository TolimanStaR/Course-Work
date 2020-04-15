from contest.models import Contest, ContestTask, ContestTest, ContestSolutionCase, ContestParticipant, \
    ContestPastParticipant
from archive.models import ArchiveTask, ArchiveTest, ArchiveSolutionCase


def complete_contest(contest_id):
    contest = Contest.objects.get(pk=contest_id)
    tasks_list = ContestTask.objects.filter(contest=contest)

    for task_number, task in enumerate(tasks_list):
        task_tests = ContestTest.objects.filter(task=task)
        task_packages = ContestSolutionCase.objects.filter(task=task)

        archive_task = ArchiveTask.objects.create(
            title=f'{contest.pk}{task.difficulty.upper()}. {task.title}',
            body=task.body,
            input=task.input,
            output=task.output,
            time_limit=task.time_limit,
            memory_limit=task.memory_limit,
            solution=task.solution,
            difficulty=task.difficulty
        )
        archive_task.save()

        for test_number, test in enumerate(task_tests):
            new_test = ArchiveTest.objects.create(
                content=test.content,
                answer=test.answer,
                task=archive_task,
            )
            new_test.save()

        for package_number, package in enumerate(task_packages):
            new_package = ArchiveSolutionCase.objects.create(
                language=package.language,
                task_file=package.task_file,
                task_code=package.task_code,
                verdict=package.verdict,
                solved=package.solved,
                user=package.participant.user,
                task=archive_task,
            )
            new_package.save()

        for test in task_tests:
            test.delete()

        for package in task_packages:
            package.delete()

    participants_list = ContestParticipant.objects.filter(contest=contest).order_by('-task_solved', 'penalty')
    