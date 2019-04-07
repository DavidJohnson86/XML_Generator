import config
from enum import Enum
import json


class ConfigMatrixScenarios(Enum):
    """Enum style class what serves for test case definition"""
    UNCONFIGURED_NC = "Unconfigured and NOT connected"
    UNCONFIGURED_CO = "Unconfigured and connected"
    UNCONFIGURED_LEAK_GND = "Unconfigured and leakage to GND"
    UNCONFIGURED_LEAK_BAT = "Unconfigured and leakage to BAT"
    INVALID_CONFIG = "Invalid configuration"


class Mandatory(Enum):
    """Contains XML tags what is mandatory for all test cases"""
    VOLTAGE = {config.VOLTAGE_TAG: config.NOMINAL_VOLTAGE}
    WAIT_AFTER_FAULT_FREE = {config.WAIT_AFTER_FAULT_FREE_TAG: config.WAIT_AFTER_FAULT_FREE}


class JsonGenerator:
    """This Class is responsible for create JSON format from test datas
    It creates testcases in JSON format that data could be passed to the
    variation generator what creates XML files for test input data"""

    def __init__(self, test_cases):
        """
        Initialize variables

        Args:
            test_cases (enum object): Enum Class for test case definition
        """
        self.test_cases = test_cases
        self.data = {}

    def define_test_name(self, component):
        """
        Creates test cases for each component for each scenario defined in test_cases
        and also adds mandatory elements.

        Args:
            component(list): list of components

        Returns:
           list : dictionaries with lists

           {
            "ZK1 Unconfigured and NOT connected": [
                {
                    "PS1.VoltageV": "13.8"
                },
                {
                    "Fxr1.WaitAfterFaultFree": "15000"
                }
            ],
           }

         Example:
            >>> GEN_JSON = JsonGenerator(ConfigMatrixScenarios)
            >>> GEN_JSON.define_test_name(config.squibs)
        """
        for test in component:
            for scenario in self.test_cases:
                test_case_name = test + scenario.value
                self.data[test_case_name] = []
                for param in Mandatory:
                    self.data[test_case_name].append(param.value)
        return self.data


if __name__ == "__main__":
    data = JsonGenerator(ConfigMatrixScenarios).define_test_name(config.squibs)
    print(json.dumps(data, indent=4))


