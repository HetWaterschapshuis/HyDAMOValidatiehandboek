# Bekijken van validatie resultaten op een kaart

Activeer de werkruimte voor het bekijken van validatie resultaten op een kaart vanuit de werkruimte voor het beheren van validatietaken, door:

- op de icoon <img src="..\..\images\41161cba-d2b7-472d-9e98-c542283550a3.png"/> te klikken van de betreffende validatietaak.
- het menu-item <img src="..\..\images\0cc87fb7-6e34-4ded-8d7e-6412689f0c89.png"/> in de verticale menu-balk te activeren waarbij de betreffende validatietaak in de tabel met validatatietaken is geselecteerd.

Er verschijnt een kaartlaag met daarin alle objecten uit de verschillende objectlagen die in de validatietaak zijn gevalideerd. Dit kunnen zijn (zie ook de legenda in de kaart voor de gebruikte iconen per objectlaag):

- Bodemvallen<img src="..\..\images\ba34ca6e-9565-480e-88e8-579e7af1d497.png"/>
- Bruggen<img src="..\..\images\c7f0fa0a-a997-4fce-b4c9-ef0499222a57.png"/>
- Duikers, sifons en hevels <img src="..\..\images\c5a54eb3-1c98-498d-bd0b-88b0f8e1b741.png"/>
- Gemalen<img src="..\..\images\1cd9e21e-e759-4f51-a882-8e9cec96d5c5.png"/>
- Regelmiddelen<img src="..\..\images\4867e1b9-c5e6-4ce3-8d78-91c763215d3f.png"/>
- Stuwen <img src="..\..\images\d9fef3da-4309-4068-bd67-6de88f94e418.png"/>
- Pompen (worden niet getoond op de kaart, maar zijn onderdeel van een ander object)
- Kunstwerkopeningen (worden niet getoond op de kaart, maar zijn onderdeel van een ander object)
- Watergangen (Hydro-objecten) :Hydroobject_HyDAMO:

<img src="..\..\images\a006ada7-ef19-450a-a45c-94938c5dfd64.png"/>

Iconen krijgen een kleur afhankelijk van het validatieresultaat. Standaard wordt een kleurverloop van rood naar groen toegepast, maar voor gebruikers die kleurenblind zijn is er ook een optie op het kleurverloop aan te passen zodat deze loopt van blauw naar rood. Deze ‘Kleurenblind modus' kan geactiveerd worden in het paneel met de filteropties (bovenin onder het item 'Map opties’).

Om de hoeveelheid iconen op de kaart overzichtelijk te houden wordt iconen van hetzelfde objecttype en die dicht bij elkaar liggen op de kaart, standaard geclusterd weergegeven. Met een getal boven het icoon wordt aangeduid hoeveel objecten geclusterd zijn. De kleur van het geclusterde icoon, toont altijd het slechtste validatieresultaat van de individuele objecten die geclusterd zijn.

<img src="..\..\images\907dcd9e-d26a-4a03-ab29-b9901f21f617.png"/>

Wanneer de muis boven een cluster icoon wordt geplaatst, verschijnt een overzicht met aanvullende informatie, bestaande uit het aantal geclusterde objecten, het gemiddelde rapportcijfer van de geclusterde objecten en het laagste en hoogte rapportcijfer van de geclusterde objecten.

<img src="..\..\images\09fa8da3-3504-4f06-9578-f2feefec180e.png"/>

Door op een geclusterd icoon te klikken worden de individuele geclusterde iconen 'onthuld'.

<img src="..\..\images\b2aaaadd-8fb3-497a-9e4d-c033248d2b3b.png"/>

Door vervolgens de muis boven een individueel icoon te plaatsen, verschijnt een overzicht met aanvullende informatie van het betreffende object, bestaande uit de NEN3610id, het objecttype, het rapportcijfer van de validatie en een samenvatting van het validatieresultaat.

<img src="..\..\images\f12cf678-9432-46de-9b3d-658c878482b2.png"/>

Door de kaart in te zoomen zal een cluster van objecten 'vanzelf' worden opgeheven zodra er voldoende ruimte is tussen de objecten om deze als individuele object op de kaart te kunnen tekenen.

Er bestaat een mogelijkheid dat objecten fysiek op dezelfde locatie liggen (bijvoorbeeld een gemaal met een regelmiddel). In dat geval wordt bij elk zoomniveau van de kaart een clustericoon getoond. Door op het cluster-icoon te klikken worden de individuele objecten alsnog zichtbaar.

Het is mogelijk om de clustering van objecten (iconen) uit te zetten. Dit kan door het vinkje bij ‘Cluster markers' in het paneel met de filteropties (bovenin onder het item 'Map opties’) te verwijderen. Een waarschuwing is hier van kracht: als er heel veel objecten in de databestanden zitten kan het uitzetten van de clustering er voor zorgen dat de browser niet meer in staat is op alle iconen op de kaart te tekenen, waardoor de applicatie 'vastloopt’. Doe dit alleen als de dataset beperkt is of als de kaart voldoende is ingezoomd. Laat in alle andere gevallen deze optie voor clustering gewoon actief staan.

