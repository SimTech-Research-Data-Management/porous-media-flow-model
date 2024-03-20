import sdRDM

from typing import Dict, Optional
from pydantic import PrivateAttr, model_validator
from uuid import uuid4
from pydantic_xml import attr, element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict


@forge_signature
class Author(sdRDM.DataModel, search_mode="unordered"):
    """*The Author section provides information about the persons involved in working on or creating the dataset.
    These information helps providing the identity and contact details of the authors associated with the dataset.*
    """

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    name: str = element(
        description="Full name of the author or the experimenter.",
        tag="name",
        json_schema_extra=dict(),
    )

    affiliation: str = element(
        description="Organisation to which the author belongs.",
        tag="affiliation",
        json_schema_extra=dict(),
    )

    email: str = element(
        description="E-Mail adress of the author.",
        tag="email",
        json_schema_extra=dict(),
    )

    phone: Optional[int] = element(
        description="Phone number of the author.",
        default=None,
        tag="phone",
        json_schema_extra=dict(),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model"
    )
    _commit: Optional[str] = PrivateAttr(
        default="07eea00104b98a757878bf718d0cd3baf4ea52d5"
    )
    _raw_xml_data: Dict = PrivateAttr(default_factory=dict)

    @model_validator(mode="after")
    def _parse_raw_xml_data(self):
        for attr, value in self:
            if isinstance(value, (ListPlus, list)) and all(
                (isinstance(i, _Element) for i in value)
            ):
                self._raw_xml_data[attr] = [elem2dict(i) for i in value]
            elif isinstance(value, _Element):
                self._raw_xml_data[attr] = elem2dict(value)
        return self
