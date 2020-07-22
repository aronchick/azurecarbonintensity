import datetime
from get_carbon_by_vm import webservices
import sys
from pathlib import Path

sys.path.append(str(Path.cwd()))
sys.path.append(str(Path.cwd().parent))

from get_carbon_by_vm.hw_lookup import calculate_co2_for_vm
from get_carbon_by_vm.datacenter import datacenter_multiplier
from get_carbon_by_vm.webservices import co2_load_by_time_and_region

def calculate_co2(vm_type, datacenter_region,  number_of_cores, evaluation_time=datetime.datetime.now()):
    vm_co2 = calculate_co2_for_vm(vm_type)
    dc_multiplier_value = datacenter_multiplier(datacenter_region)
    current_co2_load = co2_load_by_time_and_region(datacenter_region, evaluation_time)
    return vm_co2 * dc_multiplier_value * number_of_cores * current_co2_load