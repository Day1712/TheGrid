# TheGrid
Steeds meer huizen produceren hun eigen energie. Als de zon schijnt leveren zonnepanelen zelfs een overschot! Hoe kan een wijk er voor zorgen dat dit overschot zo goedkoop mogelijk opgeslagen kan worden in batterijen?

Binnen de case SmartGrid zijn er verschillende wijken met elk 150 huizen en 5 batterijen. Elk huis heeft zijn eigen energie output die via kabels bij een batterij opgeslagen kan worden. Maar, deze kabels kosten geld. Ook hebben de batterijen maar bepaalde hoeveelheid aan capaciteit. Dit zorgt voor twee interactieve problemen:

1. Welke huis-batterij combinaties zorgen voor de laagste kosten zonder de batterij capaciteit te overschrijden?
2. Hoe zorg je voor zo kort mogelijke kabels met zoveel mogelijk overlap? Want: gedeelde kabels kost minder geld!

Wij hebben verschillende algoritmes gemaakt om deze case op te lossen. Aan de hand van visualisatie is het proces zichtbaar gemaakt. Door middel van experimenten zijn resultaten verzameld om algoritmes met elkaar te vergelijken. Dit zal uiteindelijk tot een conclusie leiden: hoe kan je het goedkoopst een grid van huizen en batterijen optimaliseren. Voor het antwoord zien we jullie graag bij de presentatie!

## Algoritmes
Oplossingen voor het probleem worden gevonden door 1 van deze 3 algoritmes:

- Random. Dit algoritme zoekt naar willekeurige huis-batterij combinaties waarbij de batterij capaciteit niet wordt overschreden.
- Hill Climber. Deze begint met een random oplossing en past kleine aanpassingen toe zodat de kosten omlaag gaan.
- Simulated Annealing. Ook dit algoritme begint met een random oplossing en past deze aan waardoor de kosten omlaag gaan.

### Extra toelichting:
Zowel Hill Climber als Simulated Annealing worden in feite twee keer achter elkaar gebruikt: de eerste keer zoekt het naar de best mogelijke huis-batterij combinaties. De tweede keer gebruikt het de gevonden oplossing om de routes van de huizen te optimaliseren. Samen resulteert dit tot 1 geoptimaliseerde oplossing.

Er zijn twee aanpassingen die gedaan kunnen worden bij Hill Climber en Simulated Annealing. De eerste 'mutatie' helpt bij het maken van optimalere huis-batterij combinaties. De tweede aanpassing verandert de route van de kabels zodat deze meer overlap vinden (gedeelde kabels --> lagere kosten!).

Voor de ADVANCED is er de mogelijkheid om de locaties van de batterijen te verplaatsen. Tijdens het zoeken van de beste huis-batterij combinaties zal de batterij meer en meer naar het middenpunt verplaatsen (alleen mogelijk bij Hill Climber of Simulated annealing).

## Experiment
Wij hebben een experiment opgericht. In dit experiment worden er meerde keren valide oplossingen gevonden door de verschillende algoritmes.

De resultaten per gevonden oplossing worden opgeslagen als csv bestand (elk algoritme apart). In de resultaten staan:  
- 'shared cost' (overlappende kabels delen de prijs)
- 'own cost' (elke individuele kabel telt mee)
- de tijd die het algoritme nodig had om de oplossing te vinden.

Verder passen we ook verschillende parameters aan gedurende het experiment, bijvoorbeeld de temperatuur bij simulated_annealing. Door deze aanpassingen kunnen we gegronde conclusies trekken over welk algoritme het best gebruikt kan worden bij dit probleem.

## Gebruik
De gebruiker kan het programme verschillende dingen laten doen door "python main.py" aan te roepen gevolgd door de volgende argumenten:

1. ("-d", "--district_number", help = "Choose district number")
2. ("-a", "--algorithm", help = "Choose algorithm: hill, sim_ann, random or none")
3. ("-m", "--move_batteries", help = "Choose if batteries may move: yes or no")
4. ("-p", "--plot", default = "static", help = "Choose plot type: static, live or battery (for plot per battery)")
5. ("-e", "--experiment", default = "no", help = "Choose yes or no for experiment")
6. ("-r", "--runs", type=int, default = 18, help = "Choose amount of runs for experiment")
7. ("-o", "--output", default = "no", help = "Choose yes or no for json output")

Mocht de gebruiker niet valide opties invoeren (voorbeeld: -e ye ipv -e yes), dan wordt invalid input: {fout} geprint (in het voorbeeld: invalid input: ye)

### Eén oplossing genereren
Voorbeeld:
De gebruiker kiest het district d, het algoritme a, soort plot p en output o (yes or no).
```
python main.py -d 3 -a hill -p live -o no
```

### Experiment starten
Als een experiment wordt gedaan hoeft er voor plot en output niets te worden ingevoerd.

Voorbeeld:
```
python main.py -d 1 -a sim_ann -e yes -r 54
```

## Vereisten
Zie requirement.txt

## Structuur
```
TheGrid
│   README.md
│   main.py
│   requirements.txt   
│
└───code: bevat alle code van het project
│   └─── code/algorithms: bevat alle code dat nodig is voor het runnen van het project
│   └─── code/classes: bevat de classes van het project
│   └─── code/experiments: bevat de code voor het uitvoeren van het experiment en de resultaten
│   └─── code/output: bevat de code dat nodig is voor de json output
│   └─── code/visualisation: bevat de code dat nodig is voor het plotten
│   
└───data : de data van de 3 districts
```

# Auteurs
- Max Schuit
- Rhodé Schuitemaker
