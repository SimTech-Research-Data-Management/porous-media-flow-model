import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Device(sdRDM.DataModel):

    """This is a container for information regarding of general devices. For now it only applies to "Hardware-optics" but it could be for more."""

    id: str = Field(
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
        default="8f615b63de4ce2ffca03ad205da80541b2f02d45"
    )
