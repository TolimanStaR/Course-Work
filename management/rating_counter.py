from account.models import UserProfile
from contest.models import Contest, ContestParticipant

import operator


class RatingUserProfile(object):

    def __init__(self, username, rating, place_before, place_after):
        self.username = username
        self.rating = rating
        self.place_before = place_before
        self.place_after = place_after

    def __str__(self):
        return f'{self.username}'


def calculate_rating(contest_id):
    contest = Contest.objects.get(pk=contest_id)
    participants_list = ContestParticipant.objects.filter(contest=contest).order_by('-task_solved', 'penalty')

    users_list = [participant for participant in participants_list]

    for place, participant in enumerate(users_list):
        participant_place_in_contest = place + 1
        participant.rating = participant_place_in_contest
        participant.save()

    users_list.sort(key=operator.attrgetter('user.contest_rating'))
    users_list.reverse()

    for relative_place, participant in enumerate(users_list):
        participant.user.contest_rating += 1 + relative_place - participant.rating

        if participant.user.contest_rang >= 0:
            rang_index = min(participant.user.contest_rang // 50, 4) + 6
        else:
            rang_index = max(participant.user.contest_rang // 50, -4) + 5

        participant.user.contest_rang = UserProfile.RANG_CHOICES[rang_index][1]

        participant.user.save()
