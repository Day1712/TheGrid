# TODO write algorithm that creates better routes than the
# 'valid_shortest_route'. More overlap to lower the shared cost.

'''
Maybe Hillclimber?
Pseudo code from the lecture:

Kies een random start state
Herhaal tot na N-keer niet meer verbetert:
    Doe een kleine random aanpassing
    Als de state is verslechterd:
        Maak de aanpassing ongedaan



Simulated Annealing,
pseudo code of the lecture example:

Herhaal:
    Kies een random start state
    Kies start temperatuur
    Herhaal N iteraties:
        Doe een kleine random aanpassing
        Als random( ) > kans(oud, nieuw, temperatuur):
            Maak de aanpassing ongedaan
        Verlaag temperatuur

'''
