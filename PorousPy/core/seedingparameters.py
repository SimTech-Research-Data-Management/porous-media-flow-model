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
class SeedingParameters(sdRDM.DataModel, search_mode="unordered"):
    """*The Seeding Parameters contains crucial information about the seeding material used in the experiment.
    It includes details such as the material name, particle type, density, particle size and the kinematic viscosity of the seeding particles.
    These parameters provide valuable insights into the characteristics of the seeding material and its influence on the fluid flow behavior within the experimental setup.*
    """

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    material: str = element(
        description="Name of the seeding material.",
        tag="material",
        json_schema_extra=dict(),
    )

    phase: str = element(
        description=(
            "Phase of the seeding material which was used (e.g. solid, liquid, ...)."
        ),
        tag="phase",
        json_schema_extra=dict(),
    )

    density: float = element(
        description="Value of the seeding particle density. \\[kg/m^3]",
        tag="density",
        json_schema_extra=dict(),
    )

    particle_size: float = element(
        description="Value or span of the seeding particle diameter. \\[m]",
        tag="particle_size",
        json_schema_extra=dict(),
    )

    kinematic_viscosity: Optional[float] = element(
        description="Value of the seeding particle kinematic viscosity \\[m^2/s]",
        default=None,
        tag="kinematic_viscosity",
        json_schema_extra=dict(),
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
