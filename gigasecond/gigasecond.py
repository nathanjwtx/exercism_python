from datetime import timedelta


def add_gigasecond(moment):

    return moment + timedelta(seconds=1 * 10**9)
