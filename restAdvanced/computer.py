class Computer(object):
    
    def __init__(self, name, processorName, ram, disk, version, system, node, machine, cpu_percent):
        
        self.name=name
        self.processorName=processorName
        self.ram=ram
        self.disk=disk
        self.version=version
        self.system=system
        self.node=node
        self.machine=machine
        self.cpu_percent=cpu_percent