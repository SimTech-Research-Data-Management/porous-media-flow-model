import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Software(sdRDM.DataModel):
    """The Software section serves as a container for general information about the software utilized in the experiment.
    It includes details such as the name of the manufacturer, the specific software name, and the version used to generate the dataset.
    These details provide important context for the experiment, allowing for reproducibility and facilitating a clear understanding of the software environment in which the data analysis and processing were performed.
    """

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("softwareINDEX"),
        xml="@id",
    )

    manufacturer: str = Field(
        ...,
        description="Name of the used recording software manufacturer",
    )

    name: str = Field(
        ...,
        description="Name of the used recording software",
    )

    version: str = Field(
        ...,
        description="Version of the used recording software",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="6ceb1857568aa5664c3d40d0d0d5ed03742f2f00"
    )
