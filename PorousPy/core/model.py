import sdRDM

from typing import Dict, Optional
from pydantic import PrivateAttr, model_validator
from uuid import uuid4
from pydantic_xml import attr, element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .porousmedia import PorousMedia


@forge_signature
class Model(sdRDM.DataModel, search_mode="unordered"):
    """*The Model section contains information about the location of the object in the flow channel.
    It provides details regarding the type of the present porous media model, its location relative to the free flow and if applicable, detailed parameters related to the model which was used.*
    """

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    type: str = element(
        description=(
            "What kind of object is located inside the flow channel? (porous media"
            " model, cylinder, ...)"
        ),
        tag="type",
        json_schema_extra=dict(),
    )

    location: str = element(
        description=(
            "Where is the object located inside the flow channel? (in, adjascent to,"
            " ... the free flow)"
        ),
        tag="location",
        json_schema_extra=dict(),
    )

    porous_media: Optional[PorousMedia] = element(
        description="Description of porous media parameters",
        default=None,
        tag="porous_media",
        json_schema_extra=dict(),
    )

    cad_model: Optional[bytes] = element(
        description="CAD drawing of the used model (e.g. stored as a '.stl'-File)",
        default=None,
        tag="cad_model",
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
