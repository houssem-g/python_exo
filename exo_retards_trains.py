import datetime
def manage_delays(t,dest,delay):
    if dest in t.destinations:
        prevu = datetime.datetime.strptime(t.expected_time, '%H:%M')
        real = (prevu + datetime.timedelta(minutes=delay)).strftime("%H:%M")
        t.expected_time= real


class Train:
    def __init__(self, destinations, expected_time):
        self.destinations = destinations
        self.expected_time = expected_time


trains = [
Train(['Townsville', 'Suburbia', 'Urbantska'], '13:04'),
Train(['Farmsdale', 'Suburbia', 'Lakeside Valley'], '13:20'),
Train(['Suburbia', 'Townsville', 'Lakeside Valley'], '13:22')
]


for t in trains:
    a = manage_delays(t, 'Lakeside Valley', 60)
    print(a)


