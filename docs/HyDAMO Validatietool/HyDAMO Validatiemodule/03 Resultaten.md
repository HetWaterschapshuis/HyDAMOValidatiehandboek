# Resultaten

De beschijving van resultaten zijn bijgewerkt tot versie 0.9.6 van de Validatiemodule. Hieronder staan de resultaten van de Validatiemodule beschreven uitgesplitst naar:

- [Samenvatting (validation\_result.json)](#samenvatting-validation_resultjson)
- [Per object-laag (geopackage, csv en geojson)](#per-object-laag-geopackage-csv-en-geojson)
  - [Kolomnamen](#kolomnamen)
  - [Enumeratie van syntax-fouten](#enumeratie-van-syntax-fouten)

# Samenvatting (validation\_result.json)

Dit bestand wordt bevraagd via de API wanneer de gebruiker de metadata opvraagt. De validatiemodule levert de volgende eigenschappen:

- **succes**: true/false alleen bij true is de validatie volledig succesvol uitgevoerd
- **module\_version**:de versie van de validatiemodule die is gebruikt
- **date\_check**: De lokale datum-tijd waarop de validatie is gestart
- **duration**: nummer, de tijd in seconden die de validatie heeft geduurd
- **status:** geeft aan tot welke stap de validatiemodule is gekomen: *initialization, define data-model, syntax-validation (layers), syntax-validation (fields), logical validation, export results, finished.* Een geslaagde validatie (succes=true) heeft altijd status=finished.
- **error:** een foutmelding gevolgd door een Python Exception. Alleen zichtbaar als *succes=false* en *status != finished*
- **errors**: deze is alleen zichtbaar wanneer een of meerdere *general\_rules* of *validation\_rules* uit de validationrules.json een Python-exception veroorzaakt. De module zal bij elke exception doorgaan met de volgende regel uit de validationrules.json. Bij deze errors hebben zelf geen invloed op de *status* en *succes* waarden*.*
- **dataset\_layers:** array,lagen zoals aangeboden in de dataset GeoPackage(s)
- **result\_layers:** array, de lagen die te downloaden zijn als resultaat
- **missing\_layers**: lagen die onderdeel zijn van het datamodel, maar niet aanwezig zijn in de dataset
- **error\_layers:** aangeboden lagen die niet konden worden gevalideerd
- **syntax\_result:** array, lagen waarvoor een *syntax\_oordeel* beschikbaar is
- **validation\_result:** array, lagen waarvoor *validation\_rules* zijn uitgevoerd

Een voorbeeld van een sammenvatting bij een succesvol uitgevoerde validatie:

```java
{
    "success": true,
    "module_version": "0.9.4",
    "date_check": "2022-01-25T15:36:50.082241",
    "duration": 13.35630178451538,
    "status": "finished",
    "dataset_layers": [
        "Afvoergebiedaanvoergebied",
        "Duikersifonhevel",
        "Hydroobject",
        "Regelmiddel",
        "Stuw",
        "Brug",
        "Bodemval",
        "Gemaal",
        "Kunstwerkopening",
        "Pomp"
    ],
    "result_layers": [
        "afvoergebiedaanvoergebied",
        "duikersifonhevel",
        "hydroobject",
        "regelmiddel",
        "stuw",
        "brug",
        "bodemval",
        "gemaal",
        "kunstwerkopening",
        "pomp"
    ],
    "missing_layers": [
        "admingrenswaterschap",
        "afsluitmiddel",
        "aquaduct",
        "beheergrenswaterschap",
        "bijzonderhydraulischobject",
        "doorstroomopening",
        "grondwaterinfolijn",
        "grondwaterinfopunt",
        "grondwaterkoppellijn",
        "grondwaterkoppelpunt",
        "hydrologischerandvoorwaarde",
        "hydroobject_normgp",
        "lateraleknoop",
        "meetlocatie",
        "meetwaardeactiewaarde",
        "normgeparamprofiel",
        "normgeparamprofielwaarde",
        "peilafwijkinggebied",
        "peilbesluitgebied",
        "peilgebiedpraktijk",
        "peilgebiedvigerend",
        "profielgroep",
        "profiellijn",
        "profielpunt",
        "reglementgrenswaterschap",
        "streefpeil",
        "sturing",
        "vispassage",
        "vispassagevlak",
        "vuilvang",
        "zandvang"
    ],
    "error_layers": [],
    "syntax_result": [
        "afvoergebiedaanvoergebied",
        "duikersifonhevel",
        "hydroobject",
        "regelmiddel",
        "stuw",
        "brug",
        "bodemval",
        "gemaal",
        "kunstwerkopening",
        "pomp"
    ],
    "validation_result": [
        "duikersifonhevel",
        "regelmiddel",
        "kunstwerkopening",
        "stuw",
        "brug",
        "pomp",
        "gemaal",
        "hydroobject"
    ],
    "warnings": [
        "5 objecten niet meegenomen in general_rule object: 'duikersifonhevel', id: '1' wegens no_data in invoer.",
        "5 objecten niet meegenomen in general_rule object: 'duikersifonhevel', id: '2' wegens no_data in invoer.",
        "5 objecten niet meegenomen in general_rule object: 'duikersifonhevel', id: '3' wegens no_data in invoer.",
        "2 objecten niet meegenomen in general_rule object: 'stuw', id: '0' wegens no_data in invoer.",
        "2 objecten niet meegenomen in general_rule object: 'stuw', id: '1' wegens no_data in invoer."
    ]
}
```

# Per object-laag (geopackage, csv en geojson)

Per HyDAMO objectlaag wordt er een laag weggeschreven in het mapje **results** en of meerdere bestanden:

1. Als laag in: **results.gpkg**
2. Als csv-bestand: **csv\{object\_laag}.csv**
3. Als geojson-bestand: **geojson\{object\_laag}.geojson**

Zie een [hier](../../downloads/duikersifonhevel.csv) een voorbeeld csv-bestand voor het HyDAMO object duikersifonhevel op basis van module v0.9.4.

## Kolomnamen

Al deze bestanden bevatten de volgende kolomnamen:

- **nen3610id**: string, het nen3610id van het object waarop resultaten worden gerapporteerd
- **code**: string, de waterschapscode van het object
- **syntax\_{kolom\_naam}**: string, het resultaat van de syntax validatie per kolomnaam in het HyDAMO bestand (1 of meerdere kolommen)
- **syntax\_oordeel:** true/false, true als er geen syntax-fouten zijn opgetreden in kolommen, anders false
- **general\_{id:03d}\_{result\_variable}:** numeriek, uitkomst van een *general\_rule*, gespecificeerd naar *id* en *result\_variable (0, 1 of meerdere kolommen)*
- **validate\_{id:03d}\_{result\_variable}:** true/false, uitkomst van een *validation\_rule,* gespecificeerd naar id en result\_variable (*1 of meerdere kolommen)*
- **rating**: integer, het rapportcijfer.
- **summary**: string, een samentrekking van alle *error\_message*s van alle gefaalde validatieregels op dit object
- **valid**: string, de *id*s van de validatieregels die niet falen op dit object
- **invalid**: string de ids van de validatieregels die wel falen op dit object
- **invalid\_critical**: string uitsplitsing van invalid validatie-ids met het predicaat “critical”
- **invalid\_non\_critical**: string uitsplitsing van invalid validatie-ids met het predicaat “non-critical”
- **ignored**: string, de ids van de validatieregels die op een of andere manier (input = nan, uitgesloten via filter en/of exceptions) worden genegeerd voor dit object
- **tags\_assigned**: string, de tags die aan het object zijn gekoppeld via validatieregels
- **tags\_invalid**: string, de tags die aan het object zijn gekoppeld via validatieregels die een niet-plausibel (invalid) resultaat geven
- **date\_check:** De lokale datum-tijd waarop de validatie is gestart

## Enumeratie van syntax-fouten

De kolommen met de vorm **syntax\_{kolom\_naam}** bevatten een syntax-oordeel in de volgende vorm:

*oorspronkelijke\_waarde → NULL (fouten: #,#,#)*

Het deel voor *(fouten: #,#,#)* geeft een mutatie van de oorspronkelijke waarde naar NULL weer; het veld wordt leeggemaakt. Óf dit gebeurd is afhankelijk van de syntax-fout,

1. invalid\_dtype\_error: niet het juiste data-type en niet te converteren (waarde wordt verwijderd)
2. invalid\_dtype: niet het juiste data-type, maar wel te converteren
3. non\_unique\_values: niet unieke waarde (waarde wordt verwijderd)
4. missing\_values: missende waarde, overig of onbekend voor een verplichte kolom (waarde wordt verwijderd)
5. fill\_values: een door HWH gespecificeerde opvulwaarde (waarde wordt verwijderd)
6. non\_domain\_values: een waarde die niet bij het opgegeven keuzedomein valt (waarde wordt verwijderd)
7. invalid\_geometry: een niet valide geometrie of een geometrie van een onjuist type (geometrie wordt verwijderd)

Voorbeeld:

*onbekend-> NULL (fouten: 4)* betekent dat veld-waarde *onbekend* is verwijderd uit een verplichte kolom in het HyDAMO datamodel (code 4).
