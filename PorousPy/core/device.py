import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Device(sdRDM.DataModel):
    """This is a container for information regarding of general devices. For now it only applies to Hardware-optics but it could be for more.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("deviceINDEX"),
        xml="@id",
    )

    manufacturer: str = Field(..., description="Name of the device's manufacturer")

    model: str = Field(..., description="Name of the device's model")

    __repo__: Optional[str] = PrivateAttr(default="None")

    __commit__: Optional[str] = PrivateAttr(
        default="4720cfe81270a9ec51f1bb082be79185b982c2b2"
    )
