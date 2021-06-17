# Django boilerplate    
     This is yet another django boilerplate with docker to make dev easier .

<img align="center" src="./public/images/landing.png"/>

## Skeleton

Here is the basic suggested skeleton for your app repo that each of the starter templates conforms to:

```bash
├── project (Django project)
├── application1 (Django app)
├── application2 (Django app)
├── templates
│    ├── **/*.html(Django Template language views)
├── static
    ├──uploads(all the media uploaded by user)
│   ├── css
│   │   ├── **/*.css
│   ├── images
│   ├── js
│   │   ├── **/*.js
│   └── partials/template
├── README.md
├── entrypoint_django
├── Dockerfile
├── docker_compose.yaml
├── Pipfile
├── manage.py
└── .gitignore
```

## Dev Setup


> NOTE : Please do not remove the environment the variables already present inside the env file

```bash
  #To start the containers
  docker-compose up
  #Stop containers in diff terminal than docker
  docker-compose --volumes down
  #build docker images 
  docker-compose up --build #if there are changes in installed deps
  #faster builds
  COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build
  #windows
  set "COMPOSE_DOCKER_CLI_BUILD=1" & set "DOCKER_BUILDKIT=1" & docker-compose build
  # or to make this permanent add following to docker daemon /etc/docker/daemon.json
  { "features": { "buildkit": true } }
```

**Helpers:**
1. Remove dangling images: `docker rmi $(docker images -f dangling=true -q ) -f`
2. Remove all volumes: `docker volume rm $(docker volume ls -q)`


