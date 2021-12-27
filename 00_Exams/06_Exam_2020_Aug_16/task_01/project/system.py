from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        current_hardware = [hardware for hardware in System._hardware if hardware_name == hardware.name]
        if not current_hardware:
            return "Hardware does not exist"
        current_hardware = current_hardware[0]
        current_express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)

        current_hardware.install(current_express_software)
        System._software.append(current_express_software)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        current_hardware = [hardware for hardware in System._hardware if hardware_name == hardware.name]
        if not current_hardware:
            return "Hardware does not exist"
        current_hardware = current_hardware[0]
        current_light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        current_hardware.install(current_light_software)
        System._software.append(current_light_software)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        current_hardware = [hardware for hardware in System._hardware if hardware_name == hardware.name]
        current_software = [software for software in System._software if software_name == software.name]
        if not (current_hardware or current_software):
            return "Some of the components do not exist"
        current_hardware = current_hardware[0]
        current_software = current_software[0]
        current_hardware.uninstall(current_software)
        System._software.remove(current_software)

    @staticmethod
    def analyze():
        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {sum([software.memory_consumption for software in System._software])} / {sum([hardware.memory for hardware in System._hardware])}\n" \
               f"Total Capacity Taken: {sum([software.capacity_consumption for software in System._software])} / {sum([hardware.capacity for hardware in System._hardware])}"

    @staticmethod
    def system_split():
        hardware_result_data = []
        for hardware in System._hardware:
            software_components_names = "None"
            if hardware.software_components:
                software_components_names = ', '.join([software.name for software in hardware.software_components])
            string_result = f"Hardware Component - {hardware.name}\n" \
                            f"Express Software Components: {len([express_software for express_software in hardware.software_components if isinstance(express_software, ExpressSoftware)])}\n" \
                            f"Light Software Components: {len([light_software for light_software in hardware.software_components if isinstance(light_software, LightSoftware)])}\n" \
                            f"Memory Usage: {sum([software.memory_consumption for software in hardware.software_components])} / {hardware.memory}\n" \
                            f"Capacity Usage: {sum([software.capacity_consumption for software in hardware.software_components])} / {hardware.capacity}\n" \
                            f"Type: {hardware.hardware_type}\n" \
                            f"Software Components: {software_components_names}"
            hardware_result_data.append(string_result)
        return '\n'.join(hardware_result_data)
