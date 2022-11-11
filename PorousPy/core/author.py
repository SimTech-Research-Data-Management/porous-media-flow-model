import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class Author(sdRDM.DataModel):

    """This is a container for information regarding persons who worked on the dataset or created it.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("authorINDEX"),
        xml="@id",
    )
    name: str = Field(
        ...,
        description="Full name of the author",
    )

    affiliation: str = Field(
        ...,
        description="Organisation the author is affiliated with",
    )

    email: str = Field(
        ...,
        description="Contact e-mail adress of the author",
    )

    phone: Optional[int] = Field(
        description="Contact phone number of the author",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0df357be5c077418934ea7ba50004f15e2374916"
    )
