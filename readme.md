# HyDAMO Validatiehandboek

Deze repository bevat de MkDocs-documentatie voor het HyDAMO Validatiehandboek.

## Lokale build en preview met uv

1. Installeer uv als dat nog niet aanwezig is:
   - Windows PowerShell: `winget install --id Astral-sh.uv -e`
   - Of via pip: `pip install uv`

2. Maak een lokale Python-omgeving in de repository-root:
   ```powershell
   uv venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Installeer de benodigde packages:
   ```powershell
   uv pip install -r requirements.txt
   ```

4. Bouw de documentatie:
   ```powershell
   mkdocs build -f mkdocs.yml
   ```

5. Start de lokale preview-server:
   ```powershell
   mkdocs serve -f mkdocs.yml
   ```

   Open daarna de browser op `http://127.0.0.1:8000/`.

### Handige opdrachten

- Bouw zonder de server te starten:
  `mkdocs build -f mkdocs.yml`
- Start de server op een specifieke poort:
  `mkdocs serve -f mkdocs.yml --dev-addr 127.0.0.1:8000`
