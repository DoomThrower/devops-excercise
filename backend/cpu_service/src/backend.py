# TODO: There is a high security breach in this code, please, fix it

import json
import os
import random

from bottle import route, run, response

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


# Do not touch this function
def use_cpu_for_a_while():
    """
    This function is used to warm your house for a while
    """
    do_log("DEBUG", "Calculating random numbers...")
    calculated_value = 0
    for i in range(100000):
        calculated_value += random.randint(0, 100)
    return calculated_value


# Do not touch this function
def call_local_program():
    """
    Executes a local program, get its exit status and return it
    """
    do_log("DEBUG", "Calling a local executable...")
    binary = "/app/very_important_value"
    result = os.system(binary)
    do_log("DEBUG", "Finish calling a local executable...")
    return result


################
### Endpoints
################
# TODO: Improve number of requests per second of this endpoint. You can modify
# this code, improve the architecture or both
@route('/cpu')
def cpu():
    do_log("DEBUG", "Calling cpu endpoint")
    # This function must call use_cpu_for_a_while() at least once
    response.content_type = 'application/json'
    return json.dumps(use_cpu_for_a_while())


# TODO: Improve response site of this endpoint. You could improve the local
# program execution (see call_local_program), the architecture or both.
@route('/local_program')
def local_program():
    do_log("DEBUG", "Calling local_program endpoint")
    # This function must call call_local_program() at least once
    response.content_type = 'application/json'
    return json.dumps(call_local_program())
        

do_log("INFO", "Starting server")

# INFO: Starting only one thread to manage all request
run(host='0.0.0.0', port=8080)