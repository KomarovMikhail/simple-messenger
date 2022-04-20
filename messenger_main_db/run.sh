docker run -d --rm \
    --name messenger-main-db-container \
    -p 5434:5432 \
    -v $HOME/messenger-main-db-data:/var/lib/postgresql/data \
    --net messenger-network \
    messenger-main-db-image:latest
