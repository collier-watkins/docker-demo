In this example:

We follow a similar pattern to the first Heimdall example, where we simply pull an image from the docker hub, build a container from that image, and run it. The only difference here is that we have a ton of environment variables.

We are also linking the container's interior directory `/data` to a directory here on the host filesystem, so we get constant, persistent access to the files this container makes/uses on our host system.

WARNING: Edit the `docker-compose.yml` file so the directory referenced on the host system is correct for your system. That directory path is for my computer, not necessarily yours.
