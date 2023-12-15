from random import choice

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def choose_day():
    """Return the raondom day"""
    return choice(days)