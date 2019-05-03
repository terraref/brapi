# TERRA-REF Breeder's API

Implementation of the BRAPI standard for the BETYdb, specifically the
TERRA-REF database.

## Setup BETYdb

Following commands can be used to initialize the database to be used 
with BRAPI development. This will fetch data from TERRA-REF database
(id=6). To get the latest data you can call the sync command.

```bash
docker-compose up -d postgres
docker-compose run --rm bety initialize
docker-compose run --rm bety sync
```

## Setup Locations

For the locations endpoint to work correctly you will need to group
multiple sites together in a sitegroup. The following commands can
be executed to associate sites with the sitegroups.

(This is now part of the TERRA-REF dump)

```sql
select count(a.id) from sites as a, sites as b where b.sitename='MAC Field Scanner Field' and ST_Intersects(a.geometry, b.geometry);

select a.id from sites as a, sites as b where b.sitename='MAC Field Scanner Field' and ST_Intersects(a.geometry, b.geometry);

% MAC FIELD
insert into sitegroups(name, public_access, user_id) 
    values('MAC Field Scanner Field', true, 6000000002);

insert into sitegroups_sites(sitegroup_id, site_id)
    select s.id, a.id 
           from sites as a, sites as b, sitegroups as s
           where b.sitename='MAC Field Scanner Field'
                 and b.sitename=s.name 
                 and ST_Intersects(a.geometry, b.geometry);

% KSU FIELD
insert into sitegroups(name, public_access, user_id)
    values('Ashland Bottoms KSU Field Site', true, 6000000002);

insert into sitegroups_sites(sitegroup_id, site_id) 
    select s.id, a.id 
           from sites as a, sites as b, sitegroups as s
           where b.sitename='Ashland Bottoms KSU Field Site' 
                 and b.sitename=s.name 
                 and ST_Intersects(a.geometry, b.geometry);

insert into sitegroups_sites(sitegroup_id, site_id) 
    select s.id, a.id 
           from sites as a, sitegroups as s
           where a.sitename like 'Ashland Bottoms KSU %'
                 and s.name='Ashland Bottoms KSU Field Site';

% Danforth
insert into sitegroups(name, public_access, user_id)
    values('Danforth Plant Science Center Bellweather Phenotyping Facility', true, 6000000002);

insert into sitegroups_sites(sitegroup_id, site_id)
    select s.id, a.id 
           from sites as a, sites as b, sitegroups as s
           where b.sitename='Danforth Plant Science Center Bellweather Phenotyping Facility'
                 and b.sitename=s.name 
                 and ST_Intersects(a.geometry, b.geometry);

insert into sitegroups_sites(sitegroup_id, site_id) 
    select s.id, a.id 
           from sites as a, sitegroups as s
           where a.sitename like 'Danforth Plant Science %'
                 and s.name='Danforth Plant Science Center Bellweather Phenotyping Facility'; 

% what is left?
select id, sitename from sites 
    where id not in (select site_id from sitegroups_sites);
```

## Mappings from BETY to BRAPI models

| BRAPI      | BETY        | Notes |
|------------|-------------|-------|
| /calls     | generated   |       |
| /locations | sitegroups  | lat/lon computed from sites part of sitegroup |
| /seasons   | experiments | season = month of start_date, year of start_date |
| /germplasm  | cultivars.  |       | 
| /observations | traits | |

## Contributed Data

This repository provides the canonical reference for data that is
outside of the scope of databases used in the TERRA REF program. Such
data can be found in the `/contrib/` folder. 

Genomics data in `contrib/genomics` is in a set of CSVs that were
previously only available in the [experimental design section of the
TERRA REF documentation](https://docs.terraref.org/scientific-objectives-and-experimental-design/experimental-design). These files provide metadata that describe the germplasm used in the sorghum trials, and were originally prepared by Noah Fahlgren. 

## How to add an endpoint

You will need add a new file under the `api` folder called with the
name of the endpoint, for example /locations will need a file called
api/locations.py. In there you will need a `search` function to
handle the call to the GET endpoint. If the function is not
implemented the url will return the actual name of the file and the
function name.

## Showing data in BETY database

You can use the following command to start a docker container that is connected to the database
allowing you to browse the database.

```
docker-compose up -d bety
```

To enable the guest user you can run the following sql query when
connected to the database:

```
INSERT INTO users (login, name, email, crypted_password, salt, city, state_prov, postal_code, country, area, access_level, page_access_level, created_at, updated_at, apikey, remember_token, remember_token_expires_at)
 VALUES ('guestuser', 'guestuser', 'betydb@example.com', '994363a949b6486fc7ea54bf40335127f5413318', 'bety', 'Urbana', 'IL', '61801', 'USA', '', 4, 4, NOW(), NOW(), NULL, NULL, NULL);
```

## Testing your additions

Before you commit your new endpoints or any new code, please make sure that you check it with
BRAVA. You can do this by running the brava container `docker-compose up -d brava`. At this point
you can connect to http://localhost:8080/ to see the UI.

Next switch to 'Test your own' and change the URL. If you run the brapi server as a docker
container in docker-compose you can use `http://brapi:5000/brapi/v1` as the URL. If you run
the server on your machine you can either use `http://host.docker.internal:5000/brapi/v1` or
you can use `http://<ipaddress>:5000/brapi/v1`.
