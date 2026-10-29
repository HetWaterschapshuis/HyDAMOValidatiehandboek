# Bij een nieuwe versie van de validatieregels of andere noodzaak om de pagina '02 Validatieregels.md'
# te vervangen dit script uitvoeren in commandline met geactiverde .venv

import json
from pathlib import Path

import pandas as pd
from openpyxl.utils import get_column_letter

FUNCTION_DESCRIPTIONS = {
    "LE": "linkerwaarde is minder dan of gelijk aan rechterwaarde",
    "LT": "linkerwaarde is minder dan rechterwaarde",
    "GT": "linkerwaarde is groter dan rechterwaarde",
    "GE": "linkerwaarde is groter dan of gelijk aan rechterwaarde",
    "EQ": "linkerwaarde is gelijk aan rechterwaarde",
    "BE": "waarde ligt tussen de min- en max-waarde",
    "ISIN": "waarde komt voor in lijst",
    "NOTIN": "waarde komt niet voor in lijst",
    "NOTNA": "waarde is niet NaN of NULL",
    "join_object_exists": "object komt voor in de gerelateerde objecttabel",
    "object_relation": "aggregatiewaarde ophalen uit gerelateerde objecttabel",
    "buffer": "binnen buffer de maaiveldhoogte voor een gegeven percentiel bepalen",
    "compare_longitudinal": "vergelijking van objectwaarden met waarden van een ander object boven- of benedenstroms",
    "no_dangling_node": "hydroobject-eindpunt is verbonden met beginpunt van een ander hydroobject",
    "difference": "verschil tussen linker- en rechterwaarde",
    "multiply": "product van linker- en rechterwaarde",
    "divide": "quotiënt van linker- en rechterwaarde",
    "join_parameter": "koppeling met parameter uit ander objecttabel",
    "sum": "optellen waarden in opgegeven array"
}


def main():
    root_dir = Path(__file__).parent

    output_dir = root_dir / "overzichten_ValidationRules"
    output_dir.mkdir(exist_ok=True)

    json_files = sorted(root_dir.glob("ValidationRules_*.json"), reverse=True)

    md_file = (
        root_dir.parent
        / "docs"
        / "HyDAMO Validatietool"
        / "Introductie tool"
        / "02 Validatieregels.md"
    )

    print(f"{len(json_files)} JSON-bestanden gevonden.")

    markdown_sections = []

    for json_file in json_files:
        print(f"Verwerken: {json_file.name}")

        df = json_to_dataframe(json_file)

        excel_file = output_dir / f"overzicht_{json_file.stem}.xlsx"
        write_excel(df, excel_file, sheet_name=json_file.stem)

        print(f"  -> {excel_file.name}")

        # Voor de documentatie md lange regelnamen opsplitsen met een linebreak
        df["Regelnaam"] = df["Regelnaam"].apply(insert_linebreak_in_rule_name)
        markdown_sections.append(dataframe_to_tab(df, version=json_file.stem.replace( "ValidationRules_", "")))

    update_markdown_page(md_file, "\n\n".join(markdown_sections))
    print("Documentatie-markdown bijgewerkt.")

    print("Klaar.")


def json_to_dataframe(json_file):
    with open(json_file, encoding="utf-8") as f:
        data = json.load(f)

    rows = []

    for obj in data.get("objects", []):

        object_name = obj.get("object", "-")

        #
        # GENERAL RULES
        #
        for rule in obj.get("general_rules", []):

            result_variable = rule.get("result_variable", "-")
            function = rule.get("function", {})
            id = f"{rule.get('id', 0):03d}"

            rows.append(
                {
                    "Object": object_name,
                    "Regeltype": "algemene berekening",
                    "Regelnaam": (f"general_{id}_{result_variable}"),
                    "Toelichting": f"Berekening van '{result_variable}'",
                    "Gewicht": "-",
                    "Objectfilter": "-",
                    "Functietype": format_function_type(function),
                    "Functievariabelen": format_function_variables(function),
                }
            )

        #
        # VALIDATION RULES
        #
        for rule in obj.get("validation_rules", []):

            function = rule.get("function", {})

            regeltype = {
                "logic": "logische validatie",
                "topologic": "topologische validatie",
            }.get(
                rule.get("type"),
                f"{rule.get('type', '')}",
            )

            gewicht = {
                "critical": "kritisch",
                "non-critical": "niet-kritisch",
            }.get(
                rule.get("error_type"),
                "-",
            )

            rows.append(
                {
                    "Object": object_name,
                    "Regeltype": regeltype,
                    "Regelnaam": (
                        f"validate_{rule.get('id', 0):03d}_"
                        f"{rule.get('result_variable', '-')}"
                    ),
                    "Toelichting": rule.get("name", "-"),
                    "Gewicht": gewicht,
                    "Objectfilter": format_filter(
                        rule.get("filter")
                    ),
                    "Functietype": format_function_type(function),
                    "Functievariabelen": format_function_variables(function),
                }
            )

    return pd.DataFrame(
        rows,
        columns=[
            "Object",
            "Regeltype",
            "Regelnaam",
            "Toelichting",
            "Gewicht",
            "Objectfilter",
            "Functietype",
            "Functievariabelen",
        ],
    )


