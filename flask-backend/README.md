# Starting this App

```bash
# In a vagrant en you should create a folder in another path
mkdir /home/vagrant/mysql
cd /vagrant/data
ln -s /home/vagrant/mysql .
# Start the Flask app (Open localhost:5000/companies/)
cd /vagrant
docker-compose up -d
# Populate the DB
docker-compose run --rm -v ${PWD}:/opt/src -w /opt/src mysql bash
# In the container shell. The password is password D:
mysql -ucompanies -hmysql -p  # write exit
mysql -ucompanies -hmysql -p companies < ./db/creation.sql
```

# Using with buildah and Podman

```bash
./podman-deploy.sh
podman run --rm -ti -v ${PWD}:/opt/src -w /opt/src --network=companies_network  mysql bash
mysql -ucompanies -hmysql -p
mysql -ucompanies -hmysql -p companies < ./db/creation.sql
```

# Using podman-compose

podman-compose up -d
sudo podman run -ti --network host --rm -v ${PWD}:/opt -w /opt docker.io/mariadb:10.1 bash
mysql -ucompanies -h127.0.0.1 -p
mysql -ucompanies -h127.0.0.1 -p companies < ./db/creation.sql