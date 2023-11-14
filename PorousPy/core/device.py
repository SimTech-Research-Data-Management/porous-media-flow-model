import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Device(sdRDM.DataModel):
    """The Device provides general information about the manufacturer and model of the used devices such as cameras, lasers, optics, triggering and seeding systems."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("deviceINDEX"),
        xml="@id",
    )

    manufacturer: str = Field(
        ...,
        description="Name of the device's manufacturer",
    )

    model: str = Field(
        ...,
        description="Name of the device's model",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="6ceb1857568aa5664c3d40d0d0d5ed03742f2f00"
    )
