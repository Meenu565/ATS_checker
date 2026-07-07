web: uvicorn app.main:app --host 0.0.0.0 --port $PORT --app-dir backend
worker: celery -A app.core.celery_app worker --loglevel=info --workdir backend
