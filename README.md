# TERRA-REF Breeder's API

This repository contains preliminary work torward a BRAPI implementation
for TERRA-REF.


The server code was generated using [swagger-codegen](https://github.com/swagger-api/swagger-codegen).

## Requirements
Python 3.5.2+

## Usage
To run, first start an intance of the BETY database:

```
docker run --name betydb -d -p 5431:5432 terraref/bety-postgis
```

Install the python requirements and start the Flask server:
```
pip3 install -r requirements.txt
./run.sh
```

then open your browser to here:

```
http://localhost:8080/brapi/v1/ui/
```

The only call implemented is the `GET phenotypes-search` with a very very
preliminary mapping of BETY fields to BRAPI objects.


## Mappings from BETY to BRAPI models

| BRAPI      | BETY        | Notes |
|------------|-------------|-------|
| /calls     | generated   |       |
| /locations | sitegroups  | lat/lon computed from sites part of sitegroup |
| /seasons   | experiments | season = month of start_date, year of start_date |
| /germplasm  | cultivars.  |       | 
| /observations | traits | |


## How to add an endpoint

Example: see controllers/crops_controller.py and CropsController_impl.py