from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Camera(Device):
    """This is a container for information regarding cameras which were used within the dataset.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("cameraINDEX"),
        xml="@id",
    )

    lens: Optional[str] = Field(description="Name of the camera lens", default=None)

    sensor: Optional[str] = Field(
        description="Description of the camera sensor", default=None
    )

    __repo__: Optional[str] = PrivateAttr(default="None")

    __commit__: Optional[str] = PrivateAttr(
        default="4720cfe81270a9ec51f1bb082be79185b982c2b2"
    )
