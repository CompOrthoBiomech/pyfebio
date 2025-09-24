Getting Started
===============

Installation
------------

Clone with https:

.. code-block:: bash

    git clone https://github.com/CompOrthoBiomech/pyfebio.git

Or,

Clone with ssh:

.. code-block:: bash

    git clone git@github.com:CompOrthoBiomech/pyfebio.git

**Using uv:**

Install uv from `here <https://docs.astral.sh/uv/getting-started/installation/>`_

In top-level repository directory:

.. code-block:: bash

    uv sync

This will create a virtual environment and install the package.

**Using pip:**

In top-level repository directory:

Create a virtual environment:

.. code-block:: bash

    python -m venv .venv

Activate the virtual environment:

.. code-block:: bash

    source .venv/bin/activate

Install the package:

.. code-block:: bash

    pip install -e .

If you want to run the tests, additionally install the dev group dependencies:

.. code-block:: bash

    pip install . --group dev

To verify the installation, run:

.. code-block:: bash

    python -c "import pyfebio"

Testing
~~~~~~~

We rely on FEBio to check our generated models are valid. Therefore, you will need to have FEBio installed and available in your PATH.

To run all the tests, execute the following command:

.. code-block:: bash

    cd src
    pytest

For tests that depend on running finite element simulations, you can find them in the pytest tmp_path directory, which varies by operating system.

For the latest run:

on Linux,

.. code-block:: bash
    cd /tmp/pytest-of-[USER]/pytest-current/[TEST_FUNCTION_NAME]current

General Overview
----------------

pyfebio utilizes the pydantic-xml package, which extends the powerful type checking libary pydantic to support XML serialization.
An FEBio input file is an XML tree with the following top-level structure:

.. code-block:: xml

    <febio_spec version="4.0">
        <Module>
            ...
        </Module>
        <Globals>
            ...
        </Globals>
        <Control>
            ...
        </Control>
        <Material>
            ...
        </Material>
        <Mesh>
            ...
        </Mesh>
        <MeshDomains>
            ...
        </MeshDomains>
        <MeshData>
            ...
        </MeshData>
        <MeshAdaptor>
            ...
        </MeshAdaptor>
        <Initial>
            ...
        </Initial>
        <Boundary>
            ...
        </Boundary>
        <Loads>
            ...
        </Loads>
        <Contact>
            ...
        </Contact>
        <Constraints>
            ...
        </Constraints>
        <Rigid>
            ...
        </Rigid>
        <Discrete>
            ...
        </Discrete>
        <LoadData>
            ...
        </LoadData>
        <Step>
            ...
        </Step>
        <Output>
            ...
        </Output>
    </febio_spec>

The modules in pyfebio are divided and named based on this structure.

- module.py
- globals.py
- control.py
- material.py
- mesh.py
- meshdomains.py
- meshdata.py
- meshadaptor.py
- initial.py
- boundary.py
- loads.py
- contact.py
- constraints.py
- rigid.py
- discrete.py
- loaddata.py
- step.py
- output.py
