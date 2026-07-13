# HyDAMO Validatiehandboek

Deze repository bevat de MkDocs-documentatie voor het HyDAMO Validatiehandboek.

## Lokale build en preview met uv

1. Installeer uv als dat nog niet aanwezig is:
   - Windows PowerShell: `winget install --id Astral-sh.uv -e`
   - Of via pip: `pip install uv`

2. Maak vanuit de repository-root een virtual environment aan:
   ```powershell
   uv venv
   ```

   Hierdoor wordt een map `.venv` aangemaakt in de root van de repository.

3. Activeer de virtual environment:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

4. Synchroniseer de omgeving met de vereiste packages:
   ```powershell
   uv pip sync requirements.txt
   ```

   Dit zorgt ervoor dat iedereen met dezelfde dependency-versies werkt.

5. Bouw de documentatie:
   ```powershell
   mkdocs build -f mkdocs.yml
   ```

6. Start de lokale preview-server:
   ```powershell
   mkdocs serve -f mkdocs.yml
   ```

   Open daarna de browser op `http://127.0.0.1:8000/`.

### Handige opdrachten

- Bouw zonder de server te starten:
  `mkdocs build -f mkdocs.yml`
- Start de server op een specifieke poort:
  `mkdocs serve -f mkdocs.yml --dev-addr 127.0.0.1:8000`
