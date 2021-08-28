# Docker for development environments

Currently, Docker is the most difussed container technology. It's possible you are thinking about kubernetes and the decision about don't use Docker as a Runtime.
Well, it's true. But Docker will be compatible with K8.

So, we can continue using Docker for another things like Development.

# Some concepts

**Image:** It can be defined like a "hard-coded" file system. It can be used like a "template" by the containers.

**Container:** It's a low level set of components that use some Linux features to run a service. Another view is a container is an instance of a image (it has RAM, CPU and storage). Check this [article](https://platform.sh/blog/2020/the-container-is-a-lie/).

**Differences between VM's and Containers:** From this [blog article](https://monadical.com/posts/everyone-should-know-about-docker.html).

"The main difference between Docker and virtualization is the different low-level approach to application containment. With a virtual machine, an isolated pool of “virtual” computational resources are divided out through a special kind of software called a hypervisor. (Examples of hypervisor technologies include VMWare, Xen, and VirtualBox.) By contrast, Docker uses un-virtualized resources shared with its host system, but uses cgroups and kernel namespaces to effectively present a fake “isolated” system to each application within. Practically speaking, Docker is able to more efficiently share system resources across applications and their host, because it doesn’t have the added overhead of passing all resource accesses through a hypervisor process."

# Docker compose

Docker-compose is a technology for running multi container docker applications. You can use it for deploy stacks in any place (usually a server).
But this is useful for helping in the development stuff.

# Basic docker and docker-compose commands

```bash
# Pull an image
docker pull <image>
# Run container (e.g. nginx)
docker run -ti --name -d -p 8082:80 -v $PWD:/opt/app nginx
# Show logs
docker logs nginx 
# List containers
docker ps
# Start an stack
docker-compose up
# Start a stack in bg
docker-compose up -d
# Stop and delete containers
docker-compose down
# List services
docker-compose ps
# Run some command in a service (starting the service)
docker-compose run --rm container-name command
# If the service is up. Run in an existing container
docker-compose exec container-name command
```

# Basic structure of a compose file (based on docker compose [overview ](https://docs.docker.com/compose/))

```yaml
version: "3.9"  # optional since v1.27.0
services:   # Block for services definition
  web:
    build: .      # If the image use some Dockerfile to create the image
    ports:
      - "5000:5000"          # Port mapping section host:container
    volumes:
      - .:/code       # If you wanna use some map some host folder in the container
  redis:
    image: redis      # Another service
```

# Steps to create a dev environment using Docker Compose

* Check what services your application have. ([Example](https://github.com/afreydev/manylinux-web))
* Review your application use environment variable to get settings (usernames, passwords, endpoints, hosts, etc).
* Review you can use an existing image to dockerize your services.
* Identify what is the default exec command for your services. (Check [CMD](https://docs.docker.com/engine/reference/builder/#cmd) and [ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint))
* Create or extend images for your custom services using Dockerfiles. (Using [docker](https://docs.docker.com/engine/reference/builder/))
* Collect the config files your backing services uses. Check you cannot use env variables to config them.
* Write your docker-compose file mapping env vars and config files in each required service.

# Notes:

* A exec form in docker is: entrypoint + cmd. (An entrypoint [example](https://github.com/Monadical-SAS/oddslingers.poker/blob/main/bin/entrypoint.sh))
* [https://12factor.net/](https://12factor.net/)
