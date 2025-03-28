# Open Data Contract Standard (Python)

The pip module `open-data-contract-standard` to read and write YAML files using the [Open Data Contract Standard](https://datacontract.com). The pip module was extracted from the [Data Contract CLI](https://github.com/datacontract/datacontract-cli), which is its primary user.

The version number of the pip module corresponds to the version of the Open Data Contract Standard it supports.

## Version Mapping

| Open Data Contract Standard Version | Pip Module Version |
|-------------------------------------|--------------------|
| 3.0.1                               | 3.0.1              |

Fixes of a specific version are shipped with post released: `3.0.1.post1`, `3.0.1.post2`, etc.

## Installation

```bash
pip install open-data-contract-standard
```

## Usage

```python
from open_data_contract_standard.model import OpenDataContractStandard

# Load a data contract specification from a file
data_contract = OpenDataContractStandard.from_file('path/to/your/data_contract.yaml')
# Print the data contract specification as a YAML string
print(data_contract.to_yaml())
```

```python
from open_data_contract_standard.model import OpenDataContractStandard

# Load a data contract specification from a string
data_contract_str = """
version: 1.0.0
kind: DataContract
id: 53581432-6c55-4ba2-a65f-72344a91553b
status: active
name: my_table
dataProduct: my_quantum
apiVersion: v3.0.1
"""
data_contract = OpenDataContractStandard.from_string(data_contract_str)
# Print the data contract specification as a YAML string
print(data_contract.to_yaml())
```
