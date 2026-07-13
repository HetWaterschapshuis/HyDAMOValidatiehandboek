# HyDAMO Validatiehandboek

Deze repository bevat de MkDocs-documentatie voor het HyDAMO Validatiehandboek.

## Installeer UV

- Windows PowerShell: `winget install --id Astral-sh.uv -e`
- Of via pip: `pip install uv`


## Bouw environment en serve de site
Voer alles in 1x uit via PowerShell met `serve_docs.ps1`, of volg deze instructie:

1. Maak vanuit de repository-root een virtual environment aan:
   ```powershell
   uv venv
   ```

   Hierdoor wordt een map `.venv` aangemaakt in de root van de repository.

2. Activeer de virtual environment:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Synchroniseer de omgeving met de vereiste packages:
   ```powershell
   uv pip sync requirements.txt
   ```

   Dit zorgt ervoor dat iedereen met dezelfde dependency-versies werkt.

4. Bouw de documentatie:
   ```powershell
   mkdocs build -f mkdocs.yml
   ```

5. Start de lokale preview-server:
   ```powershell
   mkdocs serve -f mkdocs.yml
   ```

   Open daarna de browser op `http://127.0.0.1:8000/`.
