# TheGrid
TODO beschrijving van de case

## Experiment
Wij hebben een experiment opgericht. In dit experiment worden er meerde keren valide oplossingen gevonden door 3 verschillende algoritmes.

- Random. Dit algoritme zoekt naar willekeurige huis-batterij combinaties waarbij de batterij capaciteit niet wordt overschreden.
- Hill Climber. Deze begint met een random oplossing en past deze aan zodat de kosten omlaag gaan.
- Simulated Annealing. Ook dit algoritme begint met een random oplossing en past deze aan waardoor de kosten omlaag gaan.

De resultaten per gevonden oplossing worden opgeslagen als csv bestand (elk algoritme apart). In de resultaten staan de 'shared cost' (overlappende kabels delen de prijs), 'own cost' (elke individuele kabel telt mee) en de tijd die het algoritme nodig had om de oplossing te vinden. Verder passen we ook verschillende parameters aan gedurende het experiment, bijvoorbeeld de temperatuur bij simulated_annealing. Door deze aanpassingen kunnen we gegronde conclusies trekken over welk algoritme het best gebruikt kan worden bij dit probleem.

Extra toelichting:
In ons experiment wordt zowel Hill Climber als Simulated Annealing twee keer achter elkaar gebruikt: de eerste keer zoekt het naar de best mogelijke huis-batterij combinaties en de tweede keer gebruikt het de gevonden oplossing om de routes van de huizen te optimaliseren. Samen resulteert dit tot 1 geoptimaliseerde oplossing.

## Gebruik
De gebruiker kan het programme verschillende dingen laten doen door "python main.py" aan te roepen gevolgd door de volgende argumenten:

1. ("-d", "--district_number", help = "Choose district number")
2. ("-a", "--algorithm", help = "Choose algorithm: hill, sim_ann, random or none")
3. ("-p", "--plot", default = "static", help = "Choose plot type: static, live or battery (for plot per battery)")
4. ("-e", "--experiment", default = "no", help = "Choose yes or no for experiment")
5. ("-r", "--runs", type=int, default = 18, help = "Choose amount of runs for experiment")
6. ("-o", "--output", default = "no", help = "Choose yes or no for json output")

Mocht de gebruiker niet valide opties invoeren (voorbeeld: -e ye ipv -e yes), dan wordt invalid input: {fout} geprint (in het voorbeeld: invalid input: ye)
    
### Eén oplossing genereren
De gebruiker kiest het district d, het algoritme a, soort plot p en output o (yes or no).

### Experiment starten
Als een experiment wordt gedaan wordt de input bij plot en output sowieso genegeerd, het maakt dan dus niet uit wat de gebruiker in voert.
De gebruiker voer yes in bij experiment e en kiest district d, algoritme a en aantal runs r. Voor plot en output hoeft niets te worden ingevoerd.

## Vereisten
TODO requirement.txt maken

## Structuur
TODO Beschrijving van de mappen

# Auteurs
- Max Schuit
- Rhodé Schuitemaker
