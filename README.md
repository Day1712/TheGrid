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
### Eén oplossing genereren
TODO uitleg

### Experiment starten
Om het experiment te starten hoeft er op dit moment alleen main.py aangeroepen te worden. (De rest is nu in comments gezet, dit zal nog verbeterd worden).

## Vereisten
TODO requirement.txt maken

## Structuur
TODO Beschrijving van de mappen

# Auteurs
- Max Schuit
- Rhodé Schuitemaker