Bij het valideren van objecten worden rapportcijfers toegekend. Als alle validatieregels slagen dan is het rapportcijfer gelijk aan 10. Bij het falen van een niet-kritieke validatieregel wordt het rapportcijfer verminderd met 1. Bij het falen van een kritieke validatieregel wordt het rapportcijfer verminderd met 5. Afhankelijk van het uiteindelijke beoordelingscijfer van elk object, krijgen de iconen een unieke kleur volgens onderstaande kleurverloop:

- groen: voor beoordelingscijfer 10
- van geel naar oranje: voor beoordelingscijfer 2-9
- rood: voor beoordelingscijfer 0-1

Door op een object te klikken opent u een popup met daarin een tabel met alle validatieregels voor het betreffende object inclusief het validatie resultaat per validatieregel. Bovendien worden de berekende waarde van de parameters uit de 'general\_rules' gepresenteerd.

<img src="..\..\images\afd878cc-d6d8-4275-8f9f-82bcc2889c13.png"/>

## Paneel met filteropties (links)

Aan de linkerzijde van het scherm zit een paneel met de zogenoemde filteropties voor de objecten die weergegeven worden op de kaart.

<img src="..\..\images\db4f7a68-7db3-4e74-9345-f6e396cb7058.png"/>

## Map opties

Naast de eerder besproken optie voor het clusteren van iconen op de kaart en het activeren van een modus voor gebruikers die kleurenblind zijn, is er nog een derde optie ‘Zoom (initieel) naar objecten'. Deze optie staat standaard aan maar kan uitgezet worden door het vinkje te verwijderen. Als deze optie geactiveerd is zal de kaart bij het wisselen van schermen (bijvoorbeeld van en naar de werkruimte voor resultaten in tabellen) altijd weer uit-/ingezoomd worden naar het bereik zodat alle objecten zichtbaar zijn. Door deze optie uit te schakelen, wordt het laatste zoomniveau van de kaart 'vastgehouden’ als er tussen werkruimtes wordt gewisseld. Bij terugkeer naar de kaart zal de kaart het laatst gebruikte zoomniveau weer herstellen.

## Filters

Met name bij grotere dataset met veel objectlagen is het gebruik van de filter-opties in de Webclient een handige toevoeging. Met filters kunnen objecten op de kaart op basis van een specifiek criterium gefilterd worden. Er zijn zes verschillende filtermogelijkheden beschikbaar die ook met elkaar gecombineerd kunnen worden. Elk filter is opgenomen in een in/uitklapbaar item. Met <img src="..\..\images\7631a441-1187-49cb-8a09-54af82917758.png"/>kan een item geminimaliseerd worden en met<img src="..\..\images\0bea3783-4e26-446d-8503-e10c5fc5268b.png"/>kan het item gemaximaliseerd worden zodat alle opties zichtbaar zijn.

### Filter op objecttype

Dit filter staat automatisch aangevinkt en standaard zijn alle type objecten actief. Verwijder en/of plaats vinkjes bij specifieke type objecten om de gewenste selectie van objecten op de kaart zichtbaar te maken. In onderstaand voorbeeld worden alle duiker, sifons en hevels en bruggen getoond in de kaart (en de overige objecten niet).

<img src="..\..\images\5d72d9b6-69ae-4415-92c9-113e51753642.png"/>

### Filter op rapportcijfer

Met dit filter kunnen objecten op de kaart op basis van het rapportcijfer gefilterd worden. Plaats eerst een vinkje bij het filter om het filter actief te maken! Met een slider kan de range van de rapportcijfers worden ingesteld van de objecten die weergegeven moeten worden op de kaart. Default worden alle rapportcijfers weergegeven. In onderstaand voorbeeld worden alleen de objecten met een rapportcijfer van 4 tot en met 7 weergeven op de kaart.

<img src="..\..\images\7801c477-1472-40fd-84d5-963e160fb79e.png"/>

*Tip: Door bijvoorbeeld dit filter te combineren met het filter op type objecten kunt u alleen alle stuwen zichtbaar maken met een rapportcijfer vanaf 4 tot en met 7.*

### Filter op falen validatieregel

Met dit filter kunnen objecten op de kaart gefilterd worden die alleen gevalideerd zijn volgens een specifieke *falende* validatieregel. Plaats eerst een vinkje bij het filter om het filter actief te maken! Voer vervolgens de naam of een gedeelte uit de naam van een validatieregel in. Alleen die objecten waarvoor een validatieregel *faalt* EN waarvan (een gedeelte) van de naam overeenkomt met uw definitie, worden op de kaart getoond.

<img src="..\..\images\b50e0c88-7ec6-466c-9cf2-95ac410658fb.png"/>

