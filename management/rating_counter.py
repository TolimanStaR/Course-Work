from account.models import UserProfile


class RatingUserProfile(object):

    def __init__(self, username, rating, place_before, place_after):
        self.username = username
        self.rating = rating
        self.place_before = place_before
        self.place_after = place_after

    def __str__(self):
        return f'{self.username}'


def calculate_rating():
    pass
