# Zufälligkeit erzwingen mit dem import von random und Nutzung mit zB. random.randint
import random

# Spiel starten. Erstellen einer Funktion

def wuerfel_spiel():
    print("\n\033[1;32m🎲 Moin Moin und viel Spaß beim legalen Glücksspiel 🎲\033[0m")
    
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

    wuerfel_symbole = {
    1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"
}

# Wurf auslösen
    # Schleife zum Spielen. Hier wird optional noch eine begrenzung eingebaut (x Spiele oder Endlos)
    while True:
        print("\n--- \033[4mNeuer Wurf\033[0m ---")
    
        # nur Integers von 1-6 
        ergebnis = random.randint(1,6)
        print(f"Du hast eine \033[35m{ergebnis}\033[0m gewürfelt!")
        
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
        
      
    print("\n\033[32m📊 --- \033[4mSpiel beendet\033[0m --- 📊\033[0m")
    print("\033[31mHier zur Auswertung:\033[0m")
    print(f"Du hast ingesamt \033[31m{wuerfe_gesamt}\033[0m mal gewürfelt.")
    
    # ANzeige des Inhalts des Dictionaries mit for Schleife
    for zahl, anzahl in statistik.items():
        symbol = wuerfel_symbole[zahl]
        # ternary operator - kurzschreibweise für eine if else
        prozent = (anzahl / wuerfe_gesamt * 100) if wuerfe_gesamt > 0 else 0
        # :2d rückt die Anzahl anzeige ein wenig ein - rein kosmetisch =) :02d würde zB eine führende 0 einfügen
        # :.2f Möglich durch d-String: .2 macht immer zwei Nachkommastellen, f ist ein float
        print(f"Zahl \033[1;30;47m {symbol} \033[0m: {anzahl:2d} mal gewürfelt ({prozent:.2f}%)")
       
    nochmal = input("\nWillst du nochmal spielen? \nDann drück '\033[44mj\033[0m'.\nSonst drücke eine beliebige Taste!\n")
    if nochmal == "j":
        wuerfel_spiel()

if __name__ == "__main__":
    wuerfel_spiel()