import json
import os

import pytest
import yaml

from open_data_contract_standard.model import Context, MapDefinition, OpenDataContractStandard

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures")
UPSTREAM_FULL_EXAMPLE = os.path.join(FIXTURES, "full-example-v3.2.0.odcs.yaml")
ALL_NEW_FIELDS = os.path.join(FIXTURES, "all-new-fields-v3.2.0.odcs.yaml")


def _strip_none(value):
    """Drop None values, which to_yaml() does not emit (exclude_none=True)."""
    if isinstance(value, dict):
        return {k: _strip_none(v) for k, v in value.items() if v is not None}
    if isinstance(value, list):
        return [_strip_none(v) for v in value]
    return value


@pytest.mark.parametrize("fixture", [UPSTREAM_FULL_EXAMPLE, ALL_NEW_FIELDS])
def test_roundtrip_is_lossless(fixture):
    with open(fixture, encoding="utf-8") as file:
        source = yaml.safe_load(file)

    data_contract = OpenDataContractStandard.from_file(fixture)

    assert yaml.safe_load(data_contract.to_yaml()) == _strip_none(source)


def test_new_fields_are_typed():
    data_contract = OpenDataContractStandard.from_file(ALL_NEW_FIELDS)

    assert data_contract.apiVersion == "v3.2.0"
    assert isinstance(data_contract.context, Context)
    assert data_contract.context.instructions
    assert data_contract.context.verifiedStatements[1].answer
    assert data_contract.context.constraints[0].authoritativeDefinitions[0].type == "ontology"
    assert data_contract.customProperties[0].vendor == "acme"

    servers = {s.server: s for s in data_contract.servers}
    assert servers["prod"].port == "${DB_PORT:-5432}"
    assert servers["hana"].port == 30015
    assert servers["lake"].catalogUrl and servers["lake"].namespace
    assert servers["files"].encoding == "ISO-8859-1"
    assert servers["athena"].workgroup == "analytics"

    turnover = data_contract.schema_[0]
    assert turnover.deprecated is False
    assert turnover.synonyms[1].locale == "fr-FR"
    assert isinstance(turnover.context, Context)
    assert turnover.relationships[0].id == "rel-1"
    assert data_contract.schema_[1].context == "Free-text notes, do not aggregate."

    properties = {p.name: p for p in turnover.properties}
    assert properties["total_turnover_euros"].semanticType == "measure"
    assert properties["total_turnover_euros"].synonyms[0].synonym == "TO"
    enum = properties["country_code"].enum
    assert [e.value for e in enum] == ["FR", "DE"]
    assert enum[0].customProperties[0].vendor == "acme"
    assert enum[0].authoritativeDefinitions[0].type == "glossary"
    assert isinstance(properties["attributes"].map, MapDefinition)
    assert properties["attributes"].map.key.logicalType == "string"
    assert properties["attributes"].map.value.properties[0].enum[0].value == "EUR"
    assert properties["embedding"].logicalTypeOptions["dimensions"] == 1536
    assert properties["legacy_flag"].deprecated is True

    sla = data_contract.slaProperties[0]
    assert sla.customProperties[0].vendor == "acme"
    assert sla.authoritativeDefinitions[0].url


def test_port_accepts_variable_reference():
    data_contract = OpenDataContractStandard.from_string(
        """
apiVersion: v3.2.0
kind: DataContract
id: 53581432-6c55-4ba2-a65f-72344a91553b
version: 1.0.0
status: active
servers:
  - server: prod
    type: postgresql
    host: ${DB_HOST}
    port: ${DB_PORT:-5432}
  - server: dev
    type: postgresql
    host: localhost
    port: 5432
"""
    )
    assert data_contract.servers[0].port == "${DB_PORT:-5432}"
    assert data_contract.servers[1].port == 5432
    assert "port: ${DB_PORT:-5432}" in data_contract.to_yaml()


def test_context_shorthand_string():
    data_contract = OpenDataContractStandard.from_string(
        """
apiVersion: v3.2.0
kind: DataContract
id: 53581432-6c55-4ba2-a65f-72344a91553b
version: 1.0.0
status: active
context: Use this contract for revenue analysis only.
schema:
  - name: orders
    context: Always filter by order_date.
"""
    )
    assert data_contract.context == "Use this contract for revenue analysis only."
    assert data_contract.schema_[0].context == "Always filter by order_date."


def test_bundled_json_schema_is_3_2_0():
    schema = json.loads(OpenDataContractStandard.json_schema())
    assert schema["properties"]["apiVersion"]["enum"][0] == "v3.2.0"
    assert "map" in schema["$defs"]["SchemaBaseProperty"]["properties"]["logicalType"]["enum"]
