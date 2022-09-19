## Clone project from git
```
git clone https://github.com/phantruyenqnx/QNXserver-Demo.git
git branch -M main
```

## Install Docker and docker compose

We should follow this tutorial in docker docs to install Docker in your operation systems. My OS is Ubuntu 22.04 and below lines are my workflow after installing them.

We have 3 services in this compose, there are web app, postgresql database and server engine nginx.
```bash
# Build network from 3 images in docker-compose.prd.yml file
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
