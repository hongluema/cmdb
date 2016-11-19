#!/bin/bash

/usr/local/bin/gunicorn cmdb:app -w 2 -b :80
