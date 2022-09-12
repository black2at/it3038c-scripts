#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalizedCurrently')
ICU=$(echo $DATA | jq '.[0].inIcuCurrently')
VENTILATOR=$(echo $DATA | jq '.[0].onVentilatorCurrently')

echo "On $TODAY, there were $POSITIVE positive COVID cases, $HOSPITALIZED many people are currently hosipitalized, $ICU people are in the ICU, and $VENTILATOR are using a ventilator"
