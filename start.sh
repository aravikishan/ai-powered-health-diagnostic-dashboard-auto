#!/bin/bash
set -e
echo "Starting AI-Powered Health Diagnostic Dashboard..."
uvicorn app:app --host 0.0.0.0 --port 9090 --workers 1
