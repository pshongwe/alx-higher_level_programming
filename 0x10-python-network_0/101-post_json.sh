#!/bin/bash
# 101
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
