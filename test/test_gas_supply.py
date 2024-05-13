import unittest

from src.gas_supply import check_gas_supply


class TestGasSupply(unittest.TestCase):
    def test_without_connections(self):
        cities = ["a", "b", "c"]
        gas_storages = ["1", "2"]
        pipelines = []
        expected_result = [["1", ["a", "b", "c"]], ["2", ["a", "b", "c"]]]
        result = check_gas_supply(cities, gas_storages, pipelines)
        self.assertEqual(result, expected_result)

    def test_with_all_connections(self):
        cities = ["a", "b", "c"]
        gas_storages = ["1", "2"]
        pipelines = [
            ["1", "a"],
            ["1", "b"],
            ["1", "c"],
            ["2", "a"],
            ["2", "b"],
            ["2", "c"],
        ]
        expected_result = []
        result = check_gas_supply(cities, gas_storages, pipelines)
        self.assertEqual(result, expected_result)

    def test_with_transit(self):
        cities = ["a", "b", "c"]
        gas_storages = ["1", "2"]
        pipelines = [["1", "a"], ["a", "b"], ["b", "c"], ["2", "1"]]
        expected_result = []
        result = check_gas_supply(cities, gas_storages, pipelines)
        self.assertEqual(result, expected_result)

    def test_with_connections_between_cities(self):
        cities = ["a", "b", "c"]
        gas_storages = ["1", "2"]
        pipelines = [["1", "a"], ["a", "b"], ["2", "c"], ["1", "2"]]
        expected_result = [["2", ["a", "b"]]]
        result = check_gas_supply(cities, gas_storages, pipelines)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
