# Project: Strava Sailing Stats (monorepo)
Hello Sailor – Project Documentation 

Introduction 

Hello Sailor is a personal project that retrieves data from the Strava API to display the total distance 

sailed. It uses React (TypeScript) for the frontend, FastAPI (Python) for the backend, and hosts 

them on Vercel and Render respectively. 

 

Architecture 

This project is structured as a monorepo with two main directories: - **frontend/** – Next.js + 

TypeScript app for the user interface. - **backend/** – FastAPI + Python app that communicates with Strava and exposes endpoints. Hosting: - Frontend → Vercel - Backend → Render 

 

Technology Stack 

Frontend: React, Next.js, TypeScript  

Backend: FastAPI, Python, Requests  

Hosting: Vercel (frontend), Render (backend) - **API:** Strava REST API 

 

 

 

 

Setup Instructions 

1. Clone the repository.  

2. Navigate to `backend/` and create a virtual environment: ```bash python-m venv .venv source .venv/bin/activate ```  

3. Install dependencies: ```bash pip install -requirements.txt ```  

4. Run the backend locally: ```bash uvicorn app.main:app --reload ```  

5. In another terminal, navigate to `frontend/` and start the Next.js dev server: ```bash npm run dev ``` 

 

Environment Variables 

The backend requires the following environment variables  

(either via Render or a local `.env` file): 

STRAVA_CLIENT_ID= xxxxx 

STRAVA_CLIENT_SECRET= xxxxx 

STRAVA_REFRESH_TOKEN= xxxxx 

 

API Endpoints 

Endpoint 		| 	Method 	| 	Description  

`/healthz` 		| 	GET 		| 	Backend health check 

 `/v1/stats/distance`	| 	GET 		| 	Returns total sailing distance (mock or 			|			|	live) 

`/oauth/callback`	| 	GET 		| 	Receives the authorization code from 			|			|	Strava  

`/v1/strava/ping` 	| 	GET 		| 	Tests connection with Strava and returns 							 athlete info  

Deployment 

Backend (Render) -  

Root Directory: `backend` - Start Command:  

`uvicorn app.main:app –host 0.0.0.0 --port $PORT`  

- Manual Deploy after every commit.  

 

Frontend (Vercel) - Framework: 

Next.js - Environment Variable: `NEXT_PUBLIC_API_URL=https://.onrender.com` 

 

Development Workflow 

1. Make backend changes → commit and push.  

2. Manually redeploy on Render.  

3. Test locally on `/healthz` and `/v1/strava/ping`.  

4. For frontend → commit, push, and deploy via Vercel.  

5. Always stop the virtual environment with `deactivate` after work. 

 

Future Improvements 

- Replace mock distance data with live Strava data. - Add activity type filters (e.g., Sailing only). - 

Add a visual dashboard for progress tracking. - Implement auto-refresh for daily data updates. 

 

Author & License 

Created by Olin as a personal learning and performance project. License: None 
