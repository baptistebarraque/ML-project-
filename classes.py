class activity:
    def __init__(self, name, date, people, relou):
        self.name = name
        self.date = date
        self.people = people
        self.relou = relou


class people:
    def __init__(self, name, absence, love, hate):
        self.name = name
        self.absence = absence
        self.love = love
        self.hate = hate


david = people('david', [{'day': 'Lundi', 'start': 14, 'end': 18}, {
               'day': 'Mardi', 'start': 8, 'end': 12}], ['paintball'], ['vaisselle', 'city-rally'])

paintball = activity(
    'paintball', {'day': 'Mercredi', 'start': 15, 'end': 22}, 5, 1)

print(david.absence)
