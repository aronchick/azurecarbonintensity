import get_carbon_by_vm.vm_list

def calculate_co2_for_vm(vm_type):
    co2_amount = get_carbon_by_vm.vm_list.list.get(vm_type)
    return co2_amount