from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field

from .device import Device
from .seedingparameters import SeedingParameters


@forge_signature
class Seeding(Device):

    """This is a container for information regarding of the seeding device which was used within the dataset.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("seedingINDEX"),
        xml="@id",
    )
    particles: SeedingParameters = Field(
        description="Seeding parameters of the used seeding material",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0df357be5c077418934ea7ba50004f15e2374916"
    )
