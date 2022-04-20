docker run -d --rm \
    --name messenger-auth-server-container \
    -p 5433:5433 \
    -v $HOME/messenger-auth-server-workdir:/messenger-auth-server/messenger-auth-server-workdir \
    --net messenger-network \
    messenger-auth-server-image:latest
