#!/bin/env bash

# The idea of this simple program is to prevent the container from exit after start
# Initially that could be achieved by a simple while/true loop followed by sleep
# However, that approach could be more expensive since sleep would require a timer
# And that restarts every second, producing spikes.
# I would expect a tail -f for /dev/null observes and respect kernels device and not
# keep probing all the time. But that's a good opportunity for emperic measurement with
# eBPF later on.


# Exist with error if any command fails
set -e


# Start Database
su - postgres -c "/opt/postgres/pgsql_16_2/bin/pg_ctl start -D /opt/postgres/pgsql_16_2/data"



# Sart app
/usr/bin/python3 /opt/app/app.py >> /opt/log/app.log 2>&1


# Option 1:
# while true; do sleep 30; done;

# Option 2:
tail -f /dev/null
