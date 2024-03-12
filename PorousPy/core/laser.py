
from typing import Dict, Optional
from pydantic import PrivateAttr, model_validator
from uuid import uuid4
from pydantic_xml import attr, element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .device import Device


@forge_signature
class Laser(Device, search_mode="unordered"):
    """*The Laser provides information about the laser wavelength, either the laser is pulsed or continuous as well as the laser power.*"""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    wavelength: float = element(
        description="Value of the used wavelength of the laser. \\[nm]",
        tag="wavelength",
        json_schema_extra=dict(),
    )

    type: Optional[str] = element(
        description=(
            "Type of the used laser (e.g. pulsed or continuous wave laser, ...)"
        ),
        default=None,
        tag="type",
        json_schema_extra=dict(),
    )

    power: Optional[float] = element(
        description="Value of the laser power. \\[W]",
        default=None,
        tag="power",
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
