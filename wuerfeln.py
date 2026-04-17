# Zufälligkeit erzwingen mit dem import von random und Nutzung mit zB. random.randint
import random

# Spiel starten. Erstellen einer Funktion

def wuerfel_spiel():
    print("🎲 Moin Moin und viel Spaß beim legalen Glücksspiel 🎲")
    
    # Zwischenspeichr der Ergebnisse und Zählen der Würfe
    # Wahl fiel aus set, weil die Reihenfolge egal ist
    statistik = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }
    # 0 = Int
    wuerfe_gesamt = 0


# Wurf auslösen
    # Schleife zum Spielen. Hier wird optional noch eine begrenzung eingebaut (x Spiele oder Endlos)
    while True:
        print("\n--- Neuer Wurf ---")
    
        # nur Integers von 1-6 
        ergebnis = random.randint(1,6)
        print(f"Du hast eine {ergebnis} gewürfelt!")
        
        # Ergebnisse speichern
        statistik[ergebnis] += 1
        wuerfe_gesamt += 1
        
        """
        # Anzeige untereinander
        for i in range(len(statistik)):
            print(statistik[i+1])
        """
        weiterspielen = input("Möchtest Du noch einmal würfeln? (j/n) oder Enter für ja: ")
        
        if weiterspielen == 'n':
            break


if __name__ == "__main__":
    wuerfel_spiel()