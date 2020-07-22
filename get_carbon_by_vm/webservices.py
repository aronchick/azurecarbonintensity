from random import randrange
import sys
from pathlib import Path

import logging
import os
import azure.functions as func
    
sys.path.append(str(Path.cwd()))
sys.path.append(str(Path.cwd().parent))

import get_carbon_by_vm.region_list_and_multiplier
from get_carbon_by_vm.watttime_api import login, index

import yaml as YAML

def co2_per_watt_by_time_and_region(datacenter_region, evaluation_time):
    datacenter_multiplier = get_carbon_by_vm.region_list_and_multiplier.list.get(datacenter_region,None)
    carbon_dict = get_co2_for_region_by_time(datacenter_region, evaluation_time)

    # TODO: Remove mockup value below
    # Get maximum CO2 by region for non-renewable
    # max_co2 = get_maximum_co2_by_region(datacenter_region)
    max_co2 = 1500

    percent_renewable = carbon_dict['percent']

    co2_per_watt = max_co2 * float(percent_renewable) / 100
    return co2_per_watt

def get_co2_for_region_by_time(region, time_to_evaluate):
    """ Returns a % of how clean the region is.
    
    Though it takes 'time_to_evaluate' and 'region', neither is currently used (just mocking up for region='CAISO_ZP26' and time=now)
    """ 
    # TODO: Support other times (e.g. for forecasting)

    # Replace below with production evaluator (e.g. from watt time)
    # https://github.com/WattTime/apiv2-example/blob/master/query_apiv2.py

    username = os.environ["watttime_USERNAME"]
    password = os.environ["watttime_PASSWORD"]

    wt_token = login(username, password)

    # TODO: Map from Azure region to BA region (a WattTime Concept)
    BA = 'CAISO_ZP26'  # identify grid region

    carbon_dict = index(wt_token, BA)

    return carbon_dict


    # "watttime_information": {
    #   "USERNAME": "aronchick@gmail.com",
    #   "PASSWORD": "73ad35ddc87843458a5a691f3d72dc5e",
    #   "EMAIL": "aronchick@gmail.com",
    #   "ORG": "None"
    # }
