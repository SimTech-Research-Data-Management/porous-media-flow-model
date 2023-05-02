
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .device import Device


@forge_signature
class Camera(Device):

    """This is a container for information regarding cameras which were used within the dataset."""

    id: str = Field(
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
        default="217170c9b861fd33ddc40de1715b3fedae23bbe6"
    )
