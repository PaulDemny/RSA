# -*- coding: cp1252 -*-

import keygen;
import scrambler;
import descrambler;

wahl = True;

def main():

    print("Dieses Programm ist zur Schlüsselerzeugung, Verschlüsselung und Entschlüsselung \n des RSA Codes");
    
    while wahl:
        auswahl = 0;

        while not auswahl:

            print("Welche Aktion wollen Sie durchführen?");
            print("1. RSA Schlüssel erzeugen;\n2. Text chiffrieren;\n3. Text dechiffrieren;\n4.Das Programm beenden; ");
            print("     Wählen Sie mit den NUM - Tasten und bestätigen mit ENTER");
            auswahl = int(input());
            if auswahl < 1 or auswahl > 4:
                auswahl = 0;

        print("War Ihre Auswahl %s?. Bestätigen Sie mit ENTER." %auswahl);

        if auswahl == 1:
            keygen.keygen();

        if auswahl == 2:
            scrambler.scrambler();

        if auswahl == 3:
            descrambler.descrambler();

        if auswahl == 4:
            break;

        tempwahl = ord(raw_input());

        if tempwahl == 121 or tempwahl == 89:
            wahl = True;
        else:
            wahl = False;
        
    print("Das Programm wird nun beendet\n          Bye, Bye");


if __name__ == "__main()__":
    main()

    


