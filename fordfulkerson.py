
def path(parent, t):
    l = [t]
    n = t
    while parent[n] is not None:
        n = parent[n]
        l.insert(0, n)
    return l


def neighbours(G, s):
    l = []
    for v in G:
        if v in G[s]:
            l.append(s)
    return l


def search_aug_path(Gr, s, t):
    lnext = [s]
    parent = {s: None}
    while len(lnext) > 0:
        n = lnext.pop()
        if n == t:
            return path(parent, t)
        for v in neighbours(Gr, n):
            if not v in parent:
                lnext.append(v)
                parent[v] = n
    return None
