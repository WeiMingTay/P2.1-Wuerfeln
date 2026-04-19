# P2.1.1 Endloses Würfeln

## Aufgabe
Schätzung: 3 SP
### 👤 User Story 

Als Spieler*in

möchte ich so oft würfeln können wie ich will, wobei jede Zahl die gleiche Wahrscheinlichkeit besitzt,

damit ich das Spiel lange spielen kann.
### 🏁 Akzeptanzkriterien 

- gegeben das Würfelspiel ist gestartet,
    wenn ich einen Wurf auslöse,
    dann muss das Ergebnis eine positive Ganzzahl zwischen 1 und 6 (inklusiv) sein

- gegeben ich führe eine sehr hohe Anzahl an Würfen durch,
    wenn ich die Ergebnisse analysiere,
    dann sollte jede Zahl (1-6) annähernd gleich oft vorkommen (Gleichverteilung).

- gegeben ich habe gerade gewürfelt,
    wenn das Ergebnis angezeigt wird,
    dann werde ich sofort gefragt, ob ich erneut würfeln möchte.

## Lösung

### Schritte
1. Datei erstellt und github repository erstellt
2. Aufgaben thematisch aufschlüsseln und "auf Papier" logisch lösen
3. Lösungsansätze von Papier in wuerfeln.py bringen und ausprobieren

### Lösungsansatz
#### Was brauchen wir? Was sind mögliche Hürden?
- Wie startet man ein Spiel?
- Wie löse ich einen Wurf aus?
- Würfeln ist zufällig, wie stelle ich das im Code dar?
- Wie schränke ich das auf Integers und Zahlen von 1-6 ein?

- Ergebnisse sollen analysierbar sein. Heißt Ergebnisse müssen zwischengespeichert sein.
- Jeweilige Ergebnisse müssen zählbar sein für die Auswertung (Gleichverteilung)
- Wieviel Spiele sollen gespielt werden?

- Nach einem Wurf soll das Ergebnis angezeigt werden (als Zahl? Als Würfel?)
- Abfrage, ob ich nochmal würfeln mag. input --> Enter? oder Yes?

#### Offen und aktuelle Herausforderungen - 20260417
- While Schleife ist aktuell noch unendlich - ggf eine SPielanzahlsbegrenzung einbauen
- Anzeige ist aktuell eine Zahl von 1-6. Kann man Würfel darstellen?
- Wann stoppe ich die while Schleife? --> Nach jedem Spiel wird nach dem Ende gefragt

- Wenn wir eine vorgebene Anzahl von Spielen haben wollen, wollen wir dann einfach mehrere Funktionen erstellen?
    - def auswertung
    - def x-mal_spielen
    - def interaktiv_spielen
    - def main_function
- Wurzeln mit retro Consolen anischt oder symbol einbauen
