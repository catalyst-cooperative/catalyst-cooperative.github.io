# Data Sources

- Secondary sources will often standardize multiple primary sources so they can be used together.
- Deal with differences in reporting formats, level of granularity/aggregation or underlying contents.
- If shared IDs don’t exist, they may link disparate sources together manually or using statistical methods and co-reported variables.
- May derive additional values of interest.
- Inevitably choices have to be made in the process, and some of the original detail gets lost.
- The benefit is that you can start with data that’s much closer to analysis ready and build upon it rather than starting from scratch.

## International / Global data (OECD, IEA, IRENA, World Bank)

- Most expansive datasets available.
- Necessarily relatively shallow.
- Recent moves toward free and open access.
- Typically sourced from national agency reporting
- Good context, but not our focus.

## Open Source / Data Projects

- [Public Utility Data Liberation Project](https://catalystcoop-pudl.readthedocs.io/) (PUDL) (Catalyst Cooperative)
  - Primarily focused on US federal electricity system data
  - Mix of operational and financial/economic data
- [Open Grid Emissions Initiative](https://docs.singularity.energy/docs/open-grid-emissions/about_ogei-about-the-open-grid-emissions-initiative) (Singularity Energy)
  - Uses PUDL, EPA and other data to estimate hourly emissions intensity by location
- [GridStatus](https://www.gridstatus.io/)
  - Software behind the API is open source, but setting up the whole tech stack isn’t trivial
  - Consolidates data from organized markets into a common API
  - Can’t provide full granularity available in all data sources, because they vary considerably.
  - Has to provide least-common-denominator data in the name of uniformity
  - Large benefit in ease of use.
  - Not actually free and open data – for higher volume usage a $500/mo subscription is required.
- [PyPSA Meets Earth](https://github.com/pypsa-meets-earth/earth-osm)
  - Extracts electricity system data from the Open Street Map and converts the format / cleans it up for use in modeling.

## NGOs

- [Global Energy Monitor](https://globalenergymonitor.org/)
  - Worldwide coverage, industry as well as power
  - Also doing primary data collection in the Global South
- [Climate Trace Data Downloads](https://climatetrace.org/data)
- [RMI Utility Transition Hub](https://utilitytransitionhub.rmi.org/)
- [CarbonPlan Datasets](https://carbonplan.org/data)
- [Our World In Data](https://ourworldindata.org/) (new [experimental Python API](https://docs.owid.io/projects/etl/api/))
- [WattTime](https://watttime.org/data-science/data-signals/) marginal emissions & human health impacts by time and location (NGO, but not open data)

## National Labs

- [LBNL grid interconnection queue status](https://emp.lbl.gov/queues)
- [LBNL Land-Based Wind Wind Market Report](https://emp.lbl.gov/wind-technologies-market-report)
- [LBNL Tracking the Sun](https://emp.lbl.gov/tracking-the-sun/)
- [LBNL Utility Scale Solar](https://emp.lbl.gov/utility-scale-solar)
- [LBNL/USGS US Large Scale PV Database](https://eerscmap.usgs.gov/uspvdb/data/)
- [LBNL/USGS US Wind Turbine Database](https://eerscmap.usgs.gov/uswtdb/data/)

## Academic

- Static, self-archived datasets associated with peer reviewed publications, e.g.

  - [Shaping photovoltaic array output to align with changing wholesale electricity price profiles](https://zenodo.org/records/3368397) (on Zenodo)

- Semi-automated dataset updates, e.g.

  - [Power Sector Carbon Index](https://emissionsindex.org/) (Carnegie Mellon University)
  - [GridEmissions](https://gridemissions.jdechalendar.su.domains/#/) (Stanford University)

```python
import pandas as pd

pd.read_csv("path/to/file.csv")
```
