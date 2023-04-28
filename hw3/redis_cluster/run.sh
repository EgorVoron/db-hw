#!/usr/bin/env bash

redis-server node_5000.conf
redis-server node_5001.conf
redis-server node_5002.conf

redis-cli --cluster create 127.0.0.1:5000 127.0.0.1:5001 127.0.0.1:5002 --cluster-yes
