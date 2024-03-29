import sdRDM

from typing import Dict, List, Optional
from pydantic import PrivateAttr, model_validator
from uuid import uuid4
from pydantic_xml import attr, element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict


@forge_signature
class FlowParameters(sdRDM.DataModel, search_mode="unordered"):
    """*The Flow Parameters encompasses crucial details about the flow parameters of the working fluid used in the present dataset.
    These parameters provide a comprehensive understanding of the fluid's properties and flow conditions within the experiment.*
    """

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    fluid: str = element(
        description="Name of the free flow fluid (e.g. dry air, water, ...)",
        tag="fluid",
        json_schema_extra=dict(),
    )

    temperature: float = element(
        description="Value of the fluid temperature at the inlet. \\[K]",
        tag="temperature",
        json_schema_extra=dict(),
    )

    pressure: float = element(
        description="Value of the fluid pressure at the outlet. \\[bar]",
        tag="pressure",
        json_schema_extra=dict(),
    )

    density: float = element(
        description="Value of the fluid density \\[kg/m^3]",
        tag="density",
        json_schema_extra=dict(),
    )

    kinematic_viscosity: float = element(
        description="Value of the fluid kinematic viscosity \\[m^2/s]",
        tag="kinematic_viscosity",
        json_schema_extra=dict(),
    )

    dynamic_viscosity: float = element(
        description="Value of the dynamic fluid viscosity \\[mPas]",
        tag="dynamic_viscosity",
        json_schema_extra=dict(),
    )

    mass_flux: List[float] = element(
        description="Value of the fluid mass flux \\[kg/s]",
        default_factory=ListPlus,
        tag="mass_flux",
        json_schema_extra=dict(multiple=True),
    )

    reynolds_number: List[float] = element(
        description="Value(s) of investigated channel Reynolds number(s). \\[ - ]",
        default_factory=ListPlus,
        tag="reynolds_number",
        json_schema_extra=dict(multiple=True),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model"
    )
    _commit: Optional[str] = PrivateAttr(
        default="07eea00104b98a757878bf718d0cd3baf4ea52d5"
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
