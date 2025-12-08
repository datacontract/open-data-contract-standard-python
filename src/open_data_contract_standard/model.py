import importlib.resources as impresources
import os
import typing
from typing import Any

import pydantic as pyd
import yaml


class AuthoritativeDefinition(pyd.BaseModel):
    id: str | None = None
    url: str | None = None
    type: str | None = None
    description: str | None = None


class CustomProperty(pyd.BaseModel):
    id: str | None = None
    property: str | None = None
    value: Any | None = None
    description: str | None = None


class Support(pyd.BaseModel):
    id: str | None = None
    channel: str | None = None
    url: str | None = None
    description: str | None = None
    tool: str | None = None
    scope: str | None = None
    invitationUrl: str | None = None
    customProperties: list[CustomProperty] | None = None


class Pricing(pyd.BaseModel):
    id: str | None = None
    priceAmount: float | int | None = None
    priceCurrency: str | None = None
    priceUnit: str | None = None


class TeamMember(pyd.BaseModel):
    id: str | None = None
    username: str | None = None
    name: str | None = None
    description: str | None = None
    role: str | None = None
    dateIn: str | None = None
    dateOut: str | None = None
    replacedByUsername: str | None = None
    tags: list[str] | None = None
    customProperties: list[CustomProperty] | None = None
    authoritativeDefinitions: list[AuthoritativeDefinition] | None = None


class Team(pyd.BaseModel):
    id: str | None = None
    name: str | None = None
    description: str | None = None
    members: list[TeamMember] | None = None
    tags: list[str] | None = None
    customProperties: list[CustomProperty] | None = None
    authoritativeDefinitions: list[AuthoritativeDefinition] | None = None



class ServiceLevelAgreementProperty(pyd.BaseModel):
    id: str | None = None
    property: str | None = None
    value: str | float | int | bool | None = None
    valueExt: str | float | int | bool | None = None
    unit: str | None = None
    element: str | None = None
    driver: str | None = None
    description: str | None = None
    scheduler: str | None = None
    schedule: str | None = None


class DataQuality(pyd.BaseModel):
    id: str | None = None
    authoritativeDefinitions: list[AuthoritativeDefinition] | None = None
    businessImpact: str | None = None
    customProperties: list[CustomProperty] | None = None
    description: str | None = None
    dimension: str | None = None
    method: str | None = None
    name: str | None = None
    schedule: str | None = None
    scheduler: str | None = None
    severity: str | None = None
    tags: list[str] | None = None
    type: str | None = None
    unit: str | None = None
    metric: str | None = None
    rule: str | None = None  # Deprecated: Use metric instead
    arguments: dict[str, Any] | None = None
    mustBe: Any | None = None
    mustNotBe: Any | None = None
    mustBeGreaterThan: float | int | None = None
    mustBeGreaterOrEqualTo: float | int | None = None
    mustBeLessThan: float | int | None = None
    mustBeLessOrEqualTo: float | int | None = None
    mustBeBetween: list[float | int] | None = pyd.Field(None, max_length=2, min_length=2)
    mustNotBeBetween: list[float | int] | None = pyd.Field(None, max_length=2, min_length=2)
    query: str | None = None
    engine: str | None = None
    implementation: str | dict[str, Any] | None = None

class Description(pyd.BaseModel):
    usage: str | None = None
    purpose: str | None = None
    limitations: str | None = None
    authoritativeDefinitions: list[AuthoritativeDefinition] | None = None
    customProperties: list[CustomProperty] | None = None


class Relationship(pyd.BaseModel):
    type: str | None
    from_: str | list[str] | None = pyd.Field(default=None, alias="from")
    to: str | list[str] | None = None
    customProperties: list[CustomProperty] | None = None


