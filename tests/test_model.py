import yaml

from open_data_contract_standard.model import OpenDataContractStandard


def test_roundtrip():
    data_contract_str = """
version: 1.0.0
kind: DataContract
id: 53581432-6c55-4ba2-a65f-72344a91553b
status: active
name: my_table
dataProduct: my_quantum
apiVersion: v3.1.0
team:
  name: my_team
    """
    assert_equals_yaml(data_contract_str)

def assert_equals_yaml(data_contract_str):
    assert yaml.safe_load(data_contract_str) == yaml.safe_load(OpenDataContractStandard.from_string(data_contract_str).to_yaml())

def test_json_schema():
    assert "" != OpenDataContractStandard.json_schema()