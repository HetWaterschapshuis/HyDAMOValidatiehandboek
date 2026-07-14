
# Validatieregels toevoegen aan een validatietaak

De HyDAMO Validatietool is zo ontwikkeld dat het mogelijk is om zelf (per validatietaak) te bepalen welke validatieregels toegepast moeten worden. Validatieregels worden gedefinieerd in een Json bestand. Voor een overzicht van de basisset met validatieregels zie hier [Basis validatieregels](..\..\05%20Basis%20validatieregels.md). Voor meer informatie over de definitie van de validatieregels in het Json bestand zie [Validatieregels](..\..\HyDAMO%20Validatiemodule\02%20Validatieregels.md). U kunt een (aangepast) Json bestand met validatieregels controleren aan de hand van een [Json schema](https://github.com/HetWaterschapshuis/HyDAMOValidatieregels/blob/main/schemas/rules_0.9.0.json). Gebruik hiervoor eventueel een online tool zoals [jsonschemavalidator](https://www.jsonschemavalidator.net/).

Om een Json bestand met validatieregels toe te voegen selecteert u eerst een validatietaak in de tabel met validatietaken.

<img src="..\..\..\images\a9454ce4-058b-4c24-80d7-ce9d735169c7.png"/>

U kunt nu op twee manieren een bestand met validatieregels toevoegen aan de geselecteerde validatietaak:

1. Klik ergens in het oranje vlak van de ‘Validatieregels’. Er wordt een bestandsdialoog geopend waarin u een Json bestand met validatieregels kunt selecteren.
2. Selecteer een Json bestand met validatieregels (bijvoorbeeld in de Windows Verkenner) en sleep deze op het oranje vlak van de ‘Validatieregels’.

Zodra het JSON bestand met validatieregels is toegevoegd wordt de tabel met validatieregels gevuld. Deze tabel bevat de volgende kolommen (van links naar rechts):

- De status van validatieregel (vinkje als de regel actief is en een kruisje als de regel inactief is).
- De naam van het bestand waaruit de validatieregel is gelezen.
- Op welk DAMO object de validatieregel van toepassing is.
- De omschrijving van de validatieregel.
- Of voor de validatieregel uitzonderingen (objecten die uitgesloten worden van validatie met deze validatieregel) zijn gedefinieerd.

<img src="..\..\..\images\9fd93f52-f93f-4ffa-afa1-6b0536f1237e.png"/>

N.B. in deze tabel worden alleen de logische en topologische validatieregels weergegeven. De syntax validatieregels kunt u [Basis validatieregels](..\..\05%20Basis%20validatieregels.md) bekijken.

Als u per ongeluk een verkeerd Json bestand met validatieregels heeft toegevoegd zult u een nieuw bestand moeten selecteren. Het is niet mogelijk om validatieregels te verwijderen. Het is wel mogelijk om een ingelezen validatieregel via de HyDAMO Webclient te deactiveren (of weer te activeren als deze eerder gedeactiveerd werd). Klik hiervoor op de knop ‘Bewerkingsmodus inschakelen'. In de kolom ‘Actief’ is het nu mogelijk om vinkjes te verwijderen of te plaatsen. Dit kan alleen bij validatieregels en niet bij de algemene rekenregels ('general rules’). Nadat u aanpassen hebt gedaan kunt u deze opslaan door de knop 'Wijzigingen opslaan' te activeren. De HyDAMO Webclient bewaard de aangepaste instellingen ook als u deze opnieuw laadt.

Merk op dat na het toevoegen van validatieregels aan een validatietaak (in het geval dat er minimaal 1 dataset bestand aanwezig is), de status van de validatietaak wordt aangepast in 'ready\_to\_validate'.

<img src="..\..\..\images\44193ae5-83ca-490a-9459-b51289cfdadd.png"/>

De volgende stap is het daadwerkelijk starten van de validatietaak (zie [Een validatietaak starten](04%20Een%20validatietaak%20starten.md)).
