module PorousMedia

# Include the submodules in correct dependency order
include("V1.jl")

# Re-export commonly used third-party packages
using JSON3

# Use the PorousMedia module from V1.jl
using .PorousMediaV1

# Export third-party packages
export JSON3

# Export types and structs from V1.jl
export Recording, Software, ProcessStep, Calibration, Measurement
export Triggering, SeedingParameters, Seeding, Laser, Camera
export Device, Hardware, PorousMedia, Model, FlowParameters
export FreeFlow, Author, Metadata

end # module PorousMedia