import json
import config
from enum import Enum


class Scenarios(Enum):
    UNCONFIGURED_NC = "Unconfigured and NOT connected"
    UNCONFIGURED_CO = "Unconfigured and connected"
    UNCONFIGURED_LEAK_GND = "Unconfigured and leakage to GND"
    UNCONFIGURED_LEAK_BAT = "Unconfigured and leakage to BAT"
    INVALID_CONFIG = "Invalid configuration"

class Params(Enum):
    VOLTAGE = {config.VOLTAGE_TAG: config.NOMINAL_VOLTAGE}
    WAIT_AFTER_FAULT_FREE = {config.WAIT_AFTER_FAULT_FREE_TAG: config.WAIT_AFTER_FAULT_FREE}


class ConfigMatrixGenerator:

    def __init__(self):
        self.data = {}

    def define_test_name(self, tests):
        for test in tests:
            for scenario in Scenarios:
                test_case_name = test + scenario.value
                self.data[test_case_name] = []
                for param in Params:
                    self.data[test_case_name].append(param.value)
        return self.data

data = ConfigMatrixGenerator().define_test_name(config.squibs)


# data = {}
# data['ZK1_Sitzairbag_Fahrer_Unconfigured'] = []
# data['ZK1_Sitzairbag_Fahrer_Unconfigured'].append({
#     'PS1.WaitPowerOnMs': '10000',
#     'Fxr3.DefaultConfiguration': '0A,0B,3D,3A,35,37,36,38,3B,20,21,0D,04,06,01,03,10,11,26,27,02,05,18,19,14,15,16,17,22,23,2E,30,2F,31,1C,1D,FF,13,1D,FA,01,02',
#     'Fxr3.BitToConfig': '0',
#     'Fxr3.ByteToConfig': '0'
# })
#
#
# print(data)


