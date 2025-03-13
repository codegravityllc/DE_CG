SELECT * FROM pg_stat_activity;

SELECT datname FROM pg_database;


SELECT datname FROM pg_database WHERE datname ='Cgdb';
SELECT usename, usecreatedb, usesuper FROM pg_user;
SHOW port;
SELECT version();
SELECT NOW();

