#  LB Modul 324 (DevOps)

Dieses Projekt wurde im Rahmen der Leistungsbeurteilung **LB 324 – DevOps** an der BBBaden umgesetzt.  
Es handelt sich um eine kleine Tagebuch-App mit Login, die über **GitHub Actions** getestet und automatisch auf **Azure App Service** deployed wird.

🌍 Live-Version:  
👉 [Zur Anwendung](https://nael-ackle-lb324-b4bdegceged2b0ht.spaincentral-01.azurewebsites.net/)

---

## 🎯 Zielsetzung
- Aufbau eines vollständigen **DevOps-Workflows**:
  - GitHub Flow (Branches, Issues, Pull Requests)
  - Qualitätssicherung mit **pre-commit** & **pytest**
  - Automatisierte Tests & Deployment mit **GitHub Actions**
- Entwicklung einer **neuen Funktion**: Einträge mit Happiness-Wert (😃/😐/😢).

---

## 🛠️ Technologien
- **Python 3.11**, **Flask**
- **gunicorn** (Produktionsserver)
- **python-dotenv** (Umgebungsvariablen)
- **pytest** (Tests)
- **pre-commit** (Code-Qualität)
- **GitHub Actions** (CI/CD)
- **Azure Web App** (Linux)

---

## ⚙️ Einrichtung & Lokaler Start

1. Repository klonen:
   ```bash
   git clone https://github.com/<user>/<repo>.git
   cd <repo>
   ```

2. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

3. `.env`-Datei erstellen:
   ```env
   PASSWORD="DeinPasswort"
   ```

4. pre-commit einrichten:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

5. App starten:
   ```bash
   flask run
   ```
   → erreichbar unter [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## ✨ Neue Funktion
- Jeder Tagebuch-Eintrag kann mit einem **Happiness-Wert** versehen werden.  
- Diese Funktion wird durch automatische Tests überprüft.

---

## 🏆 Fazit
Mit dieser Arbeit wurde ein kompletter **CI/CD-Workflow** aufgesetzt:  
Von der Versionsverwaltung über automatisierte Tests bis zum Deployment in Azure.



<img width="1920" height="1080" alt="Screenshot 2025-09-22 221406" src="https://github.com/user-attachments/assets/0c35bd91-6999-4312-93c9-2ce7d9515434" />
<img width="1920" height="1080" alt="Screenshot 2025-09-22 094719" src="https://github.com/user-attachments/assets/6fc402ea-7bfb-409c-9cdc-1b0a65cc551a" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4f93f577-2a4b-421c-a477-e8cfef77d4b5" />
<img width="1920" height="1080" alt="Screenshot 2025-09-22 231004" src="https://github.com/user-attachments/assets/24c400b9-f785-44c6-831f-884bc9cf4bc3" />
