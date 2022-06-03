"""this script is used to count number of consecutive day in a list"""
from datetime import datetime, timedelta
def current_streak(today, lst):
    """this is the main function used to return number of consecutuve day in list"""
    nb_day = 0
    new_list = [val['date'] for val in lst]
    if today not in new_list:
        return nb_day
    delta = timedelta(days=1)
    today = datetime.strptime(today, '%Y-%m-%d')
    for element in reversed(new_list):
        consecutive_date = datetime.strptime(element, '%Y-%m-%d')
        if today != consecutive_date:
            return nb_day
        nb_day += 1
        today -= delta
    return nb_day
    