Catalyst Cooperative Documentation Index
========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

`The Public Utility Data Liberation Project (PUDL) <https://docs.catalyst.coop/pudl>`__
---------------------------------------------------------------------------------------

PUDL (pronounced puddle) is a data processing pipeline created by `Catalyst Cooperative
<https://catalyst.coop>`__ that cleans, integrates, and standardizes some of the most
widely used public energy datasets in the US. The data serves researchers, activists,
journalists, and policy makers that might not have the technical expertise to access it
in its raw form, the time to clean and prepare the data for bulk analysis, or the means
to purchase it from existing commercial providers.

- `The Public Utility Data Liberation (PUDL) Project <https://docs.catalyst.coop/pudl>`__
- `Data Documentation <https://docs.catalyst.coop/pudl/en/nightly/data.html>`__
- `Developer Documentation <https://docs.catalyst.coop/pudl/en/nightly/code.html>`__
- `PUDL Data Viewer <https://data.catalyst.coop/>`__

`PUDL Examples <https://docs.catalyst.coop/pudl-examples>`__
------------------------------------------------------------

A collection of example notebooks that work with PUDL data.

- The `Jupyter <https://jupyter-notebook.readthedocs.io/en/stable/notebook.html>`__
  notebooks are hosted on `Kaggle <https://www.kaggle.com/catalystcooperative/code>`__.
- The `Marimo <https://docs.marimo.io/>`__ notebooks are hosted in `the PUDL Data Viewer
  <https://data.catalyst.coop/dashboards>`_

`PUDL Data Archivers <https://github.com/catalyst-cooperative/pudl-archiver>`__
-------------------------------------------------------------------------------

This repo implements data archivers for The Public Utility Data Liberation Project
(PUDL). It is responsible for downloading raw data from multiple sources, and create
Zenodo archives containing that data.

- All Catalyst data archives can be found on `CERN's Zenodo research data management
  platform <https://zenodo.org/communities/catalyst-cooperative/>`__.
- Data beyond what is used in PUDL is archived in collaboration with `Public
  Environmental Data Partners <https://screening-tools.com/>`__.

`Open Energy Data For All <https://docs.catalyst.coop/open-energy-data-for-all>`__
----------------------------------------------------------------------------------

A two-day, 16-hour course on foundational software and data engineering skills aimed at
energy systems graduate students looking to generate more robust, replicable energy
analyses. Developed using `The Carpentries <https://carpentries.org/>`__ pedagogical
framework with financial support from the `Alfred P. Sloan Foundation
<https://sloan.org/>`__.

`Catalyst Agent Skills <https://github.com/catalyst-cooperative/agent-skills>`__
--------------------------------------------------------------------------------

A collection of `agent skills <https://agentskills.io/home>`__ that help LLM-based
agents work with the PUDL data, metadata, and codebase.

`FERC XBRL Extractor <https://docs.catalyst.coop/ferc-xbrl-extractor>`__
------------------------------------------------------------------------

A Python package for extracting FERC Form 1, 2, 6, 60, & 714 data from the XML-based
`XBRL format <https://en.wikipedia.org/wiki/XBRL>`__ it's published in, into file-based
`SQLite <https://sqlite.org>`__ and `DuckDB <https://duckdb.org>`__ databases for
analytical use.

`CAMD-EIA Crosswalk <https://github.com/catalyst-cooperative/camd-eia-crosswalk-latest>`__
------------------------------------------------------------------------------------------

This repository is a fork of the `original EPA-EIA crosswalk
<https://github.com/USEPA/camd-eia-crosswalk>`__ repo, and updates the system to be able to
use any recent year of data and to build a crosswalk that covers multiple years of data.

`Eel Hole <https://github.com/catalyst-cooperative/eel-hole>`__
---------------------------------------------------------------

Eel-hole is the web-app that runs the `PUDL Data Viewer <https://data.catalyst.coop>`__

`Member Handbook <https://catalystcoop-handbook.readthedocs.io>`__
------------------------------------------------------------------

The Catalyst handbook contains the cooperative's bylaws, policies and general operating
information.
