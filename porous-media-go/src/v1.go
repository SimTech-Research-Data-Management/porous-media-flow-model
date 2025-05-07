// Package porousmedia contains Go struct definitions with JSON serialization.
//
// WARNING: This is an auto-generated file.
// Do not edit directly - any changes will be overwritten.

package porousmedia

import (
	"encoding/json"
	"fmt"
)

//
// Type definitions
//

// Metadata
//
// The Metadata summarizes key information about the following dataset. It includes
// a description of the dataset's content, a descriptive name or ID of the
// dataset, and the date of creation. It also lists the contributors, highlights
// the research areas which are covered and specifies the specific porous media
// model investigated. Descriptive keywords help categorize the dataset and
// the the hardware used in the experiment is also stored. Free flow conditions
// of the turbulent air flow are also stored. The Metadata provides detailed
// information about the measurements conducted in the experiment.
type Metadata struct {
	Id           int64         `json:"-" gorm:"primaryKey;autoIncrement"`
	Description  string        `json:"description" `
	DatasetId    string        `json:"dataset_id" `
	Date         string        `json:"date" `
	Authors      []Author      `json:"authors" gorm:"many2many:metadata_authors;"`
	Subjects     []string      `json:"subjects" gorm:"serializer:json;"`
	ModelID      int64         `json:"-"`
	Model        Model         `json:"model,omitempty" gorm:"foreignKey:ModelID;"`
	Keywords     []string      `json:"keywords" gorm:"serializer:json;"`
	Devices      []Hardware    `json:"devices" gorm:"many2many:metadata_devices;"`
	FreeFlowID   int64         `json:"-"`
	FreeFlow     FreeFlow      `json:"free_flow,omitempty" gorm:"foreignKey:FreeFlowID;"`
	Measurements []Measurement `json:"measurements,omitempty" gorm:"many2many:metadata_measurements;"`
}

// Author
//
// The Author section provides information about the persons involved in working
// on or creating the dataset.These information helps providing the identity and
// contact details of the authors associated with the dataset.
type Author struct {
	Id          int64  `json:"-" gorm:"primaryKey;autoIncrement"`
	Name        string `json:"name" `
	Affiliation string `json:"affiliation" `
	Email       string `json:"email" `
	Phone       int64  `json:"phone,omitempty" `
}

// FreeFlow
//
// The Free Flow section contains information about the shape, dimensions, and
// working fluid of the free flow channel.It provides details such as the shape
// of the flow channel's cross-section, the hydraulic diameter, height, width
// and depth of the channel and a description of the flow parameters of the
// working fluid.
type FreeFlow struct {
	Id                int64          `json:"-" gorm:"primaryKey;autoIncrement"`
	Shape             string         `json:"shape" `
	HydraulicDiameter float64        `json:"hydraulic_diameter" `
	FluidID           int64          `json:"-"`
	Fluid             FlowParameters `json:"fluid" gorm:"foreignKey:FluidID;"`
	Height            float64        `json:"height,omitempty" `
	Width             float64        `json:"width,omitempty" `
	Depth             float64        `json:"depth,omitempty" `
	Diameter          float64        `json:"diameter,omitempty" `
}

// FlowParameters
//
// The Flow Parameters encompasses crucial details about the flow parameters of
// the working fluid used in the present dataset. These parameters provide a
// comprehensive understanding of the fluid's properties and flow conditions
// within the experiment.
type FlowParameters struct {
	Id                 int64     `json:"-" gorm:"primaryKey;autoIncrement"`
	Fluid              string    `json:"fluid" `
	Temperature        float64   `json:"temperature" `
	Pressure           float64   `json:"pressure" `
	Density            float64   `json:"density" `
	KinematicViscosity float64   `json:"kinematic_viscosity" `
	DynamicViscosity   float64   `json:"dynamic_viscosity" `
	MassFlux           []float64 `json:"mass_flux" gorm:"serializer:json;"`
	ReynoldsNumber     []float64 `json:"reynolds_number" gorm:"serializer:json;"`
}

// Model
//
// The Model section contains information about the location of the object in the
// flow channel.It provides details regarding the type of the present porous
// media model, its location relative to the free flow and if applicable,
// detailed parameters related to the model which was used.
type Model struct {
	Id            int64       `json:"-" gorm:"primaryKey;autoIncrement"`
	Type          string      `json:"type" `
	Location      string      `json:"location" `
	PorousMediaID int64       `json:"-"`
	PorousMedia   PorousMedia `json:"porous_media,omitempty" gorm:"foreignKey:PorousMediaID;"`
	CadModel      []byte      `json:"cad_model,omitempty" `
}

