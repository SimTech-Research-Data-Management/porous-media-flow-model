
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .seedingparameters import SeedingParameters
from .device import Device


@forge_signature
class Seeding(Device):
    """This is a container for information regarding of the seeding device which was used within the dataset."""

    id: Optional[str] = Field(
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
        default="bcd0026275c43b975bd1ffb5d0a0a434786df0e4"
    )
