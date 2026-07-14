# Een validatietaak starten

Een validatietaak kan pas gestart worden als wordt voldaan aan twee voorwaarden:

- Er is minimaal 1 dataset bestand toegevoegd aan de validatie-taak.
- Er is een bestand met minimaal 1 validatieregel toegevoegd aan de validatie-taak.

Als aan beide voorwaarden voldaan is zal de status van de validatietaak gelijk zijn aan ‘ready\_to\_validate' en wordt de knop 'Start validatietaak’, onderin het scherm van de werkruimte voor het beheren van validatietaken actief.

<img src="..\..\..\images\bde456da-8fb1-4b63-a1d0-62188ef721a2.png"/>

Om de validatietaak te starten activeert u de knop ‘Start validatietaak'. De status van de geselecteerde validatietaak zal in eerste instantie wijzigen in ‘pending’. Afhankelijk van de beschikbare capaciteit in de online (reken)omgeving (er kunnen maximaal 3 validatietaken simultaan uitgevoerd worden) wordt de validatietaak meteen gestart of wordt de validatie-taak in een wachtrij geplaatst en gestart zodra op 1 van de 3 rekennodes beschikbaar komt. De status zal dan wijzigen in ‘validating’.

De validatietaak is klaar als de status van ‘validating' wijzigt in ‘finished’ (de validatietaak is zonder foutmelding tot een goed einde gekomen) of in 'error’ (de validatietaak is voortijdig gestopt door een fout).

De volgende stap is het bekijken en analyseren van de resultaten van de validatietaak (zie [Resultaten van een validatietaak bekijken](05%20Resultaten%20van%20een%20validatietaak%20bekijken.md)).