// PorousMedia
//
// The Porous Media contains information regarding the parameters associated with
// the utilized porous media model.They include the topology of the porous media
// model, the dimensions and other relevant material properties.
type PorousMedia struct {
	Id            int64   `json:"-" gorm:"primaryKey;autoIncrement"`
	Topology      string  `json:"topology" `
	Height        float64 `json:"height" `
	Width         float64 `json:"width" `
	Depth         float64 `json:"depth" `
	Porosity      float64 `json:"porosity" `
	Permeability  float64 `json:"permeability,omitempty" `
	PeriodicityX  float64 `json:"periodicity_x,omitempty" `
	PeriodicityY  float64 `json:"periodicity_y,omitempty" `
	WallThickness float64 `json:"wall_thickness,omitempty" `
}

// Hardware
//
// The Hardware includes descriptions of the camera systems, laser systems, seeding
// devices and materials, optical devices, and triggering systems utilized
// during the experiment.
type Hardware struct {
	Id         int64        `json:"-" gorm:"primaryKey;autoIncrement"`
	Camera     []Camera     `json:"camera" gorm:"many2many:hardware_camera;"`
	Laser      []Laser      `json:"laser" gorm:"many2many:hardware_laser;"`
	Seeding    []Seeding    `json:"seeding" gorm:"many2many:hardware_seeding;"`
	Optics     []Device     `json:"optics,omitempty" gorm:"many2many:hardware_optics;"`
	Triggering []Triggering `json:"triggering,omitempty" gorm:"many2many:hardware_triggering;"`
}

// Device
//
// The Device provides general information about the manufacturer and model of the
// used devices such as cameras, lasers, optics, triggering and seeding systems.
type Device struct {
	Id           int64  `json:"-" gorm:"primaryKey;autoIncrement"`
	Manufacturer string `json:"manufacturer" `
	Model        string `json:"model,omitempty" `
}

// Camera
//
// It specifies details about the camera lenses and sensors which were used during
// the experiment.
type Camera struct {
	Id           int64  `json:"-" gorm:"primaryKey;autoIncrement"`
	Manufacturer string `json:"manufacturer" `
	Model        string `json:"model,omitempty" `
	Lens         string `json:"lens,omitempty" `
	Sensor       string `json:"sensor,omitempty" `
}

// Laser
//
// The Laser provides information about the laser wavelength, either the laser is
// pulsed or continuous as well as the laser power.
type Laser struct {
	Id           int64   `json:"-" gorm:"primaryKey;autoIncrement"`
	Manufacturer string  `json:"manufacturer" `
	Wavelength   float64 `json:"wavelength" `
	Model        string  `json:"model,omitempty" `
	Type         string  `json:"type,omitempty" `
	Power        float64 `json:"power,omitempty" `
}

// Seeding
//
// The Seeding describes the material of the seeding particles, the type of them as
// well as their density, particle size, and kinematic viscosity.
type Seeding struct {
	Id           int64             `json:"-" gorm:"primaryKey;autoIncrement"`
	Manufacturer string            `json:"manufacturer" `
	ParticlesID  int64             `json:"-"`
	Particles    SeedingParameters `json:"particles" gorm:"foreignKey:ParticlesID;"`
	Model        string            `json:"model,omitempty" `
}

// SeedingParameters
//
// The Seeding Parameters contains crucial information about the seeding material
// used in the experiment.It includes details such as the material name,
// particle type, density, particle size and the kinematic viscosity of the
// seeding particles.These parameters provide valuable insights integero the
// characteristics of the seeding material and its influence on the fluid flow
// behavior within the experimental setup.
type SeedingParameters struct {
	Id                 int64   `json:"-" gorm:"primaryKey;autoIncrement"`
	Material           string  `json:"material" `
	Phase              string  `json:"phase" `
	Density            float64 `json:"density" `
	ParticleSize       float64 `json:"particle_size" `
	KinematicViscosity float64 `json:"kinematic_viscosity,omitempty" `
}

// Triggering
//
// The Triggering explains the recording mode employed during the experiment.
type Triggering struct {
	Id            int64  `json:"-" gorm:"primaryKey;autoIncrement"`
	Manufacturer  string `json:"manufacturer" `
	RecordingMode string `json:"recording_mode" `
	Model         string `json:"model,omitempty" `
}

// Measurement
//
// The Measurement encompasses key details about the conducted experiment and its
// calibration.
type Measurement struct {
	Id              int64         `json:"-" gorm:"primaryKey;autoIncrement"`
	Name            string        `json:"name" `
	Calibration     []Calibration `json:"calibration,omitempty" gorm:"many2many:measurement_calibration;"`
	Recordings      []Recording   `json:"recordings,omitempty" gorm:"many2many:measurement_recordings;"`
	ProcessingSteps []ProcessStep `json:"processing_steps,omitempty" gorm:"many2many:measurement_processing_steps;"`
}

