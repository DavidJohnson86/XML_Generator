import config
from enum import Enum
import json
import abc

class Mandatory(Enum):
    """Contains XML tags what is mandatory for all test cases"""
    VOLTAGE = {config.VOLTAGE_TAG: config.NOMINAL_VOLTAGE}
    WAIT_AFTER_FAULT_FREE = {config.WAIT_AFTER_FAULT_FREE_TAG: config.WAIT_AFTER_FAULT_FREE}
    DIAG_SERVICE = {config.DIAG_SERVICE_TAG : config.DIAG_SERVICE}


class FaultHandlingScenarios(Enum):
    """Enum style class what serves for test case definition"""
    Open = {config.SWITCHING: "Open"}
    Short = {config.SWITCHING: "Short"}
    Leakage_to_GND = {config.SWITCHING: "Leak_GND"}
    Leakage_to_BAT = {config.SWITCHING: "Leak_BAT"}


class AbstractTestGenerator(metaclass=abc.ABCMeta):

    def add_tags(self):
        pass


class TestGenerator(AbstractTestGenerator):
    """This Class is responsible for create JSON format from test datas
    It creates testcases in JSON format that data could be passed to the
    variation generator what creates XML files for test input data"""

    def __init__(self, test_cases, component):
        """
        Initialize variables

        Args:
            test_cases (enum object): Enum Class for test case definition
        """
        self.test_cases = test_cases
        self.component = component
        self.data = {}

    def add_tags(self):
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
            >>> GEN_JSON = TestGenerator(FaultHandlingScenarios)
            >>> GEN_JSON.add_tags(config.squibs)
        """
        for test in self.component:
            for scenario in self.test_cases:
                test_case_name = test + scenario.name
                self.data[test_case_name] = []
                # self.data[test_case_name].append(scenario.value)
                # for param in Mandatory:
                #     self.data[test_case_name].append(param.value)
        return self.data


class TestGeneratorDecorator(AbstractTestGenerator, metaclass=abc.ABCMeta):
    """Decorator Class"""

    def __init__(self, decorated_generator):
        self.decorated_generator = decorated_generator


class MandatoryGenerator(TestGeneratorDecorator):
    """Responsible for adding mandatory fields"""

    def __init__(self, decorated_generator):
        """Initialize variables"""
        super().__init__(decorated_generator)

    def add_tags(self):
        """Receive list and append mandatory fields"""
        test_cases = self.decorated_generator.add_tags()
        for keys, values in enumerate(test_cases):
            for enum in Mandatory:
                test_cases[values].append(enum.value)
        return test_cases


if __name__ == "__main__":
    #print(json.dumps(data, indent=4))
    data = MandatoryGenerator(TestGenerator(FaultHandlingScenarios, config.squibs)).add_tags()
    print(data)


