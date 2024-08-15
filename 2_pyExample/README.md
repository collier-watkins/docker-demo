In this example: Build your own image and container

Use the bash commands in commands.txt or run `docker compose up` to use docker compose syntax. Either way, the same thing is done:

1) The steps within the Dockerfile to build the image are followed, which includes copying all the files within this directory into the image, and more config steps.
2) A container is built and run based on this image. The container will exist as long as the CMD step (last command in the Dockerfile) is running. When that command completes, the container will die.
