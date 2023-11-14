
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .device import Device


@forge_signature
class Laser(Device):
    """The Laser provides information about the laser wavelength, either the laser is pulsed or continous and the laser power."""

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
        default="6ceb1857568aa5664c3d40d0d0d5ed03742f2f00"
    )
