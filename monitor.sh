#!/bin/bash
# ---------------------------------------------------
# BDG Corp Server Monitoring Script
# ---------------------------------------------------
echo "System Check: RAM is $(free -m | awk 'NR==2 {print $7 " MB"}') | Disk free is $(df / | awk 'NR==2 {print 100-$5 "%"}')" 