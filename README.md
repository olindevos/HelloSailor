# Project: Strava Sailing Stats (monorepo)
Monorepo 

/ (project-root)  

 ├─ /frontend   

  └─ /backend  

        ├─ app/  

               ├─ init.py   

                └─ main.py   

       ├─ requirements.txt  

        └─ render.yaml  

------------------------------------------------------------------------------------------------------------- 

Backend 

Python 3 
FastAPI 
 

Render (deployment) 

Service type: Web Service 
Language: Python 3 
Build: pip install -r requirements.txt 
Start: uvicorn app.main:app --host 0.0.0.0 --port $PORT 
Live URL: https://<jouw-service>.onrender.com/healthz werkt 
 

Hoe start/stop je alles opnieuw? 

Lokaal — backend 

Terminal openen – naar backend map 
--- cd backend 
Virtuele omgeving activeren: 
--- source .venv/bin/activate 
 

* Als dit faalt, bestaat .venv/ niet (dan heb je ‘m verwijderd of zit je in de verkeerde map). 

 

Server starten: 
--- uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 
 
Check: 
Browser: http://localhost:8000/healthz 
Verwacht: {"status":"ok"} 
Stoppen: 
Terminal: CTRL + C 
Virtualenv uitzetten (optioneel): deactivate 
Cloud — backend (Render) 

Deploy triggert automatisch op git push naar je repo. 
Handmatig redeployen: Render dashboard → jouw service → Manual Deploy. 
Health check: https://<jouw-service>.onrender.com/healthz 
Als build faalt: 

Meest voorkomend: bestand niet gepusht. 
Fix: 
--- git add backend/* 
--- git commit -m "fix: backend files" 
--- git push 
 
Check of root directory in Render op backend staat. 
 

 

Hoe zet je je machine “klaar” na een pauze? 

VS Code openen in project-root. 
Backend: 
--- cd backend 
--- source .venv/bin/activate 
--- uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 
 
→ check http://localhost:8000/healthz 
Frontend : 
--- cd ../frontend 
--- npm run dev 
 
→ http://localhost:3000 

 

Wat je altijd moet doen bij een backend-wijziging 

Commit & push 
--- git add . 
--- git commit -m "beschrijf wat je hebt veranderd" 
--- git push 
 
Redeploy in Render 
Open je service → Manual Deploy → Deploy latest commit 
Test je endpoint 
Bijvoorbeeld: https://<jouw-service>.onrender.com/v1/stats/distance 
 

 

Hoe sluit je alles netjes af 

Wanneer je klaar bent met werken aan je project: 

1. Backend 

1. In je terminal: 

--- CTRL + C 
→ dat stopt de Uvicorn-server (die draait zolang dat proces actief is). 
 
2. Daarna (optioneel): 

--- deactivate 
→ dat sluit je virtuele omgeving (.venv) af. Je ziet dat je prompt verandert van (.venv) naar gewoon bash of zsh. 
* Je hoeft .venv niet te verwijderen. 
Die map mag gewoon blijven staan — hij wordt automatisch weer gebruikt als je later source .venv/bin/activate uitvoert. 

2. Frontend (als je die draait) 

1. In de terminal waarin npm run dev actief is: 

--- CTRL + C 
→ dat stopt de Next.js development server. 
 
3. VS Code en terminal 

Je kunt nu gewoon VS Code afsluiten, of de terminal vensters sluiten. 
Er blijft niks “op de achtergrond” draaien, want zowel Uvicorn als Next.js zijn handmatig gestopt. 

 
 

 

Endpoints 

Healthz  
Roep je aan wanneer je de status van de backend wil weten 

 

Get_total_distance  
mockdata op te testen of ik snap hoe endpoints werken.  