def insert_linebreak_in_rule_name(name):

    if len(name) < 40:
        return name

    parts = name.split("_", 2)

    if len(parts) != 3:
        return name

    return f"{parts[0]}_{parts[1]}_<br>{parts[2]}"


def format_function_type(function):
    if not function:
        return "-"

    function_type = next(iter(function))

    if function_type in FUNCTION_DESCRIPTIONS:
        return (
            f"{function_type} "
            f"({FUNCTION_DESCRIPTIONS[function_type]})"
        )

    return function_type


def format_function_variables(function):
    if not function:
        return "-"

    function_type = next(iter(function))
    variables = function[function_type]

    if not isinstance(variables, dict):
        return str(variables)

    result = []

    for key, value in variables.items():

        if isinstance(value, list):
            value = ", ".join(map(str, value))

        result.append(f"{key}={value}")

    return ", ".join(result)


def format_filter(filter_dict):
    if not filter_dict:
        return "-"

    filter_type = next(iter(filter_dict))
    details = filter_dict[filter_type]

    parameter = details.get("parameter", "")

    result = f"{parameter} {filter_type}"

    if filter_type == "ISIN" or filter_type == "NOTIN":
        opties = ", ".join(
            str(v)
            for v in details.get("array", [])
        )
        result += f" ({opties})"

    return result


def write_excel(df, output_file, sheet_name):
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

        df.to_excel(
            writer,
            sheet_name=sheet_name,
            index=False,
        )

        worksheet = writer.sheets[sheet_name]

        worksheet.auto_filter.ref = worksheet.dimensions
        worksheet.freeze_panes = "A2"

        for column_number, column_name in enumerate(df.columns, start=1):

            content_width = df[column_name].apply(
                lambda value: len(str(value)) if pd.notna(value) else 0
            ).max()

            column_width = max(
                content_width,
                len(str(column_name))
            ) + 2

            column_letter = get_column_letter(column_number)

            worksheet.column_dimensions[
                column_letter
            ].width = column_width


def dataframe_to_tab(df, version):

    if '1.' in version:
        version_modhydamo = version.replace('1.', '2.')
    else:
        version_modhydamo = version

    md_df = df[
        [
            "Object",
            "Regeltype",
            "Regelnaam",
            "Toelichting",
        ]
    ]

    table = md_df.to_markdown(index=False)

    indented_table = "\n".join(
        f"    {line}"
        for line in table.splitlines()
    )

    return (
        f'=== "Versie {version}"\n\n'
        f'    Download hieronder de gekozen versie de validatieregels\n\n'
        f'    - Uitgebreid overzicht van de (inhoudlijke) validatieregels [v{version} als Excel-bestand]'
        f'(https://github.com/HetWaterschapshuis/HyDAMOValidatiehandboek/tree/main/validation_rules/overzichten_ValidationRules)'
        '''{:target="_blank"}\n\n'''
        f'    - De validatieregels [v{version} in JSON-formaat]'
        f'(https://github.com/HetWaterschapshuis/HyDAMOValidatiehandboek/tree/main/validation_rules/ValidationRules_{version}.json?raw=true)'
        '''{:target="_blank"}\n\n'''
        f'    - De syntaxregels in vorm van het [HyDAMO-datamodel {version_modhydamo} in JSON-formaat]'
        f'(https://github.com/HetWaterschapshuis/HyDAMOValidatiehandboek/tree/main/validation_schemas/datamodellen_hydamo/'
        f'HyDAMO_{version_modhydamo}.json?raw=true)'
        '''{:target="_blank"}\n\n'''
        f"{indented_table}\n"
    )


def update_markdown_page(
    markdown_file,
    generated_content,
):

    start_marker = (
        "<!-- VALIDATION_RULE_TABLES_START -->"
    )

    end_marker = (
        "<!-- VALIDATION_RULE_TABLES_END -->"
    )

    text = markdown_file.read_text(
        encoding="utf-8"
    )

    replacement = (
        f"{start_marker}\n"
        "<!-- AUTOMATISCH GEGENEREERD - "
        "NIET HANDMATIG WIJZIGEN -->\n\n"
        f"{generated_content}\n\n"
        f"{end_marker}"
    )

    start_index = text.index(start_marker)
    end_index = text.index(end_marker) + len(end_marker)

    updated_text = (
        text[:start_index]
        + replacement
        + text[end_index:]
    )

    markdown_file.write_text(
        updated_text,
        encoding="utf-8"
    )


if __name__ == "__main__":
    main()