# Starting this App

```bash
# In a vagrant en you should create a folder in another path
mkdir /home/vagrant/mysql
cd /vagrant/data
ln -s /home/vagrant/mysql .
# Start the Flask app (Open localhost:5000/companies/)
cd /vagrant
docker-compose -f docker-compose-vagrant.yml up -d
# Populate the DB

docker-compose -f docker-compose-vagrant.yml run --rm -v ${PWD}:/opt/src -w /opt/src mysql-2 bash

mysql -ucompanies -h172.18.0.3 -p  # write exit
mysql -ucompanies -h172.18.0.3 -p companies < ./db/creation.sql
```