import classes

days = ['Lundi', 'Mardi', 'Mercredi',
        'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
time = ['Matin', 'Aprem', 'Soir']

# Une fonction qui renvoie toutes les dates des activités d'une liste d'activités -> renvoie une liste de dico


def horaires(activities):
    l = []
    for e in activities:
        if e.date not in l:
            l.append(e.date)
    return l


def is_there(people, activity):  # savoir si la personne est présente à l'activité indiquée
    for abs in people.absence:
        if abs['day'] == activity.date['day']:
            if (activity.date['end'] >= abs['start'] >= activity.date['start']) or (activity.date['start'] <= abs['end'] <= activity.date['end']):
                return False
    return True


# Fonction qui classifie les activités en divisant une journée en 3 (Matin, Aprem, Soir)
# (à remodifier s'il y a chevauchement des horaires)


def classification(activities):
    d = {}
    for day in days:
        d[day] = {'Matin': [], 'Aprem': [], 'Soir': []}
    for act in activities:
        if act.date['end'] <= 12:
            d[act.date['day']]['Matin'].append(act)
        if act.date['start'] >= 12 and act.date['end'] <= 18:
            d[act.date['day']]['Aprem'].append(act)
        if act.date['start'] >= 18:
            d[act.date['day']]['Soir'].append(act)
    return d


# Fonction qui renvoie si une personne est présente sur une demi journée; un segment est un couple ('Lundi', 'Matin')

def is_there_segment(people, segment):
    for abs in people.absence:
        if abs['day'] == segment[0]:
            if abs['end'] <= 12 and segment[1] == 'Matin':
                return False
            if abs['start'] >= 12 and abs['end'] <= 18 and segment[1] == 'Aprem':
                return False
            if abs['start'] >= 18 and segment[1] == 'Soir':
                return False
    return True


# Transforme une liste de staffeurs et une liste d'activités en un graphe de flot (pas besoin des sommets s et t).
def graph_flow(peoples, activities, s, t):
    G = {s: {}, }
    for p in peoples:
        # arête de capacité le nombre maximal de staff réalisable par une personne sur la semaine:
        G[s][p] = 5
        G[p] = {}
        for day in days:
            for t in time:
                for act in classification(activities)[day][t]:
                    # On vérifie si la personne est bien là sur la demi journée:
                    if is_there_segment(p, (day, t)):
                        # arête de capacité 1 entre la personne et une demi journée:
                        G[p][(day, t)] = 1
    for day in days:
        for t in time:
            G[(day, t)] = {}
            for act in classification(activities)[day][t]:
                # arête de capacité 1 entre l'activité et le terminal:
                G[act] = {t: 1}
                # arête de capacité le nombre de staffeurs nécéssaires:
                G[(day, t)][act] = act.staffnumber
    return G
