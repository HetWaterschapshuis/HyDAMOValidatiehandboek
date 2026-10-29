# Resultaten

Aan het einde van een validatie heeft de gebruiker verschillende mogeljkheden om de resultaten te verkrijgen. Bij een validatie met behulp van de webclient is het mogelijk om de [resultaten op de kaart](TODO hier de link toevoegen) met enig interpretatie van de uitkomsen te bekijken. Bij gebruik van de Validatie-API of de losse validatiemodule kan de validatie-log en een set van verschillende uitvoerbestanden gedownload worden. Alle bestanden kunnen uiteraard ook in de Webviewer gedownload worden. Hieronder is een handreiking van hoe de resultaten te interpreteren zijn.

## Samenvatting (validation_result.json)

De samenvatting zit in het bestand validation_result.json en wordt ook **metadata** genoemd of uitgebreid **log-bestand**. Je kan hem goed bekijken met bijvoorbeeld een teksteditor. Een voorbeeld van een sammenvatting bij een succesvol uitgevoerde validatie:

```json
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

 Belangrijke uitkomsten vind je onder de volgende JSON-keys:

- **success**: true/false alleen bij true is de validatie volledig uitgevoerd
- **module_version**:de versie van de validatiemodule die is gebruikt
- **date_check**: De lokale datum-tijd waarop de validatie is gestart
- **duration**: nummer, de tijd in seconden die de validatie heeft geduurd
- **status:** geeft aan tot welke stap de validatiemodule is gekomen: *initialization, define data-model, syntax-validation (layers), syntax-validation (fields), logical validation, export results, finished.* Een geslaagde validatie (succes=true) heeft altijd status=finished.
- **error:** een foutmelding gevolgd door een Python-exception. Alleen zichtbaar als *succes=false* en *status != finished*
- **errors**: deze is alleen zichtbaar wanneer een of meerdere *general\_rules* of *validation\_rules* uit de validationrules.json een Python-exception veroorzaakt. De module zal bij elke exception doorgaan met de volgende regel uit de validationrules.json. Bij deze errors hebben zelf geen invloed op de *status* en *succes* waarden*.*
- **dataset_layers:** array,lagen zoals aangeboden in de dataset GeoPackage(s)
- **result_layers:** array, de lagen die te downloaden zijn als resultaat
- **missing_layers**: lagen die onderdeel zijn van het datamodel, maar niet aanwezig zijn in de dataset
- **error_layers:** aangeboden lagen die niet konden worden gevalideerd
- **syntax_result:** array, lagen waarvoor een *syntax\_oordeel* beschikbaar is
- **validation_result:** array, lagen waarvoor *validation\_rules* zijn uitgevoerd



## Resultaat als objectlaag (GeoPackage, csv, GeoJSON)

Je kan de resultaten ook per als objectlagen downloaden. Voor resultaten in csv- en GeoJSON-formaat wordt een bestand per objectlaag aangemaakt. Bij een GeoPackage zijn alle lagen in een bestand samengevoegd. De validatie-uitkomsten staan per feature in de toegevoegde resultaat-kolommen.


### Resultaat-kolommen

Alle uitvoebestanden bevatten de volgende, resultaat-kolommen:

- **nen3610id** (string): de unieke id van het object volgens NEN 3610 norm
- **code** (string): de waterschapscode van het object
- **syntax_{kolom_naam}** (string): het resultaat van de syntax-validatie per item (velddefinitie) van het HyDAMO-datamodel
- **syntax_oordeel** (true/false): alle syntax-validaties zijn hier samengevat: true als er geen syntax-fouten zijn opgetreden, anders false
- **general_{id:03d}_{result_variable}** (numeriek): uitkomst van een algemene regel, oftewel *general_rule*, gespecificeerd met *id* en *result_variable* van de desbetreffende regel
- **validate_{id:03d}_{result_variable}** (true/false): uitkomst van een logische regel, oftewel *validation_rule*, gespecificeerd met *id* en *result_variable* van de desbetreffende (topo-)logische regel
- **rating** (integer): het rapportcijfer, waarbij 10 de hoogste beoordeling is en 0 de laagste.
- **summary** (string): een samenvatting van alle *error_message*s van alle gefaalde (topo-)logische validatieregels op dit object
- **valid** (string): de *regel-id's* van alle (topo-)logische validatieregels slagen voor dit object
- **invalid** (string): de *regel-id's* van alle (topo-)logische validatieregels die falen voor dit object
- **invalid_critical** (string): uitsplitsing van de 'invalid' regel-id's met de aanduiding 'kritiek'
- **invalid_non_critical** (string): uitsplitsing van de 'invalid' regel-id's met de aanduiding 'niet-kritiek'
- **ignored** (string): de regel-id's van (topo-)logische validatieregels die genegeerd worden (input = nan, uitgesloten via filter of exceptions) voor dit object
- **tags_assigned** (string): de tags die aan het object zijn gekoppeld via validatieregels
- **tags_invalid** (string): de tags die aan het object zijn gekoppeld via validatieregels die een niet-plausibel (invalid) resultaat geven
- **date_check**: De lokale datum-tijd waarop de validatie is gestart

### Fout-codes bij syntaxfouten

De resultaat-kolommen met betrekking tot syntax-controles (syntax_{kolom_naam}) kunnen een samengezet syntax-oordeel bevatten in de vorm van:

*oorspronkelijke_waarde → NULL (fouten: #,#,#)*

Het deel *oorspronkelijke_waarde → NULL* komt alleen voor als een mutatie van de oorspronkelijke waarde naar NULL heeft plaats gevonden. Het veld wordt dan leeggemaakt.

Het deel *(fouten: #,#,#)* geeft met de getallen 1 t/m 7 de code van de fouten weer die gedetecteerd zijn voor dit object:

- **1 = invalid_dtype_error**: de oorspronkelijke waarde is niet van het juiste data-type en kan niet geconverteerd worden (waarde wordt verwijderd),
- **2 = invalid_dtype**: de oorspronkelijke waarde is niet van het juiste data-type maar kan wél geconverteerd worden,
- **3 = non_unique_values**: de oorsprokelijke waarde is niet uniek (waarde wordt verwijderd),
- **4 = missing_values**: deze verplichte kolom ontbreekt compleet of komt voor maar bevat geen waarde, naast null worden ook de domeinwaarden 98 en 99 ('overig', 'onbekend') als ontbrekend gedetecteerd,
- **5 = fill_values**: de ongeldige vulwaarde -999 is gedetecteerd (waarde wordt verwijderd),
- **6 = non_domain_values**: een waarde is gedetecteerd die niet binnen het toegestaane keuzedomein valt (waarde wordt verwijderd),
- **7 = invalid_geometry**: een niet-valide geometrie of een geometrie van een onjuist type is gedetecteerd (geometrie wordt verwijderd).
