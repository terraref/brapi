# Run BETY
#docker run -n betydb -d -p 5432:5432 terraref/bety-postgis


export DBHOST=localhost
export DBNAME=bety
export DBUSER=bety
export DBPASS=bety

python3 -m bety_brapi
