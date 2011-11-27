#!/bin/bash
set -e
#Define User & Group
USER=`whoami`
GROUP=admin
LOGFILE="/opt/webapps/ncsu/log/gunicorn.log"
NUM_WORKERS=3
TIMEOUT=180
cd /opt/webapps/ncsu/wolfscout
source ../bin/activate
exec /opt/webapps/ncsu/bin/gunicorn_django -w $NUM_WORKERS \
    --user=$USER --group=$GROUP --log-level=debug \
    --log-file=$LOGFILE 2>>$LOGFILE \
    --timeout=$TIMEOUT
