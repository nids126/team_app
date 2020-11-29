#!/bin/bash
UP=$(/etc/init.d/mysql status | grep running | grep -v not | wc -l);
if [ "$UP" -ne 1 ];
then
        echo "MySQL is down.";
        sudo service mysql start
else
        echo "Enter your mysql username"
        read username
        mysql -u $username -p < initialize.sql
        echo "Database set up done successfully"
fi
