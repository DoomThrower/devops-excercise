# TODO: this image is executing too many steps every time the code changes
FROM python:3.7
EXPOSE 8080
COPY ./src /app
COPY ./bin/very_important_value /app/very_important_value
RUN pip install pipenv && cd /app && pipenv install
CMD cd /app && pipenv run python ./backend.py