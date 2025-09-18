## Overview

This is a Python package for generating FEBio input files.

## Getting Started

- [Installation](#installation)
- [Short Example](#short-example)
- Documentation
- [Features](#features)

## Installation

We will build PyPi packages later. For now, you can install from source:

Clone with https:

```bash
git clone https://github.com/CompOrthoBiomech/pyfebio.git
```

Or,

Clone with ssh:

```bash
git clone git@github.com:CompOrthoBiomech/pyfebio.git
```

**Using uv:**

Install uv from [here](https://docs.astral.sh/uv/getting-started/installation/)

In top-level repository directory:

```bash
uv sync
```

This will create a virtual environment and install the package.

**Using pip:**

In top-level repository directory:

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the package:

```bash
pip install -e .
```

## Short Example

## Features

Brief overview, see module documentation for more details. Unchecked to be implemented.

- Control
  - [x] All control settings
- Mesh Section
  - [x] Nodes
  - [x] Solid Elements:
     - tet4, tet10, hex8, hex20, hex27, penta6
  - [x] Shell Elements:
     - tri3, tri6, quad4, quad8, quad9, q4ans, q4eas
  - [x] Beam Elements:
     - line2, line3
  - [x] Node, Element, Surface Sets
- MeshDomain
  - [x] Solid, Shell, and Beam Domains
  - [x] Granular control for integration schmemes, etc.
- MeshData Section
  - [x] Node Data
    - [x] Scalar
    - [x] Vector3
  - [x] Element Data
    - [x] Scalar
    - [x] Vector3
  - [x] Surface Data
    - [x] Scalar
    - [x] Vector3
- Material
  - [x] Most Unconstrained Formulation Materials
  - [x] Most Uncoupled Formulation Materials
  - [x] Fiber models
  - [x] Continuous Fiber Distributions
    - [x] Integration Schemes
  - [] Biphasic Materials
  - [] Viscoelastic Materials
  - [] Multiphasic Materials
- Rigid
  - [x] Fixed Displacement and Rotation
  - [x] Prescribed Displacement and Rotation
  - [x] Precribed Rotation about Vector
  - [x] Prescribed Euler Rotation
  - [x] All Connectors
  - [x] Follower Loads
- Initial
  - [x] Initial Velocity
  - [x] Initial Pre-strain
- Loads
  - [x] Nodal Loads
  - [x] Traction Loads (surface)
  - [x] Pressure Loads (surface)
  - [x] Fluid Flux (surface)
  - [x] Fluid Pressure (surface)
- LoadData
  - [x] Load Curves
    - [x] All Options
  - [x] PID Controllers
  - [x] Math Controllers
- Boundary
  - [x] Fixed Displacement (solid and shell)
  - [x] Prescribed Displacement (solid and shell)
  - [x] Precribed Deformation Gradient
  - [x] Displacment Along Normals
  - [x] Fix to Rigid Body
  - [x] Rigid Node Set Deformation (translation and rotation)
  - [x] Zero Fluid Pressure
  - [x] Prescribed Fluid Pressure
- Constraints
  - [x] Symmetry Plane
  - [x] Prestrain
  - [x] In-Situ Stretch
- Contact
  - [x] Sliding
    - [x] Elastic
    - [x] Facet-Facet
    - [x] Node-Facet
    - [x] Biphasic
    - [x] Sliding2
    - [x] Contact Potential Formulation
  - [x] Tie
    - [x] Elastic
    - [x] Facet-Facet
    - [x] Node-Facet
    - [x] Biphasic
- Step
  - [x] Multistep Analysis
- Output
  - [x] Log File Configuration
  - [x] Plot File Configuration
  - [x] Node Variables
  - [x] Element Variables
  - [x] Rigid Body Variables
  - [x] Rigid Connector Variables
