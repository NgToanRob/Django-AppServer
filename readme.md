## Install Docker and docker compose

We should follow this tutorial in docker docs to install Docker in your operation systems.

We have 4 services in this compose, there are django web app, postgresql database, redis caching and server engine nginx.
```bash
# Build network from 4 images in docker-compose.prd.yml file
docker-compose -f docker-compose.prd.yml build
# Run containers
docker-compose -f docker-compose.prd.yml start
# To stop 
docker-compose -f docker-compose.prd.yml stop

# To re-build and up containers (-d : without logs)
docker-compose -f docker-compose.prd.yml up -d --build

# To remove non-running containers
docker-compose -f docker-compose.prd.yml down
```


## Accessing

Admin link [localhost/admin](localhost/admin)

Create action in realtime link [localhost/realtime/realtime](localhost/realtime/realtime)
