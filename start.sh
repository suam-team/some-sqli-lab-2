#!/bin/sh

rm -rf /app/mysql
mkdir /app/mysql
mkdir /app/mysql/data

sed "s/_USER_/$(whoami)/g" my.cnf.tmpl > my.cnf

mysql_install_db --defaults-file=/app/my.cnf
mysqld --defaults-file=/app/my.cnf &

while ! mysqladmin -S /app/mysql/mysql.sock ping --silent; do
    sleep 1
done

sed "s/_FLAG_/${FLAG}/g" lab.sql.tmpl > lab.sql

mysql -S /app/mysql/mysql.sock -uroot < lab.sql

gunicorn app:app -b :$PORT

