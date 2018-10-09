# Please follow the steps 
## Run the application on Centos 7
```
git clone git@gitlab.acirrustech.com:deployment/applicaiton_deployment.git
cd applicaiton_deployment
```



# Dockerize the application 
```
git clone git@gitlab.acirrustech.com:deployment/applicaiton_deployment.git
cd applicaiton_deployment
docker build acirrustech:acirrustech . 
docker run -dti -p 80:5000 acirrustech:acirrustech
```