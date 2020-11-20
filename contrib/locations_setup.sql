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