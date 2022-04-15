docker run -d --rm \
    --name messenger-auth-server-container \
    -p 5433:5433 \
    --net messenger-network \
    messenger-auth-server-image:latest