class SchemaProperty(pyd.BaseModel):
    id: str | None = None
    name: str | None = None
    physicalType: str | None = None
    physicalName: str | None = None
    description: str | None = None
    businessName: str | None = None
    authoritativeDefinitions: list[AuthoritativeDefinition] | None = None
    tags: list[str] | None = None
    customProperties: list[CustomProperty] | None = None
    primaryKey: bool | None = None
    primaryKeyPosition: int | None = None
    logicalType: str | None = None
    logicalTypeOptions: dict[str, Any] | None = None
    required: bool | None = None
    unique: bool | None = None
    partitioned: bool | None = None
    partitionKeyPosition: int | None = None
    classification: str | None = None
    encryptedName: str | None = None
    transformSourceObjects: list[str] | None = None
    transformLogic: str | None = None
    transformDescription: str | None = None
    examples: list[Any] | None = None
    criticalDataElement: bool | None = None
    relationships: list[Relationship] | None = None
    quality: list[DataQuality] | None = None
    properties: list["SchemaProperty"] | None = None
    items: typing.Optional["SchemaProperty"] = None


class SchemaObject(pyd.BaseModel):
    id: str | None = None
    name: str | None = None
    physicalType: str | None = None
    description: str | None = None
    businessName: str | None = None
    authoritativeDefinitions: list[AuthoritativeDefinition] | None = None
    tags: list[str] | None = None
    customProperties: list[CustomProperty] | None = None
    logicalType: str | None = None
    physicalName: str | None = None
    dataGranularityDescription: str | None = None
    properties: list[SchemaProperty] | None = None
    relationships: list[Relationship] | None = None
    quality: list[DataQuality] | None = None


class Role(pyd.BaseModel):
    id: str | None = None
    role: str | None = None
    description: str | None = None
    access: str | None = None
    firstLevelApprovers: str | None = None
    secondLevelApprovers: str | None = None
    customProperties: list[CustomProperty] | None = None


class Server(pyd.BaseModel):
    id: str | None = None
    server: str | None = None
    type: str | None = None
    description: str | None = None
    environment: str | None = None
    roles: list[Role] | None = None
    customProperties: list[CustomProperty] | None = None

    account: str | None = None
    catalog: str | None = None
    database: str | None = None
    dataset: str | None = None
    delimiter: str | None = None
    endpointUrl: str | None = None
    format: str | None = None
    host: str | None = None
    location: str | None = None
    path: str | None = None
    port: int | None = None
    project: str | None = None
    region: str | None = None
    regionName: str | None = None
    schema_: str | None = pyd.Field(default=None, alias="schema")
    serviceName: str | None = None
    stagingDir: str | None = None
    stream: str | None = None
    warehouse: str | None = None



class OpenDataContractStandard(pyd.BaseModel):
    model_config = pyd.ConfigDict(
        extra='forbid',
    )
    version: str | None = None
    kind: str | None = None
    apiVersion: str | None = None
    id: str | None = None
    name: str | None = None
    tenant: str | None = None
    tags: list[str] | None = None
    status: str | None = None
    servers: list[Server] | None = None
    dataProduct: str | None = None
    description: Description | None = None
    domain: str | None = None
    schema_: list[SchemaObject] | None = pyd.Field(default=None, alias="schema")
    support: list[Support] | None = None
    price: Pricing | None = None
    team: Team | list[TeamMember] | None = None
    roles: list[Role] | None = None
    slaDefaultElement: str | None = None
    slaProperties: list[ServiceLevelAgreementProperty] | None = None
    authoritativeDefinitions: list[AuthoritativeDefinition] | None = None
    customProperties: list[CustomProperty] | None = None
    contractCreatedTs: str | None = None

    def to_yaml(self) -> str:
        return yaml.dump(
            self.model_dump(exclude_defaults=True, exclude_none=True,
                            by_alias=True),
            sort_keys=False,
            allow_unicode=True,
        )

    @classmethod
    def from_file(cls, file_path: str) -> "OpenDataContractStandard":
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        with open(file_path, "r", encoding="utf-8") as file:
            file_content = file.read()
        return cls.from_string(file_content)

    @classmethod
    def from_string(cls, data_contract_str: str) -> "OpenDataContractStandard":
        data = yaml.safe_load(data_contract_str)
        return cls(**data)

    @classmethod
    def json_schema(cls):
        package_name = __package__
        json_schema = "schema.json"
        with impresources.open_text(package_name,
                                    json_schema) as file:
            return file.read()
