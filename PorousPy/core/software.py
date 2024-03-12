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
class Software(sdRDM.DataModel, search_mode="unordered"):
    """*The Software section serves as a container for general information about the software utilized in the experiment.
    It includes details such as the name of the manufacturer, the specific software name, and the version used to generate the dataset.
    These details provide important context for the experiment, allowing for reproducibility and facilitating a clear understanding of the software environment in which the data analysis and processing were performed.*
    """

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    manufacturer: str = element(
        description="Name of the used recording or processing software manufacturer.",
        tag="manufacturer",
        json_schema_extra=dict(),
    )

    name: str = element(
        description="Name of the used recording or processing software.",
        tag="name",
        json_schema_extra=dict(),
    )

    version: Optional[str] = element(
        description="Version of the used recording or processing software.",
        default=None,
        tag="version",
        json_schema_extra=dict(),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model"
    )
    _commit: Optional[str] = PrivateAttr(
        default="2535a1c6d00880d1546dce3ed835fcc5e3bfb375"
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
