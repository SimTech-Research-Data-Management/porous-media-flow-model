import sdRDM

from typing import Dict, Optional
from pydantic import PrivateAttr, model_validator
from uuid import uuid4
from pydantic_xml import attr, element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict


@forge_signature
class PorousMedia(sdRDM.DataModel, search_mode="unordered"):
    """*The Porous Media contains information regarding the parameters associated with the utilized porous media model.
    They include the topology of the porous media model, the dimensions and other relevant material properties.*
    """

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    topology: str = element(
        description="Definition of the porous media model topology.",
        tag="topology",
        json_schema_extra=dict(),
    )

    height: float = element(
        description="Value of the porous media model height. \\[m]",
        tag="height",
        json_schema_extra=dict(),
    )

    width: float = element(
        description="Value of the porous media model width. \\[m]",
        tag="width",
        json_schema_extra=dict(),
    )

    depth: float = element(
        description="Value of the porous media model depth. \\[m]",
        tag="depth",
        json_schema_extra=dict(),
    )

    porosity: float = element(
        description="Value of the porous media model porosity. \\[ - ]",
        tag="porosity",
        json_schema_extra=dict(),
    )

    permeability: Optional[float] = element(
        description="Value of the porous media model permeability. \\[m^2]",
        default=None,
        tag="permeability",
        json_schema_extra=dict(),
    )

    periodicity_x: Optional[float] = element(
        description="Value of the porous media model periodicity in x-direction. \\[m]",
        default=None,
        tag="periodicity_x",
        json_schema_extra=dict(),
    )

    periodicity_y: Optional[float] = element(
        description="Value of the porous media model periodicity in y-direction. \\[m]",
        default=None,
        tag="periodicity_y",
        json_schema_extra=dict(),
    )

    wall_thickness: Optional[float] = element(
        description="Value of the porous media model wall thickness. \\[m]",
        default=None,
        tag="wall_thickness",
        json_schema_extra=dict(),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model"
    )
    _commit: Optional[str] = PrivateAttr(
        default="d9cbe04e5a17a9543e7cb10ad90843d10faaac18"
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
