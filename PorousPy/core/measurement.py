import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from h5py._hl.dataset import Dataset as H5Dataset
from numpy.typing import NDArray
from pydantic import Field
from pydantic import validator
from pydantic.types import PositiveInt
from typing import List
from typing import Optional
from typing import Union

from .processstep import ProcessStep
from .recording import Recording
from .software import Software


@forge_signature
class Measurement(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("measurementINDEX"),
        xml="@id",
    )
    name: str = Field(
        ...,
        description="Name of the experiment",
    )

    recordings: List[Recording] = Field(
        description="Recordings that have been done in the course of the experiment",
        default_factory=ListPlus,
    )

    processing_steps: List[ProcessStep] = Field(
        description="Processed video data of the flow measurement",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0df357be5c077418934ea7ba50004f15e2374916"
    )

    def add_to_recordings(
        self,
        camera_id: Union[str, "Camera"],
        time: float,
        repetition_rate: float,
        field_of_view: str,
        height: Optional[PositiveInt] = None,
        width: Optional[PositiveInt] = None,
        n_frames: Optional[int] = None,
        frames: Union[NDArray, H5Dataset, None] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Recording' to the attribute 'recordings'.

        Args:
            id (str): Unique identifier of the 'Recording' object. Defaults to 'None'.
            camera_id (Union[str, 'Camera']): ID of the camera that has been used.
            time (float): Value of the investigated time period in s.
            repetition_rate (float): Value of the recording repetition rate in Hz.
            field_of_view (str): Value of the field of view in m x m.
            height (Optional[PositiveInt]): Height of the image. Defaults to None
            width (Optional[PositiveInt]): Width of the image. Defaults to None
            n_frames (Optional[int]): Number of frames found in this video. Defaults to None
            frames (Union[NDArray, H5Dataset, None]): Videoframes. Defaults to None
        """

        params = {
            "camera_id": camera_id,
            "time": time,
            "repetition_rate": repetition_rate,
            "field_of_view": field_of_view,
            "height": height,
            "width": width,
            "n_frames": n_frames,
            "frames": frames,
        }

        if id is not None:
            params["id"] = id

        recordings = [Recording(**params)]

        self.recordings = self.recordings + recordings

    def add_to_processing_steps(
        self,
        name: str,
        processed_recording: Recording,
        software: Software,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'ProcessStep' to the attribute 'processing_steps'.

        Args:
            id (str): Unique identifier of the 'ProcessStep' object. Defaults to 'None'.
            name (str): Name of the processing step.
            processed_recording (Recording): Resulting video from the processing.
            software (Software): Software that has been used to perform the processing step.
        """

        params = {
            "name": name,
            "processed_recording": processed_recording,
            "software": software,
        }

        if id is not None:
            params["id"] = id

        processing_steps = [ProcessStep(**params)]

        self.processing_steps = self.processing_steps + processing_steps
