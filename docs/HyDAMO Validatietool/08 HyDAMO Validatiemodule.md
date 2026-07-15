# HyDAMO Validatiemodule

De HyDAMO Validatiemodule voert de daadwerkelijke validatie van één of meerdere datasets (conform DAMO 2.5 datamodel) uit aan de hand van set validatieregels. De Validatiemodule is een Python toepassing en wordt op een centrale server aangeboden voor gebruik in combinatie met de HyDAMO Validatie-API en/of de HyDAMO Validatiemodule Webclient.

De HyDAMO Validatiemodule voert drie soorten validaties uit:

1. Syntax validatie: gevalideerd wordt of de dataset voldoet aan de vereiste voorwaarden voor het juiste type geometrie (point, linestring, polygon, etc.), voor gebruik van de juiste type waarde (tekst, integer, float, etc.), of alle verplichte attributen gevuld zijn en of alle waarde binnen de gestelde keuzedomeinen vallen. De vereiste voorwaarden zijn gesteld in het HyDAMO datamodel (op dit moment DAMO 2.5). Voor een beschrijving van het datamodel zie [DAMO Objectenboek](https://damo.hetwaterschapshuis.nl/DAMO%202.6/Objectenhandboek%20DAMO%202.6/html/DAMO%20Objectenhandboek.html) en het [JSON-schema](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule/blob/main/hydamo_validation/schemas/hydamo/HyDAMO_2.2.json).
2. Logische validatie: gevalideerd wordt of de dataset plausibele waarden (o.b.v. een specifiek domein) bevat en of de waarden (contextueel) logisch zijn.
3. Topologische validatie: gevalideerd wordt of de dataset aan de geografische eisen qua ligging van objecten (zoals ‘ligt exact op', 'ligt binnen x meter van’, etc.) voldoet.

Zie hier voor meer informatie over het gebruik van de HyDAMO Validatiemodule op de onine omgeving (Validatie as a service) in combinatie met:

- de HyDAMO Validatiemodule Webclient
- een script waarin de HyDAMO Validatie-API wordt gebruikt

Het is ook mogelijk om de HyDAMO Validatiemodule als losse module op een lokaal systeem te gebruiken (lees verder).

## Lokale versie van de HyDAMO Validatiemodule

Starten met de HyDAMO validatiemodule als lokale Python installatie:

1. Installeer op een lokaal systeem de laatste versie van de HyDAMO validatiemodule door het volgen van
2. de instructies op de [GitHub-pagina](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule/).
3. Een voorbeeld van een validatie inclusief eenbeschrijving staat in deze [Jupyter Notebook](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule/blob/main/notebooks/test_wrij.ipynb).

Alle overige informatie voor het gebruik van een lokale installatie van de HyDAMO Validatiemodule vindt u op deze paginas:

- [Uitvoeren van een validatie](HyDAMO%20Validatiemodule/01%20Uitvoeren%20van%20een%20validatie.md)
- [Validatieregels](HyDAMO%20Validatiemodule/02%20Validatieregels.md) en [Functies](HyDAMO%20Validatiemodule/Validatieregels/01%20Functies.md)
- [Resultaten](HyDAMO%20Validatiemodule/03%20Resultaten.md)
