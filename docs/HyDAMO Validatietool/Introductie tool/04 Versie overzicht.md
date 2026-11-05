---
hide:
- toc
---

# Versieoverzicht

Op deze pagina vind je de actuele versies van de verschillende componenten van de HyDAMO-validatietool.

|  **Component**             |  **Versie**                                                                         |  **Releasedatum**    |
|:---------------------------|:------------------------------------------------------------------------------------|:---------------------|
| HyDAMO-validatiemodule     | 1.6.0 (ondersteuning voor HyDAMO 2.5) <br/> LET OP: zie opmerking onder deze tabel! | 17-08-2026           |
| HyDAMO-validatie-API       | 1.2.4.2 (verwerken grote invoerbestanden)                                           | 31-08-2026           |
| HyDAMO-validatie-webclient | 2.0.22 (facelift Webclient, verwerken grote invoerbestanden)                        | 31-08-2026           |

Let op: als je rekenmodule **versie 1.3.0** of hoger gebruikt, moet je het JSON-bestand met validatieregels als volgt aanpassen:

- verwijs bovenin naar de laatste versie van het schema → "schema": "1.5",
- Voor het attribuut hydamo_version kun je nu de waarde 2.2, 2.3, 2.4 of 2.5 kiezen.

## Release notes

**HyDAMO-validatiemodule**

Zie ook de uitgebreide [release notes](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule/releases){ target="_blank" } op de openbare GitHub-repository.

|  **Versie**    |  **Status**    |
|:---------------|:---------------|
| **Versie 1.6.0** <br/> 21.07.2026 | HyDAMO 2.5-ondersteuning toegevoegd |
| **Versie 1.5.0** <br/> 26.02.2026 | Ondersteuning voor Python 3.12 toegevoegd en overgestapt op omgevingsbeheer met pyproject en uv.<br>Python-bibliotheken bijgewerkt.<br> Kolom voor filteren van resultaten op categorie waterlichaam toegevoegd. |
| **Versie 1.4.0** <br/> 13.05.2025 | HyDAMO 2.4 ondersteuning toegevoegd.<br/>Filteren op de categorie van het oppervlaktewaterlichaam (primair/secundair) toegevoegd aan de validatieregel 'splitted_at_junction' voor hydro-objecten.|
| **Versie 1.3.1** <br/> 07.10.2024 | Aanpassing validatie van PointZ-objecten als gevolg van het wegvallen van de ondersteuning van dit geometrieformaat in de laatste versie van Shapely |
| **Versie 1.3.0** <br/> 20.03.2024 | Python-pakketten bijgewerkt, waaronder het pakket voor het lezen en schrijven van GeoPackages en GeoJSON-bestanden. Dit levert een aanzienlijke prestatieverbetering op. <br/>Vanaf deze versie ondersteunt de module ook HyDAMO-JSON 2.3 (conform DAMO 2.3). Zie ook \<https://github.com/HetWaterschapshuis/HyDAMOValidatieModule/blob/main/hydamo_validation/schemas/hydamo/HyDAMO_2.3.json\> <br/> Bug opgelost door de unieke id van objecten niet meer de NEN3610id, maar de FID te laten zijn. <br/>Een fout opgelost waardoor lege GeoDataFrames konden ontstaan en de module tijdens de syntaxvalidatie een foutmelding gaf.<br/> Een extra logbestand (validator.log) toegevoegd met een uitgebreider overzicht van de voortgang van de module|
| **Versie 1.2.0** <br/> 15.12.2023 | Order als attribuut verwijderd uit de validatieregels <br/> Functie voor bepalen overlappende objecten verbeterd (duikersifonhevel, gemaal en stuw) |
| **Versie 1.1.0** <br/> 29.03.2022 | Sturing en profielen toegevoegd <br/> Bug uitzetten van validatieregel (active=false) opgelost <br/> Bug in functie 'structures\_at\_boundaries' gebruikt bij hydro-objecten opgelost <br/> Bug bij rapportage van eindresultaat syntaxvalidatie opgelost |
| **Versie 1.0.1** <br/> 17.02.2022 | Bugfix: Een dataset-GeoPackage veroorzaakt een Error: Python Exception. tijdens de validatie bij niet-unieke objecten (unieke NEN3610id) |
| **Versie 1.0.0** <br/> 14.02.2022 | Lancering      |


