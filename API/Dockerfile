From tiangolo/uvicorn-gunicorn-fastapi:python3.8

Run pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "lendingclub.py", "catboost_v1.pkl", "./"]

COPY . .

CMD gunicorn -w 3 -k uvicorn.workers.UvicornWorker predict:app --bind 0.0.0.0:$PORT
