#test deploy local
 mkdir -p static media staticfiles
python manage.py collectstatic --no-input
python -m gunicorn mykala.asgi:application -k uvicorn.workers.UvicornWorker