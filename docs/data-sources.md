# Data Sources

- Secondary sources will often standardize multiple primary sources so they can be used together.
- Deal with differences in reporting formats, level of granularity/aggregation or underlying contents.
- If shared IDs don’t exist, they may link disparate sources together manually or using statistical methods and co-reported variables.
- May derive additional values of interest.
- Inevitably choices have to be made in the process, and some of the original detail gets lost.
- The benefit is that you can start with data that’s much closer to analysis ready and build upon it rather than starting from scratch.

## Worldwide Energy Data

- Most expansive datasets available.
- Necessarily relatively shallow.
- Recent moves toward free and open access.
- Typically sourced from national agency reporting
- Good for context, but not Catalyst's focus.

### OECD

### IEA

### IRENA

### World Bank

### [Global Energy Monitor](https://globalenergymonitor.org/)

- Worldwide coverage, industry as well as electricity generation
- Also doing primary data collection in the Global South

### [Climate Trace Data Downloads](https://climatetrace.org/data)

### [Our World In Data](https://ourworldindata.org/)

- Experimental [OWID Python API](https://docs.owid.io/projects/etl/api/)

## Open Source / Data Projects

### [Public Utility Data Liberation Project](https://catalystcoop-pudl.readthedocs.io/) (PUDL) (Catalyst Cooperative)

- Primarily focused on US federal electricity system data
- Mix of operational and financial/economic data

### [Open Grid Emissions Initiative](https://docs.singularity.energy/docs/open-grid-emissions/about_ogei-about-the-open-grid-emissions-initiative) (Singularity Energy)

- Uses PUDL, EPA and other data to estimate hourly emissions intensity by location

### [GridStatus](https://www.gridstatus.io/)

- Software behind the API is open source, but setting up the whole tech stack isn’t trivial
- Consolidates data from organized markets into a common API
- Can’t provide full granularity available in all data sources, because they vary considerably.
- Has to provide least-common-denominator data in the name of uniformity
- Large benefit in ease of use.
- Not actually free and open data – for higher volume usage a $500/mo subscription is required.

### [PyPSA Meets Earth](https://github.com/pypsa-meets-earth/earth-osm)

- Extracts electricity system data from the Open Street Map and converts the format / cleans it up for use in modeling.

## NGOs

### [RMI Utility Transition Hub](https://utilitytransitionhub.rmi.org/)

### [CarbonPlan Datasets](https://carbonplan.org/data)

- Carbon capture and sequestration project evaluations
- Carbon offset project evaluations
- Wildfire emissions estimates
- Downscaled climate model outputs

### [WattTime](https://watttime.org/data-science/data-signals/)

- Marginal emissions & human health impacts by time and location
- Non-profit NGO, but the data is no longer open.

## National Labs

- [LBNL grid interconnection queue status](https://emp.lbl.gov/queues)
- [LBNL Land-Based Wind Wind Market Report](https://emp.lbl.gov/wind-technologies-market-report)
- [LBNL Tracking the Sun](https://emp.lbl.gov/tracking-the-sun/)
- [LBNL Utility Scale Solar](https://emp.lbl.gov/utility-scale-solar)
- [LBNL/USGS US Large Scale PV Database](https://eerscmap.usgs.gov/uspvdb/data/)
- [LBNL/USGS US Wind Turbine Database](https://eerscmap.usgs.gov/uswtdb/data/)

## Academic

### Static archives

Datasets associated with a publication that have been archived for future reference, but are not actively maintained.

- [10+ years of locational marginal pricing data scraped from ISO/RTO websites](https://zenodo.org/records/3368397)

### Curated resources

Research datasets with at least an attempt at ongoing maintenance.

- [Power Sector Carbon Index](https://emissionsindex.org/) (Carnegie Mellon University)
- [GridEmissions](https://gridemissions.jdechalendar.su.domains/#/) (Stanford University)

```python
import pandas as pd

pd.read_csv("path/to/file.csv")
```
