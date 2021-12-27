class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        if not (software.capacity_consumption <= self.capacity and software.memory_consumption <= self.memory):
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software):
        self.software_components.remove(software)
