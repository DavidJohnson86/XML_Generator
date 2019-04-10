"""This module is responsible for generating varition files for Compa 3 airbag tests"""
import abc
import lxml.etree as ET
import lxml.builder
from data_model_generator import TestGenerator, SquibFaultHandling, parse_testcases, TEST_DATA_PATH
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
        """ Init instance variables
        Attributes:
           path (string): Directory name where the script is running
           name (string): Name of the output file
           extension (string): The extension of the output file
        """

        self.path = path
        self.name = name
        self.extension = extension
        self.file_path = self.path + "//" + self.name + self.extension
        self.root = ET.Element(ROOT)
        self.tree = None
        self.element_maker = lxml.builder.ElementMaker()

    def build_structure(self, test_inputs):
        """Build up the xml file"""
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
                for tag, values in sub_element.items():
                    if "=" in tag:
                        tag_name = tag.split(" ")[0]
                        attrib = tag.split(" ")[-1].split("=")[0]
                        value = tag.split("=")[1]
                        test_steps = ET.SubElement(test_cases, tag_name, attrib={attrib: value})
                    else:
                        test_steps = ET.SubElement(test_cases, tag)
                    test_steps.text = values
        self.tree = ET.ElementTree(self.root)
        self.tree.write(self.file_path, pretty_print=True)


if __name__ == "__main__":
    test_inputs = parse_testcases(TEST_DATA_PATH, "squibs")
    test_data = TestGenerator(test_inputs, SquibFaultHandling).add_tags()
    decorated = ConcreteVariation(name="SquibFaultHandlingVar")
    decorated.build_structure(test_data)





