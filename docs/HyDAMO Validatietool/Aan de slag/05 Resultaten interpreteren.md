# Resultaten

Aan het einde van een validatie heeft de gebruiker verschillende mogelijkheden om de resultaten te verkrijgen. Bij een validatie via de webclient kun je de [resultaten op de kaart](02%20De%20Webclient.md#9-bekijken-van-resultaten-op-de-kaart) bekijken en zijn de uitkomsten door kleurgeving en labels van enige interpretatie voorzien. Bij gebruik van de Validatie-API of de losse validatiemodule kun je de validatielog en verschillende uitvoerbestanden downloaden (alle bestanden zijn uiteraard ook in de Webviewer beschikbaar voor download). Hieronder vind je een toelichting op de interpretatie van de resultaten.

## Samenvatting (validation_result.json)

De samenvatting staat in het bestand validation_result.json. Dit bestand wordt ook wel **metadata** of uitgebreid **logbestand** genoemd. Je kunt dit bestand bijvoorbeeld met een teksteditor bekijken. Hieronder staat een voorbeeld van een samenvatting van een succesvol uitgevoerde validatie:

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

 De belangrijkste uitkomsten vind je onder de volgende JSON-sleutels:

- **success** (true/false): alleen als de waarde true is, is de validatie volledig uitgevoerd,
- **module_version**: de versie van de validatiemodule die is gebruikt,
- **date_check**: de lokale datum en tijd waarop de validatie is gestart,
- **duration** (nummer): de tijd in seconden die de validatie heeft geduurd,
- **status**: geeft aan tot welke stap de validatiemodule is gekomen: *initialization, define data-model, syntax-validation (layers), syntax-validation (fields), logical validation, export results, finished.* Een geslaagde validatie (succes=true) heeft altijd status=finished,
- **error**: een foutmelding gevolgd door een Python-exception. Alleen zichtbaar als *success=false* en *status != finished*,
- **errors**: deze sleutel is alleen zichtbaar wanneer een of meer *general_rules* of *validation_rules* uit validationrules.json een Python-exceptie veroorzaken. De module gaat na elke exceptie verder met de volgende regel. Deze fouten hebben zelf geen invloed op de waarden van *status* en *success*,
- **dataset_layers** (array): lagen zoals aangeboden in de dataset-GeoPackage(s),
- **result_layers** (array): de lagen die te downloaden zijn als resultaat,
- **missing_layers**: lagen die onderdeel zijn van het datamodel, maar niet aanwezig zijn in de dataset,
- **error_layers**: aangeboden lagen die de tool niet kon valideren,
- **syntax_result** (array): lagen waarvoor een *syntax_oordeel* beschikbaar is,
- **validation_result** (array): lagen waarvoor *validation_rules* zijn uitgevoerd.

## Resultaat als objectlaag (GeoPackage, CSV, GeoJSON)

Je kunt de resultaten ook als objectlaag downloaden. Voor resultaten in CSV- en GeoJSON-formaat wordt een bestand per objectlaag aangemaakt. Bij een GeoPackage zijn alle lagen in een bestand samengevoegd. De validatie-uitkomsten staan per feature in de toegevoegde resultaatkolommen.

### Foutcodes bij syntaxfouten

De resultaatkolommen met betrekking tot syntaxcontroles (syntax_{kolom_naam}) kunnen worden samengezet tot één syntax-oordeel in de vorm van:

*oorspronkelijke_waarde → NULL (fouten: #,#,#)*

Het deel *oorspronkelijke_waarde → NULL* komt alleen voor als de oorspronkelijke waarde is gewijzigd naar NULL. Het veld wordt dan leeggemaakt.

Het deel *(fouten: #,#,#)* bevat de foutcodes 1 tot en met 7 die voor dit object zijn vastgesteld:

- **1 = invalid_dtype_error**: de oorspronkelijke waarde heeft niet het juiste gegevenstype en kan niet worden geconverteerd (waarde wordt verwijderd), 
- **2 = invalid_dtype**: de oorspronkelijke waarde heeft niet het juiste gegevenstype, maar kan wel worden geconverteerd,
- **3 = non_unique_values**: de oorspronkelijke waarde is niet uniek (waarde wordt verwijderd),
- **4 = missing_values**: deze verplichte kolom ontbreekt volledig of bevat geen waarde, naast null worden ook de domeinwaarden 98 en 99 ('overig', 'onbekend') als ontbrekend beschouwd,
- **5 = fill_values**: de ongeldige vulwaarde -999 is gedetecteerd (waarde wordt verwijderd),
- **6 = non_domain_values**: er is een waarde vastgesteld die niet binnen het toegestane keuzedomein valt (waarde wordt verwijderd),
- **7 = invalid_geometry**: er is een ongeldige geometrie of een geometrie van het verkeerde type vastgesteld (geometrie wordt verwijderd).

### Resultaatkolommen

Alle uitvoerbestanden bevatten de volgende resultaatkolommen:

- **nen3610id** (string): de unieke ID van het object volgens de NEN 3610-norm,
- **code** (string): de waterschapscode van het object,
- **syntax_{kolom_naam}** (string): het resultaat van de syntaxvalidatie per item ten opzichte van het HyDAMO-datamodel,
- **syntax_oordeel** (true/false): alle syntaxvalidaties zijn hier samengevat: true als er geen syntax-fouten zijn opgetreden, anders false,
- **general_{id:03d}_{result_variable}** (numeriek): uitkomst van een algemene regel, oftewel *general_rule*, gespecificeerd met *id* en *result_variable* van de desbetreffende regel,
- **validate_{id:03d}_{result_variable}** (true/false): uitkomst van een logische regel, oftewel *validation_rule*, gespecificeerd met *id* en *result_variable* van de desbetreffende (topo-)logische regel,
- **rating** (integer): het rapportcijfer: 10 is de hoogste beoordeling en 0 de laagste,
- **summary** (string): een samenvatting van alle *error_message*s van alle gefaalde (topo-)logische validatieregels op dit object,
- **valid** (string): de *regel-id's* van alle (topo-)logische validatieregels die slagen voor dit object,
- **invalid** (string): de *regel-id's* van alle (topo-)logische validatieregels die falen voor dit object,
- **invalid_critical** (string): uitsplitsing van de 'invalid' regel-id's met de aanduiding 'kritiek',
- **invalid_non_critical** (string): uitsplitsing van de 'invalid' regel-id's met de aanduiding 'niet-kritiek',
- **ignored** (string): de regel-id's van (topo-)logische validatieregels die genegeerd worden (input = nan, uitgesloten via filter of exceptions) voor dit object,
- **tags_assigned** (string): de tags die aan het object zijn gekoppeld via validatieregels,
- **tags_invalid** (string): de tags die aan het object zijn gekoppeld via validatieregels die een niet-plausibel (invalid) resultaat geven,
- **date_check**: De lokale datum en tijd waarop de validatie is gestart.