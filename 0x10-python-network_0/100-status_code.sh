#!/bin/bash
# 100
curl -s -o /dev/null -w "%{http_code}" "$1"
