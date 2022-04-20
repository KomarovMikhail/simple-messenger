FROM postgres:latest

ENV POSTGRES_DB messenger-main-db
ENV POSTGRES_PASSWORD 0000
ENV PGDATA /var/lib/postgresql/data/pgdata

COPY init.sql /docker-entrypoint-initdb.d/
