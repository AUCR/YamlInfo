"""yamlinfo config tester."""
# coding=utf-8
import unittest
from yaml_info.yamlinfo import YamlInfo


class YamlInfoConfigTest(unittest.TestCase):
    """Unittests automated yamlinfo test case framework."""

    def setUp(self):
        """Set up needed base environment data for unittests."""
        self.project_data = YamlInfo("projectinfo.yml", "projectinfo", "LICENSE").get()

    def test_config_get(self):
        """Test run get function call."""
        self.assertEqual(self.project_data["info"]["name"], "YamlInfo")


if __name__ == '__main__':
    unittest.main(verbosity=2)
