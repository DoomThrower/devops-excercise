FROM python:3.7
EXPOSE 8080 8000
WORKDIR /app

# Dependencies will not change too often, so lets separate that step
RUN pip install pipenv
COPY ./src/Pipfile ./
RUN pipenv install

# Now, lets copy only the source code, which is likely to change often
COPY ./src/*.py ./
CMD pipenv run python ./backend.py
