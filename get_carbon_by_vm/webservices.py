import sys
from pathlib import Path

sys.path.append(str(Path.cwd()))
sys.path.append(str(Path.cwd().parent))

import get_carbon_by_vm.region_list_and_multiplier

def co2_load_by_time_and_region(datacenter_region, evaluation_time):
    datacenter_multiplier = get_carbon_by_vm.region_list_and_multiplier.list.get(datacenter_region,None)
    get_co2_for_region_by_time()

    raise NotImplementedError("NYI")

def get_co2_for_region_by_time(time_to_evaluate):
    # Replace below with actual evaluator (e.g. from watt time)

    # For current: https://api2.watttime.org/v2/index/?latitude=42.372&longitude=72.519&style=all
    #     from urllib2 import Request, urlopen

    # headers = {
    #   'Authorization': 'Bearer <Access_Token>',
    #   'Accept': 'application/zip'
    # }
    # request = Request('https://api2.watttime.org/v2/historical/?ba=&version=', headers=headers)

    # response_body = urlopen(request).read()
    # print response_body


    # For historical: 
    #     
    # from urllib2 import Request, urlopen

    # headers = {
    #   'Authorization': 'Bearer <Access_Token>'
    # }
    # request = Request('https://api2.watttime.org/v2/index/?latitude=&longitude=&style=', headers=headers)

    # response_body = urlopen(request).read()
    # print response_body
    