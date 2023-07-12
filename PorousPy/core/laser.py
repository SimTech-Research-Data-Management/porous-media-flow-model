
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .device import Device


@forge_signature
class Laser(Device):
    """This is a container for information regarding lasers which were used within the dataset."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("laserINDEX"),
        xml="@id",
    )

    wavelength: float = Field(
        ...,
        description="Value of the used wavelength",
    )

    type: Optional[str] = Field(
        default=None,
        description="Pulsed or continous wave laser?",
    )

    power: Optional[float] = Field(
        default=None,
        description="value of the laser power",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="bcd0026275c43b975bd1ffb5d0a0a434786df0e4"
    )
