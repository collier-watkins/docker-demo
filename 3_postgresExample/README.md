In this example: Use multiple containers within a single stack.

Run `docker compose up`. This example combines the two previous examples. First, the python-server image is built, a container is built from that image and run just like the previous example.

Then, like the Heimdall example, images from Docker Hub are pulled and run with the correct environment variable configurations. We are using Postgres and PgAdmin images to make containers.

The python app written here is already prepared to connect to postgres and run some basic SQL commands when a user navigates to its flask webpage on `http://localhost:5000`.
