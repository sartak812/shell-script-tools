#!/bin/bash
# ---------------------------------------------------
# BDG Corp Server Monitoring Script
# ---------------------------------------------------
echo "System Check: $(df / | awk 'NR==2 {print 100-$5 "%"}')"