import sys
from pathlib import Path

sys.path.append(str(Path.cwd()))
sys.path.append(str(Path.cwd().parent))

import get_carbon_by_vm.region_list_and_multiplier

def datacenter_multiplier(datacenter_region):
    datacenter_multiplier = get_carbon_by_vm.region_list_and_multiplier.list.get(datacenter_region,None)
    if datacenter_multiplier is None:
        raise ValueError(f"'{datacenter_region}' is not a known datacenter region.")

    return datacenter_multiplier
