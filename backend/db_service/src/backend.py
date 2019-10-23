import json

from bottle import route, run, request, response
from postgres import Postgres

# Local cache
cache = {}


###############
### Helpers
###############
# Modify this function if you want
def do_log(level, message):
    """
    Log a message with a level
    """
    print(level, message, flush=True)


def get_from_db(name):
    """
    Given a name, return the ages from a database
    """
    db = Postgres("postgres://postgres:backend@db/backend")
    return list(
        map(lambda record: (name, record.age),
            db.all(f"SELECT * FROM name_age WHERE \"name\"='{name}' ")))


def insert_into_db(name, age):
    """
    Given a name and an age, insert into a database
    """
    db = Postgres("postgres://postgres:backend@db/backend")
    db.run(f"INSERT INTO name_age VALUES ('{name}', {age})")


################
### Endpoints
################
@route("/age", method="PUT")
def put_age():
    """
    This endpoint inserts an age given a person name. JSON structure must have
    following interface:
        {
            "name": "A name string",
            "age": number,
        }
    """
    do_log("DEBUG", "Calling put_age endpoint")
    if not request.json:
        response.status = 400
        msg = "This endpoint only accept JSON objects"
        do_log("WARN", msg)
        return msg

    if "name" not in request.json:
        response.status = 400
        msg = f"Received {request.json} but no \"name\" field was found"
        do_log("WARN", msg)
        return msg

    if "age" not in request.json:
        response.status = 400
        msg = f"Received {request.json} but no \"age\" field was found"
        do_log("WARN", msg)
        return msg

    name, age = request.json["name"], int(request.json["age"])

    do_log("INFO", f"Inserting {name} with age {age} into the system")
    # TODO: Imagine you want to have multiple services, local cache with this
    # implementation doesn't have consistency among different instances.
    # Please, fix this issue or explain how are you going to implement a
    # cache with multi-service awareness.
    cache[name] = None
    insert_into_db(name, age)


@route("/age/<name>", method="GET")
def get_age(name):
    do_log("DEBUG", "Calling get_age endpoint")
    # TODO: Imagine you want to have multiple services, local cache with this
    # implementation doesn't have consistency among different instances.
    # Please, fix this issue or explain how are you going to implement a
    # cache with multi-service awareness.
    if name not in cache:
        do_log("DEBUG", f"{name} not in cache")
        cache[name] = get_from_db(name)
        do_log("DEBUG", f"cache[{name}] = {cache[name]}")
    response.content_type = 'application/json'
    return json.dumps(cache[name])
        

do_log("INFO", "Starting server")

# INFO: Starting only one thread to manage all request
run(host='0.0.0.0', port=8080)