import sdRDM

from typing import Optional, Union, List
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic.types import PositiveInt
from numpy.typing import NDArray
from h5py._hl.dataset import Dataset as H5Dataset
from typing import Union

from .software import Software
from .processstep import ProcessStep
from .recording import Recording
from .camera import Camera


@forge_signature
class Measurement(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
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
        multiple=True,
    )

    processing_steps: List[ProcessStep] = Field(
        description="Processed video data of the flow measurement",
        default_factory=ListPlus,
        multiple=True,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="9861f1edfafad8d066d12be2808992116bbd3b62"
    )

    def add_to_recordings(
        self,
        camera_id: Camera,
        time: float,
        repetition_rate: float,
        field_of_view: str,
        height: Optional[PositiveInt] = None,
        width: Optional[PositiveInt] = None,
        n_frames: Optional[int] = None,
        frames: Optional[Union[NDArray, H5Dataset]] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Recording' to attribute recordings

        Args:
            id (str): Unique identifier of the 'Recording' object. Defaults to 'None'.
            camera_id (): ID of the camera that has been used.
            time (): Value of the investigated time period in s.
            repetition_rate (): Value of the recording repetition rate in Hz.
            field_of_view (): Value of the field of view in m x m.
            height (): Height of the image. Defaults to None
            width (): Width of the image. Defaults to None
            n_frames (): Number of frames found in this video. Defaults to None
            frames (): Videoframes. Defaults to None
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

        self.recordings.append(Recording(**params))

    def add_to_processing_steps(
        self,
        name: str,
        processed_recording: Recording,
        software: Software,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'ProcessStep' to attribute processing_steps

        Args:
            id (str): Unique identifier of the 'ProcessStep' object. Defaults to 'None'.
            name (): Name of the processing step.
            processed_recording (): Resulting video from the processing.
            software (): Software that has been used to perform the processing step.
        """

        params = {
            "name": name,
            "processed_recording": processed_recording,
            "software": software,
        }

        if id is not None:
            params["id"] = id

        self.processing_steps.append(ProcessStep(**params))
