#!/bin/bash

# These are color variables for terminal output.
GREEN="\033[1;32m"
CYAN="\033[1;36m"
YELLOW="\033[1;33m"
NC="\033[0m"

# Prints a menu header.
echo -e "${CYAN}======================================${NC}"
echo -e "${GREEN}        WELCOME TO SUPER SEARCH      ${NC}"
echo -e "       Please select search mode"
echo -e "${CYAN}======================================${NC}"

# When the user types 0, -maxdepth 1 is used, so the script does NOT go into subfolders.
# When the user types 1, -maxdepth 1 is NOT used, so the script scans all directories and subdirectories under .

while true; do
    echo "0 - Simple"    # Scan only the current directory
    echo "1 - Advanced"  # Scan subdirectories 
    read -p "Enter 0 or 1: " choice

    case $choice in
        0)
            largest_file=$(find . -maxdepth 1 -type f -printf "%s %p\n" | sort -nr | head -n1 | cut -d' ' -f2-)
            break
            ;;
        1)
            largest_file=$(find . -type f -printf "%s %p\n" | sort -nr | head -n1 | cut -d' ' -f2-)
            break
            ;;
        *)
            echo "Invalid option. Please enter 0 or 1."
            ;;
    esac
done

file_size=$(stat -c %s "$largest_file" | numfmt --to=iec --suffix=B)

# Prints results in green labels, with normal color for the values.

echo -e "${GREEN}Largest file:${NC} $largest_file"
echo -e "${GREEN}Size:${NC} $file_size"