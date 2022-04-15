docker run -d --rm \
    --name messenger-users-db-container \
    -p 5432:5432 \
    -v $HOME/messenger-users-db-data:/var/lib/postgresql/data \
    --net messenger-network \
    messenger-users-db-image:latest
