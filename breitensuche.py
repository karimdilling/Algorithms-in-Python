# Breitensuche findet kürzeste Distanz von einem Startknoten zu jedem anderen Knoten in einem ungerichteten Graphen

# Initialisiere BFS
Adj = { # Adjazenzliste des Graphen (Python "Dictionary" wird hier dafür verwendet)
    1: [2, 5, 6],
    2: [3, 7],
    3: [1, 8],
    4: [5],
    5: [3, 4],
    6: [5],
    7: [4],
    8: [4]
}
color = {
    1: "grau",
    2: "weiß",
    3: "weiß",
    4: "weiß",
    5: "weiß",
    6: "weiß",
    7: "weiß",
    8: "weiß"
}
Q = [1] # Wert des Startknotens in die Schlange eintragen
d = { # Entfernung zu Startknoten (hier Knoten 1), -1 entspricht unendlich
    1: 0,
    2: -1,
    3: -1,
    4: -1,
    5: -1,
    6: -1,
    7: -1,
    8: -1
}
pi = { # Vaterknoten von u (zu Beginn None)
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None
}

# Eigentlicher Algorithmus:
while len(Q) != 0: # Führe den Algorithmus solange aus, wie die Schlange Q nicht leer ist
    u = Q[0] # u = head[Q]
    for v in Adj[u]:
        if color[v] == "weiß":
            color[v] = "grau"
            d[v] = d[u]+1 # d[u]: Abstand zu s (zu Beginn unendlich bzw. -1)
            pi[v] = u # Vaterknoten von u (zu Beginn None (leer)) -- Für die Ausführung des Algorithmus nicht unbedingt von Nöten --
            Q.append(v) # Fügt neues Objekt v am Ende der Schlange ein (enqueue(Q,v))
    Q.remove(Q[0]) # Entfernt Objekt am Kopf der Schlange -> doppelt verkette Liste verwenden (wird in Python automatisch getan)
    color[u] = "schwarz"

# Funktionstest:
print(color) # Schaue, ob zum Ende alle Knoten schwarz sind
print(d) # Zeige kürzeste Wege zu allen Knoten vom Startknoten aus