#!/bin/bash
set -e
echo "✓ Charters intact"
ls canon/dossiers/ || mkdir -p canon/dossiers
ls canon/index/ || mkdir -p canon/index
