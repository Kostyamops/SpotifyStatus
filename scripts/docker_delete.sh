#!/bin/bash

# This script stops and removes all Docker containers, networks,
# and volumes defined in the docker-compose.yaml file.
# Should be run from the root of the project.

echo "[*] Stopping and deleting Docker containers, networks, and volumes..."
docker compose down --volumes --remove-orphans
# --volumes: Removes named and anonymous volumes declared in the compose file.
# --remove-orphans: Removes containers not defined in the current compose file but attached to the network.

# Check if the previous command was successful
if [ $? -eq 0 ]; then
    echo "[✔] Containers, networks, and volumes removed successfully."
else
    echo "[✘] Error while deleting containers, networks, or volumes. Try manually."
    exit 1
fi

# Optionally, remove dangling images
echo "[*] Removing dangling Docker images..."
docker image prune -f
# -f: Forces the removal without confirmation.

if [ $? -eq 0 ]; then
    echo "[✔] Dangling images removed successfully."
else
    echo "[✘] Error while removing dangling images. Try manually."
    exit 1
fi

echo "[✔] Cleanup completed successfully."