**HyDAMO validatie-API**

|  **Versie**    |  **Status**    |
|:---------------|----------------|
| **Versie 1.2.5 en 1.2.6**  <br/> 18.08.2026 | Aangepaste GeoJSON-generatie i.v.m. het verwerken van grote invoerbestanden |
| **Versie 1.2.4**  <br/> 20.07.2026 | Ondersteuning nieuwe versie webclient |
| **Versie 1.2.3**  <br/> 06.07.2026 | Modernisering Docker-imagegeneratie, update Python-versie naar 3.12, update libraries |
| **Versie 1.2.1 en 1.2.2**  <br/> 18.02.2026 | Bijwerken metadata o.a. met aangepast mailadres helpdesk |
| **Versie 1.2.0**  <br/> 06.11.2024 | Een tijdelijke oplossing in de API geïmplementeerd voor een fout waarbij meerdere cloudinstanties dezelfde rekentaak tegelijk konden verwerken. |
| **Versie 1.1.1** <br/> 19.05.2024 | Kleine verbetering in download van resultaten   |
| **Versie 1.1.0** <br/> 10.05.2023 | De API uitgebreid met een endpoint waarmee alle resultaten als ZIP-bestand kunnen worden gedownload. |
| **Versie 1.0.0** <br/> 16.02.2022 | Lancering  |



**HyDAMO validatie-webclient**

|  **Versie**  |  **Status**   |
|:-------------|:--------------|
| **Versie 2.0.22** <br/> 31.08.2026 | Een volledige vernieuwing van de webclient, waarin verschillende wensen van gebruikers zijn verwerkt, zoals het kunnen bekijken van datasets voordat een validatie is gestart, het 'vasthouden' van het kaartzoombereik bij het wisselen tussen schermen, etc. |
| **Versie 1.2.2** <br/> 24.11.2022 | Download van alle resultaatbestanden nu in een ZIP-bestand. Wait cursor toegevoegd bij het uploaden van een GeoPackage-databestand.  |
| **Versie 1.2.0** <br/> 01.11.2022 | Voor elke taak is een downloadknop toegevoegd waarmee het volledige resultaat van een validatie kan worden gedownload (metadatabestand (JSON) + validatieresutlaten in GeoPackage, CSV-bestanden en GeoJSON-bestanden voor elk objecttype). <br/> Het inladen van grote datasets kan enige tijd duren. Om weer te geven dat de Webclient bezig is de data te laden, is een loading spinner toegevoegd. Dit is ook het geval bij het downloaden van CSV-bestanden uit de tabellen. <br/> Bij grote gebieden gaat de performance van de kaart omlaag. Om die reden is standaard de objectlaag met profielpunten uitgezet in de Webclient. |
| **Versie 1.1.3** <br/> 28.03.2022 | Sturing en profielen toegevoegd <br/> Bug opgelost bij uploaden van datasets bij meer dan 1 taak in takenoverzicht <br/> Bug in filter op rapportcijfer van hydro-objecten opgelost  |
| **Versie 1.1.0, 1.1.1 en 1.1.2** <br/> 26.03.2022 | Niet vrijgegeven  |
| **Versie 1.0.3** <br/> 24.02.2022 | Bugfix: Bij het gebruik van meerdere taken in de takenlijst wordt een datasetbestand aan de verkeerde (altijd de eerste) taak uit de takentabel toegevoegd. |
| **Versie 1.0.1 en 1.0.2** <br/> 23.02.2022 | Niet vrijgegeven   |
| **Versie 1.0.0** <br/> 11.02.2022 | Lancering          |

