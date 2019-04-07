"""This module is responsible for generating varition files for Compa 3 airbag tests"""
import abc
import lxml.etree as ET
import lxml.builder
from config_matrix_generator import data
from os.path import dirname

ROOT = "DBXML"
TABLE_ELEMENT = "TABLE"
TABLE_ELEMENT_TAG = "Variations"
TEST_CASE_ELEMENT = "RECORD"


class AbstractVariation(metaclass=abc.ABCMeta):
    """Defines the skeleton of the variation file"""
    def __init__(self,
                 path=dirname(__file__),
                 name='variation',
                 extension='.xml'):
        self.path = path
        self.name = name
        self.extension = extension
        self.file_path = self.path + self.name + self.extension
        self.root = ET.Element(ROOT)
        self.tree = None
        self.element_maker = lxml.builder.ElementMaker()

    def build_structure(self, test_inputs):
        """Build up the xml file"""
        pass

    def write(self):
        """Save the file in xml format or else"""
        pass


class ConcreteVariation(AbstractVariation):
    """Implements AbstractVariation Class"""

    def build_structure(self, test_inputs):
        """
        Build up the xml file and write it to file.

        Args:
            test_inputs (json): test data

        """
        table = ET.SubElement(self.root, TABLE_ELEMENT, name=TABLE_ELEMENT_TAG)
        for key, values in test_inputs.items():
            test_cases = ET.SubElement(table, TEST_CASE_ELEMENT, name=key)
            for sub_element in values:
                for key, values in sub_element.items():
                    test_steps = ET.SubElement(test_cases, key)
                    test_steps.text = values
        self.tree = ET.ElementTree(table)
        self.tree.write(self.name, pretty_print=True)


if __name__ == "__main__":
    test_inputs = data
    decorated = ConcreteVariation()
    decorated.build_structure(test_inputs)





