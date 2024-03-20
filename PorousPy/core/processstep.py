import sdRDM

from typing import Dict, List, Optional
from pydantic import PrivateAttr, model_validator
from uuid import uuid4
from pydantic_xml import attr, element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .recording import Recording
from .software import Software


@forge_signature
class ProcessStep(sdRDM.DataModel, search_mode="unordered"):
    """*The Process Step outlines the specific processing steps applied to the flow measurement video data.
    It includes the name of each processing step, the resulting video from the processing, and the software used to post-process the data.
    Additionally, files with the extension ".lvs" from the Davis 10 software can be embedded within this section, providing a comprehensive record of the processing workflow and ensuring the availability of relevant files for reference and replication.*
    """

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    name: str = element(
        description="Full name of the processing step.",
        tag="name",
        json_schema_extra=dict(),
    )

    processed_recording: List[Recording] = element(
        description=(
            "Resulting video after applying the process steps and the raw video."
        ),
        default_factory=ListPlus,
        tag="processed_recording",
        json_schema_extra=dict(multiple=True),
    )

    software: List[Software] = element(
        description="Software that has been used to perform the processing steps.",
        default_factory=ListPlus,
        tag="software",
        json_schema_extra=dict(multiple=True),
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

    def add_to_processed_recording(
        self,
        time: float,
        repetition_rate: float,
        field_of_view: str,
        n_frames: Optional[int] = None,
        frames: Optional[bytes] = None,
        location: Optional[str] = None,
        id: Optional[str] = None,
    ) -> Recording:
        """
        This method adds an object of type 'Recording' to attribute processed_recording

        Args:
            id (str): Unique identifier of the 'Recording' object. Defaults to 'None'.
            time (): Value of the investigated time period. \\[s].
            repetition_rate (): Value of the recording repetition rate. \\[Hz].
            field_of_view (): Value of the field of view. \\[m x m].
            n_frames (): Number of frames found in this video.. Defaults to None
            frames (): The actual Videoframes of the raw video. Defaults to None
            location (): Specify the local filepath to the location of the recordings.. Defaults to None
        """
        params = {
            "time": time,
            "repetition_rate": repetition_rate,
            "field_of_view": field_of_view,
            "n_frames": n_frames,
            "frames": frames,
            "location": location,
        }
        if id is not None:
            params["id"] = id
        self.processed_recording.append(Recording(**params))
        return self.processed_recording[-1]

    def add_to_software(
        self,
        manufacturer: str,
        name: str,
        version: Optional[str] = None,
        id: Optional[str] = None,
    ) -> Software:
        """
        This method adds an object of type 'Software' to attribute software

        Args:
            id (str): Unique identifier of the 'Software' object. Defaults to 'None'.
            manufacturer (): Name of the used recording or processing software manufacturer..
            name (): Name of the used recording or processing software..
            version (): Version of the used recording or processing software.. Defaults to None
        """
        params = {"manufacturer": manufacturer, "name": name, "version": version}
        if id is not None:
            params["id"] = id
        self.software.append(Software(**params))
        return self.software[-1]
