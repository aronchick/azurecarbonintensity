import logging

import azure.functions as func
import datetime
import os
import sys
from pathlib import Path

sys.path.append(str(Path.cwd()))
sys.path.append(str(Path.cwd().parent))

from get_carbon_by_vm.calculator import calculate_co2

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    vmfamily = None
    region = None
    cores = None
    gpus = None
    time_to_schedule = None
    req_body = None

    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        vmfamily = req_body.get('vmfamily')
        region = req_body.get('region')
        cores = req_body.get('cores')
        gpus = req_body.get('gpus')

        time_to_schedule = req_body.get('time_to_schedule')
        if time_to_schedule is None:
            time_to_schedule = datetime.datetime.now()

    if req_body is not None:
        total_co2 = calculate_co2(vmfamily, region,  cores)
        return func.HttpResponse(f"Hello, This HTTP triggered function executed successfully, and has the following information: {total_co2}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully, but there was no json body. Please pass in a json body",
             status_code=200
        )
