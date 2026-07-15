# Validatieregels

Bijgewerkt tot versie: 1.4.0

Sets met validatieregels voor de Validatiemodule zijn beschikbaar op een daarvoor aangemaakte [GitHub-pagina](https://github.com/HetWaterschapshuis/HyDAMOValidatieregels). Op deze pagina kunt u bestanden met validatieregels, waaronder een actuele [voorbeeldset](https://github.com/HetWaterschapshuis/HyDAMOValidatieregels/blob/main/validation_rules/ValidationRules.json) die u kunt gebruiken voor het valideren van uw HyDAMO gegevens.

De structuur waaraan uw bestand met validatieregels (validationrules.json) moet voldoen zijn vastgelegd in een [JSON-schema](https://github.com/HetWaterschapshuis/HyDAMOValidatieregels/blob/main/schemas), welke u kunt gebruiken voor het valideren van uw JSON voorafgaand aan het gebruik van de validatiemodule. Ook de validatiemodule zal zelf het de JSON met validatieregels valideren aan het JSON-schema voorafgaand aan de datavalidatie zelf.

Op deze pagina vindt u een beschrijving van de objecten binnen het validatie JSON bestand:

- [schema](#schema)
- [hydamo\_version](#hydamo_version)
- [status\_object](#status_object)
- [objects](#objects)
  - [general\_rules (optioneel)](#general_rules-optioneel)
    - [id](#id-general)
    - [result\_variable](#result_variable-general)
    - [function](#function-general)
  - [validation\_rules (optioneel)](#validation_rules-optioneel)
    - [id](#id)
    - [name](#name)
    - [type](#type)
    - [validation\_rule\_set](#validation_rule_set)
    - [exceptions](#exceptions)
    - [tags](#tags)
    - [filter](#filter)
    - [error\_type](#error_type)
    - [error\_message](#error_message)
    - [result\_variable](#result_variable)
    - [active](#active)
    - [function](#function)

# schema

De versie van het JSON-schema waaraan dit bestand moet voldoen.

# hydamo\_version

De versie van HyDAMO waaraan de objecte-lagen en attributen binnen de object-lagen aan moeten voldoen. We ondersteunen op dit moment alleen HyDAMO versie 2.2.

# status\_object

Een lijst met statussen waarop de datasets worden gefilterd. De mogelijke waarden hierin volgen de enumeratie van attribuutwaarden binnen het attribuut *status\_object* van elke object-laag.

# objects

Een lijst met hydamo object-lagen waarover contextuele datavalidatie wordt uitgevoerd. Elk item in de lijst bevat de volgende JSON-elementen, die in de secties hieronder nader worden toegelicht:

- [object-(verplicht)
- [general\_rules-(optioneel)](#general_rules-optioneel))
- [validation\_rules-(optioneel)](#validation_rules-optioneel)

## general\_rules (optioneel)

Een optionele lijst met algemene regels die nieuwe numerieke variabele genereren binnen de HyDAMO object-laag. Deze variabelen zijn vanaf dat punt beschikbaar voor validatieregels en/of general\_rules van andere object-lagen. Binnen general\_rules worden de volgende objecten gespecificeerd

### **id-general**

(integer-waarde) de index van de validatieregel; bepaald de volgorde waarin deze in de resultaattabel wordt opgenomen

### **result\_variable-general**

bepaalt attribuut-naam samen met id: *general\_{id}\_{result\_variable}*

### **function-general**

de functie waarmee de result\_variable wordt berekend. Deze functies vormen de kern van de general\_rules en staan beschreven in [Functies](Validatieregels/01%20Functies.md).

## validation\_rules (optioneel)

(Topo)logische validatieregels die beoordelen of een object of attribuut-waarde wel of niet logisch zijn.

### **id**

(integer-waarde) de index van de validatieregel; bepaalt de volgorde waarin deze in de resultaattabel wordt opgenomen

### **name**

een beschrijvende naam voor de validatieregel

### **type**

logic/topologic, type validatieregel

### **validation\_rule\_set**

identificatie van de set waarbinnen de regel hoort, waarmee de gebruiker kan filteren

### **exceptions**

een lijst met nen3610ids die moeten worden uitgesloten van validatie

### **tags**

optionele lijst met tags waarop de gebruiker kan filteren

### **filter**

een filter voor het opnemen/uitsluiten van objecten in de validatieregel middels een logische functie

### **error\_type**

critical/non-critical, indicatie voor het gewicht van de regel

### **error\_message**

foutmelding die in *samenvatting* wordt bijgeschreven wanneer een object faalt op een bepaalde regel

### **result\_variable**

bepaalt attribuut-naam samen met id: validate\_{id}\_{result\_variable}

### **active**

optie om een validatieregel mee te nemen/uit te sluiten in validatie

### **function**

de functie waarmee de validatie wordt uitgevoerd. Deze functies formen de kern van de validation\_rules en worden afhankelijk van het [type](#type) (logic/topology) uitgevoerd met de functies beschreven in:

- [Functies](Validatieregels/01%20Functies.md)
