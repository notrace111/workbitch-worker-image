#!/usr/bin/env bash
set -Eeuo pipefail

echo "=== WORK BITCH POD START ==="
echo "Mode: headless RunPod worker"

# Work Bitch does not use Jupyter. Keeping Jupyter out of the boot path removes
# an unnecessary failure dependency while preserving RunPod's official SSH
# and long-lived pod lifecycle through /start.sh.
unset JUPYTER_PASSWORD

if [ ! -x /start.sh ]; then
  echo "FATAL: RunPod /start.sh missing or not executable" >&2
  exit 70
fi

exec /start.sh
