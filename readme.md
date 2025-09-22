# 📓 Tagebuch-Applikation – Leistungsbeurteilung LB 324 (DevOps)

Dieses Repository enthält die Umsetzung der Leistungsbeurteilung im Modul **324 – DevOps** an der BBBaden.  
Ziel war es, eine kleine Tagebuch-Applikation mit Python/Flask zu entwickeln und diese über **GitHub Actions** automatisiert zu testen und via **Azure App Service** zu deployen.

---

## 🎯 Zielsetzung

- Aufbau eines vollständigen **DevOps-Workflows** für eine Webapplikation:
  - **Versionsverwaltung** mit GitHub
  - **GitHub Flow** mit Issues, Branches, Pull Requests
  - **Labels & Templates** für Anforderungen
  - **Pre-Commit Hooks** für Qualitätssicherung
  - **Automatisierte Tests** mit pytest
  - **CI/CD-Pipeline** mit GitHub Actions
  - **Deployment** auf Azure
- Implementierung einer **neuen Funktion** (HZ5): *Einträge mit Happiness-Wert*.

---

## 🛠️ Technologien

- **Python 3.11**
- **Flask** (Webframework)
- **gunicorn** (Produktionsserver)
- **python-dotenv** (Umgebungsvariablen)
- **pytest** (Tests)
- **pre-commit** (Code-Qualität)
- **GitHub Actions** (CI/CD)
- **Azure Web App (Linux, Python 3.11)**

---

## ⚙️ Einrichtung & Lokaler Start

1. Repository klonen:
   ```bash
   git clone https://github.com/<user>/<repo>.git
   cd <repo>
Abhängigkeiten installieren:

bash
Code kopieren
pip install -r requirements.txt
.env-Datei anlegen:

env
Code kopieren
PASSWORD="MeinGitHubName"
pre-commit installieren:

bash
Code kopieren
pip install pre-commit
pre-commit install
App starten:

bash
Code kopieren
flask run
→ erreichbar unter http://127.0.0.1:5000

🔐 Login
Zugriff auf das Tagebuch ist nur nach Login möglich.

Passwort wird aus .env geladen (lokal) bzw. in Azure als Application Setting hinterlegt.

🧪 Pre-Commit Hooks
Dieses Projekt nutzt pre-commit, um die Qualität des Codes sicherzustellen.

Installation

bash
Code kopieren
pip install pre-commit
pre-commit install
Regeln

Bei jedem Commit wird der Code automatisch geprüft.

Bei jedem Push werden Tests (pytest) ausgeführt.

Manuell ausführen

bash
Code kopieren
pre-commit run --all-files
🔀 GitHub Flow & Projektstruktur
Branches:

main → Release & Deployment

dev → Integrations-Branch

feature/* → neue Features (z. B. feature/add-happiness-entry)

Issues:

mit Templates (bug_report.yml, feature_request.yml, hz_task.yml)

enthalten User Stories + Akzeptanzkriterien

Labels:

funktionale Anforderung

Qualitätsanforderung

Randanforderung

HZ1 … HZ5

Pull Requests:

feature/* → dev (Tests laufen automatisch)

dev → main (Deployment auf Azure)

⚙️ CI/CD-Pipeline
Datei: .github/workflows/azure.yml

PR auf dev:

Build & Test (pytest)

kein Deployment

Push/Merge auf main:

Build & Test

Deployment auf Azure

Secrets (GitHub):

AZURE_WEBAPP_NAME → Name der Web App (z. B. nael-tagebuch-324)

AZURE_WEBAPP_PUBLISH_PROFILE → XML-Inhalt aus Azure „Publish Profile“

🌐 Deployment auf Azure
Azure Web App: Linux, Python 3.11

Konfiguration:

Application Settings:

ini
Code kopieren
PASSWORD=<GitHub-Name>
SCM_DO_BUILD_DURING_DEPLOYMENT=1
Startup-Command:

bash
Code kopieren
gunicorn --bind=0.0.0.0 --timeout 600 app:app
Automatisches Deployment bei jedem Merge in main

Live-URL:
👉 https://nael-tagebuch-324.azurewebsites.net

✨ Neue Funktion: Happiness-Einträge
Beim Erstellen eines Eintrags kann zusätzlich ein Happiness-Wert (😃/😐/😢) angegeben werden.

Einträge werden mit Zeitstempel und Happiness gespeichert.

Akzeptanzkriterien (HZ5):

POST /add_entry akzeptiert content + happiness

Response = 302 Redirect → /

Eintrag wird in entries[0] gespeichert

entry.content == "Test Entry Content"

entry.happiness == "😃"

Automatischer Test:
test_add_entry_with_happiness prüft diese Kriterien erfolgreich.

✅ Erfüllte Handlungsziele
HZ	Ziel	Umsetzung
HZ1	Anforderungen ermitteln & dokumentieren	Issues mit User Stories, Akzeptanzkriterien
HZ2	Anforderungen mit Labels & Templates verwalten	Labels (funktional, Qualität, Rand), Templates hz_task.yml
HZ3	Sourcecode & Artefakte versionieren	GitHub Repo, GitHub Flow, Branches
HZ4	CI einrichten (Build & Test)	GitHub Actions Workflow prüft PRs auf dev
HZ5	CD einrichten (Deployment)	Automatisches Deploy nach Azure bei Merge auf main

📋 Akzeptanzkriterien & Testfälle
Beispiel: HZ5 – Happiness-Eintrag

User Story:
Als Benutzer möchte ich beim Erstellen eines Eintrags zusätzlich eine Happiness-Angabe speichern,
damit ich meine Stimmung im Tagebuch nachvollziehen kann.

Akzeptanzkriterien:

POST /add_entry akzeptiert content + happiness

Response = 302 Redirect → /

Eintrag wird gespeichert in entries[0]

entry.content == "Test Entry Content"

entry.happiness == "😃"

Automatischer Test (pytest):
Wird in der Pipeline ausgeführt und läuft grün (test_add_entry_with_happiness).

📸 Screenshots / Nachweise
Screenshots befinden sich im Ordner /docs:

Labels & Issue-Board

Beispiel-Issue mit Akzeptanzkriterien

Pull Request mit grünem Test-Check

GitHub Actions Log (Build + Deploy)

Azure-Konfiguration (App Settings, Startup Command)

Live-Anwendung im Browser

📚 Quellen
Unterrichtsmaterial Modul 324 (BBBaden)

pre-commit

pytest

Azure Web Apps

GitHub Actions Marketplace: azure/webapps-deploy

🏆 Fazit
Mit dieser Arbeit wurde ein vollständiger DevOps-Workflow umgesetzt:
Von der Anforderungserhebung über Versionsverwaltung und Qualitätssicherung bis hin zu automatisiertem Build, Test und Deployment.

Die neue Funktion (Happiness-Einträge) ist implementiert und getestet.
Damit sind alle Handlungsziele HZ1–HZ5 erfüllt.


<img width="1920" height="1080" alt="Screenshot 2025-09-22 221406" src="https://github.com/user-attachments/assets/0c35bd91-6999-4312-93c9-2ce7d9515434" />
<img width="1920" height="1080" alt="Screenshot 2025-09-22 094719" src="https://github.com/user-attachments/assets/6fc402ea-7bfb-409c-9cdc-1b0a65cc551a" />
<img width="1920" height="1080" alt="Screenshot 2025-09-22 231004" src="https://github.com/user-attachments/assets/24c400b9-f785-44c6-831f-884bc9cf4bc3" />
