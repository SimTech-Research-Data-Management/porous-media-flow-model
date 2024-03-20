import sdRDM

from typing import Optional, Union, List, Dict
from pydantic import PrivateAttr, model_validator
from uuid import uuid4
from pydantic_xml import attr, element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from numpy.typing import NDArray
from h5py._hl.dataset import Dataset as H5Dataset
from .processstep import ProcessStep
from .calibration import Calibration
from .software import Software
from .recording import Recording


@forge_signature
class Measurement(sdRDM.DataModel, search_mode="unordered"):
    """*The Measurement encompasses key details about the conducted experiment and its calibration.*"""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    name: str = element(
        description=(
            "Name of the experiment.It should contain all relevant information about"
            " the experiment."
        ),
        tag="name",
        json_schema_extra=dict(),
    )

    calibration: List[Calibration] = element(
        description="Calibration that has been done before the actual experiment.",
        default_factory=ListPlus,
        tag="calibration",
        json_schema_extra=dict(multiple=True),
    )

    recordings: List[Recording] = element(
        description="Recordings that have been done in the course of the experiment.",
        default_factory=ListPlus,
        tag="recordings",
        json_schema_extra=dict(multiple=True),
    )

    processing_steps: List[ProcessStep] = element(
        description="Processing steps and processed video data of the experiment",
        default_factory=ListPlus,
        tag="processing_steps",
        json_schema_extra=dict(multiple=True),
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

    def add_to_calibration(
        self,
        calibration_type: str,
        scale_factor: float,
        camera_position_translation: Optional[float] = None,
        camera_position_rotation: Optional[float] = None,
        calibration_image: Optional[bytes] = None,
        id: Optional[str] = None,
    ) -> Calibration:
        """
        This method adds an object of type 'Calibration' to attribute calibration

        Args:
            id (str): Unique identifier of the 'Calibration' object. Defaults to 'None'.
            calibration_type (): Specify the calibration plate and/or the calibration facility which was used for calibration..
            scale_factor (): Value of the scale factor of the recordings.The amount of pixels corresponding to the length of 1 mm. \\[px/mm].
            camera_position_translation (): Value of the translation of the camera position relative to the calibration plate. \\[m]. Defaults to None
            camera_position_rotation (): Value of the rotation of the camera position relative to the calibration plate. \\[Ã\x83Â\x82Ã\x82Â°]. Defaults to None
            calibration_image (): The actual calibration image which was used.. Defaults to None
        """
        params = {
            "calibration_type": calibration_type,
            "scale_factor": scale_factor,
            "camera_position_translation": camera_position_translation,
            "camera_position_rotation": camera_position_rotation,
            "calibration_image": calibration_image,
        }
        if id is not None:
            params["id"] = id
        self.calibration.append(Calibration(**params))
        return self.calibration[-1]

    def add_to_recordings(
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
        This method adds an object of type 'Recording' to attribute recordings

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
        self.recordings.append(Recording(**params))
        return self.recordings[-1]

    def add_to_processing_steps(
        self,
        name: str,
        operation_list: Optional[Union[NDArray, H5Dataset]] = None,
        processed_recording: List[Recording] = ListPlus(),
        software: List[Software] = ListPlus(),
        id: Optional[str] = None,
    ) -> ProcessStep:
        """
        This method adds an object of type 'ProcessStep' to attribute processing_steps

        Args:
            id (str): Unique identifier of the 'ProcessStep' object. Defaults to 'None'.
            name (): Full name of the processing step..
            operation_list (): List of processing steps carried out with the processing software.. Defaults to None
            processed_recording (): Resulting video after applying the process steps and the raw video.. Defaults to ListPlus()
            software (): Software that has been used to perform the processing steps.. Defaults to ListPlus()
        """
        params = {
            "name": name,
            "operation_list": operation_list,
            "processed_recording": processed_recording,
            "software": software,
        }
        if id is not None:
            params["id"] = id
        self.processing_steps.append(ProcessStep(**params))
        return self.processing_steps[-1]
