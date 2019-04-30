# TERRA-REF Breeder's API

This repository contains preliminary work torward a BRAPI implementation
for TERRA-REF.

```bash
docker-compose up -d postgres
docker-compose run --rm bety initialize
docker-compose run --rm bety sync
```


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

## Contributed Data

This repository provides the canonical reference for data that is outside of the scope of databases used in the TERRA REF program. Such data can be found in the `/contrib/` folder. 

Genomics data in `contrib/genomics` is in a set of CSVs that were previously only available in the [experimental design section of the TERRA REF documentation](https://docs.terraref.org/scientific-objectives-and-experimental-design/experimental-design). These files provide metadata that describe the germplasm used in the sorghum trials, and were originally prepared by Noah Fahlgren. 

## How to add an endpoint

Example: see controllers/crops_controller.py and CropsController_impl.py

## Showing data in BETY database

You can use the following command to start a docker container that is connected to the database
allowing you to browse the database.

```
docker run -ti --rm -p 8000:8000 --link betydb:postgres pecan/bety
```

To enable the guest user you can run the following sql query when connected to the database:

```
INSERT INTO users (login, name, email, crypted_password, salt, city, state_prov, postal_code, country, area, access_level, page_access_level, created_at, updated_at, apikey, remember_token, remember_token_expires_at)
 VALUES ('guestuser', 'guestuser', 'betydb@example.com', '994363a949b6486fc7ea54bf40335127f5413318', 'bety', 'Urbana', 'IL', '61801', 'USA', '', 4, 4, NOW(), NOW(), NULL, NULL, NULL);
```
