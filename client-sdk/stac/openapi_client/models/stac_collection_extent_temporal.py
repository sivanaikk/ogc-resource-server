# coding: utf-8

"""
    OGC Compliant IUDX Resource Server

    OGC compliant Features and Common API definitions. Includes Schema and Response Objects.

    The version of the OpenAPI document: 1.0.1
    Contact: info@iudx.org.in
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class StacCollectionExtentTemporal(BaseModel):
    """
    The temporal extent of the features in the collection.
    """ # noqa: E501
    interval: Annotated[List[Annotated[List[Optional[datetime]], Field(min_length=2, max_length=2)]], Field(min_length=1)] = Field(description="One or more time intervals that describe the temporal extent of the dataset. The first time interval describes the overall temporal extent of the data. All subsequent time intervals  describe more precise time intervals, e.g., to identify  clusters of data. Clients only interested in the overall extent will only need to access the first item in each array.")
    trs: Optional[StrictStr] = Field(default='http://www.opengis.net/def/uom/ISO-8601/0/Gregorian', description="Coordinate reference system of the coordinates in the temporal extent (property `interval`). The default reference system is the Gregorian calendar. In the Core this is the only supported temporal reference system. Extensions may support additional temporal reference systems and add additional enum values.")
    __properties: ClassVar[List[str]] = ["interval", "trs"]

    @field_validator('trs')
    def trs_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['http://www.opengis.net/def/uom/ISO-8601/0/Gregorian']):
            raise ValueError("must be one of enum values ('http://www.opengis.net/def/uom/ISO-8601/0/Gregorian')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of StacCollectionExtentTemporal from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StacCollectionExtentTemporal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "interval": obj.get("interval"),
            "trs": obj.get("trs") if obj.get("trs") is not None else 'http://www.opengis.net/def/uom/ISO-8601/0/Gregorian'
        })
        return _obj


