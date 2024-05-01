### Create docker account

### signin docker account

### Create dockerfile name as Dockerfile 

```bash
    docker images -display all docker image
```
```bash
    docker build -t "image_name" .
            or
    docker build -t my-image:latest .
```
### run locally
```bash
    docker run imagename

```

### Deploy to azure steps

#### Create one azure container registery

#### Login your container registery using below command in your terminal
```bash
    docker login "your ACR name" ex.(companynamegen.azurecr.io)
```
#### enable access token 
```bash
    copy username and password
```
#### Push 
```bash
    1 docker tag myapp companynamegen.azurecr.io/images
    2 docker push companynamegen.azurecr.io/images
    it will push our images to azure
```
#### create webapp using azure appservices

select  container while creating webapp service where it will suggest out docker image. once you click everything you can click review and create it will take few min to deploy. once its deploy you can access you application by clicking the azure url





