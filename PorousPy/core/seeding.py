
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .device import Device
from .seedingparameters import SeedingParameters


@forge_signature
class Seeding(Device):

    """This is a container for information regarding of the seeding device which was used within the dataset."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("seedingINDEX"),
        xml="@id",
    )

    particles: SeedingParameters = Field(
        ...,
        description="Seeding parameters of the used seeding material",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="7663b173df67fd6098a9e76ea7a354fcf151c549"
    )
