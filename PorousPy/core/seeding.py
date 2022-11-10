from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

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
        description="Seeding parameters of the used seeding material", default=None
    )

    __repo__: Optional[str] = PrivateAttr(default="None")

    __commit__: Optional[str] = PrivateAttr(
        default="4720cfe81270a9ec51f1bb082be79185b982c2b2"
    )
