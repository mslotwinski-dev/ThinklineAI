@echo off
start cmd /k "cd /d ..\apps\client && npm run serve"
start cmd /k "cd /d ..\apps\api && npm run start:dev"
start cmd /k "cd /d ..\apps\ai-core && uvicorn src.app:app --reload --host 0.0.0.0 --port 8000"
