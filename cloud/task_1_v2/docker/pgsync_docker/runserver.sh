#! /bin/sh
./wait-for-it.sh postgres:5432 -t 60
./wait-for-it.sh elasticsearch:9200 -t 60
./wait-for-it.sh redis:6379 -t 60
./wait-for-it.sh kibana:5601 -t 60

python schema.py --config schema.json
python data.py --config schema.json

bootstrap --config schema.json
pgsync --config schema.json 


