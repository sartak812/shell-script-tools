#!/bin/bash
# ---------------------------------------------------
# BDG Corp Server Monitoring Script
# ---------------------------------------------------
echo "System Check: $(free -m | awk 'NR==2 {print $7 " MB"}')"