### Filter op falen naar gewicht

Met dit filter kunnen objecten op de kaart gefilterd worden die *falen* volgens niet-kritieke of kritiek validatieregels. Plaats eerst een vinkje bij het filter om het filter actief te maken! Maak een keuze tussen ‘critical' en 'non-critical’ respectievelijk kritieke en niet-kritieke validatieregels. Alleen die objecten worden op de kaart getoond die *falen* volgens een minimaal 1 validatieregel van de aangevinkte voorwaarde.

<img src="..\..\images\1f009572-c68b-4a95-b598-6f67a099bc70.png"/>

*Tip: Door beide voorwaarden in dit filter aan te vinken kunt u een overzicht op de kaart krijgen van alle objecten die falen. Dit is overigens ook te realiseren door het filter op rapportcijfer gelijk te kiezen aan 9 of lager.*

### Filter op id-match

Dit filter is bedoeld om snel een specifiek object te zoeken op de kaart. Plaats eerst een vinkje bij het filter om het filter actief te maken! Vul vervolgens een (gedeelte) van de NEN3610id in om een object te filteren op de kaart.

<img src="..\..\images\d9e5e1e3-cf35-43c4-b1be-1597faeb20d6.png"/>

### Filter op categorie oppervlakte waterlichaam

Dit laatste filter is alleen van toepassing op de waterlopen (oppervlakte waterlichamen ook wel aangeduid als de Hydro-objecten). Plaats eerst een vinkje bij het filter om het filter actief te maken! Selecteer vervolgens de gewenste categorie van het waterlichaam (Primair, Secundair, Tertiar en Overige) dat op de kaart getoond moet worden.

<img src="..\..\images\796ba901-6c41-4d06-b60b-6ddd8879a189.png"/>

## Paneel met kaartlagen (rechts)

Aan de rechterzijde van het scherm zit een paneel met de kaartlagen.

<img src="..\..\images\4841ad87-3efc-4d29-9585-7b4a4076fb04.png"/>

### Kaartlagen met objecten

In het bovenste blok worden de kaartlagen van de verschillende type objecten weergegeven. Doro een vinkje te verwijderen kan de weergave op de kaart uitgezet worden. Dit heeft overlap met het filter op objecttype omdat het min of meer hetzelfde doet! Met de zes puntjes voor een kaartlaag <img src="..\..\images\89f85c8e-fca6-43a5-bd59-b44f1c242a6b.png"/>kan een kaartlaag ‘opgepakt' worden en naar boven of beneden 'gesleept’ worden. Hiermee is de volgorde van de opbouw van de kaartlagen in de kaart te beïnvloeden. De onderste kaartlaag wordt als eerste getekend en de bovenste als laatste!

Met de drie puntjes achter een kaartlaag kan een popup geopend worden waarin onder andere de transparantie van de kaartlaag aangepast kan worden (met de slider; links volledig transparant en dus onzichtbaar en rechts volledig zichtbaar). Met de optie 'Centreer kaartlaag' wordt de kaart in-/uitgezoomd zodat alle elementen van de betreffende kaartlaag in beeld zijn.

<img src="..\..\images\90b43102-6d84-4687-8dc6-e11311d19cd5.png"/>

### Overige kaartlagen

In dit blok worden alle kaartlagen getoond die wel in de datasets voorkomen maar niet gevalideerd worden (omdat daar (nog) geen validatieregels beschikbaar voor zijn). Daarnaast wordt hier ook altijd (indien beschikbaar in de dataset uiteraard) een referentie kaartlaag met de waterlichamen (Hydro-objecten) toegevoegd. Deze referentielaag kan aangezet worden om bijvoorbeeld te kunnen beoordelen of sommige objecten (zoals een stuw) samenvallen met een waterlichaam.

Standaard staan de overige kaartlagen niet aan. Plaats een vinkje om deze te activeren en zichtbaar te maken op de kaart. Ook voor deze kaartlagen zijn de mogelijkheden beschikbaar om de volgorde aan te passen en de transparantie te wijzigen.

N.B. het is zelfs mogelijk om de volgorde van de overige kaartlagen met de object kaartlagen om te wisselen. Gebruik hiervoor de drie puntjes voor de naam van het blok

### Achtergrondkaartlagen

Er kunnen vier achtergrondkaartlagen gekozen worden (allen afkomstig van [PDOK](https://www.pdok.nl/achtergrondkaarten1)):

- Topografie: de basisregistratie (BRT) achtergrondkaartlaag in kleur.
- Topografie water: de basisregistratie (BRT) achtergrondkaartlaag met watervlakken (standaard geselecteerd).
- Topografie grijs: de basisregistratie (BRT) achtergrondkaartlaag in grijze kleur.
- Een actuele luchtfoto (ortho).

Daarnaast is het mogelijk om de achtergrondkaartlaag uit te schakelen. Kies dan voor 'Geen achtergrondkaart'.
