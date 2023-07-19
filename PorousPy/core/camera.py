
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .device import Device


@forge_signature
class Camera(Device):
    """It specifies details about the camera lenses and sensors which are used."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cameraINDEX"),
        xml="@id",
    )

    lens: Optional[str] = Field(
        default=None,
        description="Name of the camera lens",
    )

    sensor: Optional[str] = Field(
        default=None,
        description="Description of the camera sensor",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0a1753bd2d9d680e8290be0d84d604b5bccf852b"
    )
