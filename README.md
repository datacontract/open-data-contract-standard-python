# Open Data Contract Standard (Python)

The pip module `open-data-contract-standard` to read and write YAML files using the [Open Data Contract Standard](https://github.com/bitol-io/open-data-contract-standard). The pip module was extracted from the [Data Contract CLI](https://github.com/datacontract/datacontract-cli), which is its primary user.

The version number of the pip module corresponds to the version of the Open Data Contract Standard it supports.

## Version Mapping

| Open Data Contract Standard Version | Pip Module Version |
|-------------------------------------|--------------------|
| 3.0.1                               | >=3.0.1            |
| 3.0.2                               | >=3.0.4            |
| 3.1.0                               | >=3.1.0            |

**Note**: We mirror major and minor version from the ODCS to the pip module, but not the patch version!

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
apiVersion: v3.1.0
"""
data_contract = OpenDataContractStandard.from_string(data_contract_str)
# Print the data contract specification as a YAML string
print(data_contract.to_yaml())
```


## Development

```
uv sync --all-extras
```

## Release

- Change version number in `pyproject.toml`
- Run `./release` in your command line
- Wait for the releases on [GitHub](https://github.com/datacontract/open-data-contract-standard-python/releases), [PyPi](https://test.pypi.org/project/open-data-contract-standard/) and [PyPi (test)](https://test.pypi.org/project/open-data-contract-standard/)
