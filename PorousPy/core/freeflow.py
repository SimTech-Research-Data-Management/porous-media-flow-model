import sdRDM

from typing import Dict, Optional
from pydantic import PrivateAttr, model_validator
from uuid import uuid4
from pydantic_xml import attr, element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .flowparameters import FlowParameters


@forge_signature
class FreeFlow(sdRDM.DataModel, search_mode="unordered"):
    """*The Free Flow section contains information about the shape, dimensions, and working fluid of the free flow channel.
    It provides details such as the shape of the flow channel's cross-section, the hydraulic diameter, height, width and depth of the channel and a description of the flow parameters of the working fluid.*
    """

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    shape: str = element(
        description=(
            "Shape of the flow channel's cross section (e.g. rectangular, round, ...)"
        ),
        tag="shape",
        json_schema_extra=dict(),
    )

    hydraulic_diameter: float = element(
        description="Value of the channel's hydraulic diameter. \\[m]",
        tag="hydraulic_diameter",
        json_schema_extra=dict(),
    )

    height: Optional[float] = element(
        description=(
            "Value of the channel height, assuming a rectangular channel. \\[m]"
        ),
        default=None,
        tag="height",
        json_schema_extra=dict(),
    )

    width: Optional[float] = element(
        description=(
            "Value of the flow channel width, assuming a rectangular channel. \\[m]"
        ),
        default=None,
        tag="width",
        json_schema_extra=dict(),
    )

    depth: Optional[float] = element(
        description=(
            "Value of the flow channel depth, assuming a rectangular channel. \\[m]"
        ),
        default=None,
        tag="depth",
        json_schema_extra=dict(),
    )

    diameter: Optional[float] = element(
        description=(
            "Value of the flow channel diameter, assuming a round channel. \\[m]"
        ),
        default=None,
        tag="diameter",
        json_schema_extra=dict(),
    )

    fluid: FlowParameters = element(
        description="Description of the free flow parameters during the dataset.",
        tag="fluid",
        json_schema_extra=dict(),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model"
    )
    _commit: Optional[str] = PrivateAttr(
        default="2535a1c6d00880d1546dce3ed835fcc5e3bfb375"
    )
    _raw_xml_data: Dict = PrivateAttr(default_factory=dict)

    @model_validator(mode="after")
    def _parse_raw_xml_data(self):
        for attr, value in self:
            if isinstance(value, (ListPlus, list)) and all(
                (isinstance(i, _Element) for i in value)
            ):
                self._raw_xml_data[attr] = [elem2dict(i) for i in value]
            elif isinstance(value, _Element):
                self._raw_xml_data[attr] = elem2dict(value)
        return self