// Calibration
//
// The Calibration contains information about the parameters used during the
// recording process.The parameters are providing insights integero the camera
// position relative to the experiment for correcting possible misalignments.
type Calibration struct {
	Id                        int64   `json:"-" gorm:"primaryKey;autoIncrement"`
	CalibrationType           string  `json:"calibration_type" `
	ScaleFactor               float64 `json:"scale_factor" `
	CameraPositionTranslation float64 `json:"camera_position_translation,omitempty" `
	CameraPositionRotation    float64 `json:"camera_position_rotation,omitempty" `
	CalibrationImage          []byte  `json:"calibration_image,omitempty" `
}

// ProcessStep
//
// The Process Step outlines the specific processing steps applied to the flow
// measurement video data.It includes the name of each processing step, the
// resulting video from the processing, and the software used to post-process
// the data.Additionally, files with the extension ".lvs" from the Davis 10
// software can be embedded within this section, providing a comprehensive
// record of the processing workflow and ensuring the availability of relevant
// files for reference and replication.
type ProcessStep struct {
	Id                 int64       `json:"-" gorm:"primaryKey;autoIncrement"`
	Name               string      `json:"name" `
	OperationList      []Operation `json:"operation_list,omitempty" gorm:"many2many:processstep_operation_list;"`
	ProcessedRecording []Recording `json:"processed_recording,omitempty" gorm:"many2many:processstep_processed_recording;"`
	Software           []Software  `json:"software" gorm:"many2many:processstep_software;"`
}

// Operation
//
// The Operation section defines the specific operations performed during the data
// processing.It includes the name of the operation, its description, and the
// parameters used in the operation.
type Operation struct {
	Id          int64       `json:"-" gorm:"primaryKey;autoIncrement"`
	Name        string      `json:"name" `
	Description string      `json:"description,omitempty" `
	Parameters  []Parameter `json:"parameters,omitempty" gorm:"many2many:operation_parameters;"`
}

// Parameter
//
// The Parameter section defines the specific parameters used in various operations
// during the data processing. It includes the name of the parameter and
// its corresponding value, which can be a float, string, or boolean. This
// information is crucial for understanding the exact configuration of each
// operation and ensuring reproducibility of the processing steps.
type Parameter struct {
	Id    int64              `json:"-" gorm:"primaryKey;autoIncrement"`
	Name  string             `json:"name" `
	Value ParameterValueType `json:"value,omitempty" `
}

// Software
//
// The Software section serves as a container for general information about
// the software utilized in the experiment.It includes details such as the
// name of the manufacturer, the specific software name, and the version
// used to generate the dataset.These details provide important context for
// the experiment, allowing for reproducibility and facilitating a clear
// understanding of the software environment in which the data analysis and
// processing were performed.
type Software struct {
	Id           int64  `json:"-" gorm:"primaryKey;autoIncrement"`
	Manufacturer string `json:"manufacturer" `
	Name         string `json:"name" `
	Version      string `json:"version,omitempty" `
}

// Recording
//
// The Recording contains crucial information about the parameters used during
// the recording process.These parameters offer valuable insights integero the
// experimental setup, facilitating accurate analysis and integererpretation
// of the recorded data. The inclusion of the video frames allows for a visual
// reference and further examination of the recorded footage.
type Recording struct {
	Id             int64   `json:"-" gorm:"primaryKey;autoIncrement"`
	Time           float64 `json:"time" `
	RepetitionRate float64 `json:"repetition_rate" `
	FieldOfView    string  `json:"field_of_view" `
	NFrames        int64   `json:"n_frames,omitempty" `
	Frames         []byte  `json:"frames,omitempty" `
	Location       string  `json:"location,omitempty" `
}

// ParameterValueType represents a union type that can hold any of the following types:
// - float
// - string
// - boolean
type ParameterValueType struct {
	Float   float64
	String  string
	Boolean bool
}

// UnmarshalJSON implements custom JSON unmarshaling for ParameterValueType
func (t *ParameterValueType) UnmarshalJSON(data []byte) error {
	// Reset existing values
	t.Float = 0
	t.String = ""
	t.Boolean = false
	var floatValue float64
	if err := json.Unmarshal(data, &floatValue); err == nil {
		t.Float = floatValue
		return nil
	}
	var stringValue string
	if err := json.Unmarshal(data, &stringValue); err == nil {
		t.String = stringValue
		return nil
	}
	var boolValue bool
	if err := json.Unmarshal(data, &boolValue); err == nil {
		t.Boolean = boolValue
		return nil
	}
	return fmt.Errorf("ParameterValueType: data is neither float, string, boolean")
}

// MarshalJSON implements custom JSON marshaling for ParameterValueType
func (t ParameterValueType) MarshalJSON() ([]byte, error) {
	if t.Float != 0 {
		return json.Marshal(t.Float)
	}
	if t.String != "" {
		return json.Marshal(t.String)
	}
	if t.Boolean {
		return json.Marshal(t.Boolean)
	}
	return []byte("null"), nil
}
