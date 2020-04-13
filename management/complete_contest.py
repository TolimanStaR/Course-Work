from contest.models import Contest, ContestTask, ContestTest, ContestSolutionCase, ContestParticipant, \
    ContestPastParticipant
from archive.models import ArchiveTask, ArchiveTest, ArchiveSolutionCase


def complete_contest(contest):
    participants_list = ContestParticipant.objects.filter(contest=contest)
    tasks_list = ContestTask.objects.filter(contest=contest)

