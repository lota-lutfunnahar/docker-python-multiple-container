# Docker-python-multiple-container

### Most uses command 

```
    docker ps
    docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
    docker-compose -f docker-compose.prod.yml down -v
    docker ps
    docker-compose -f docker-compose.prod.yml down -v
    docker-compose -f docker-compose.prod.yml up -d --build
    docker ps
    docker ps -a
    docker-compose -f docker-compose.prod.yml logs -f
    docker-compose -f docker-compose.prod.yml down -v
    docker-compose -f docker-compose.prod.yml up -d --build
    docker-compose -f docker-compose.prod.yml logs -f
    docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
    docker ps
  ```

### Running the application 

  ```shell
  docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
  ```
  
### Check the logs

  ```shell
  docker-compose -f docker-compose.prod.yml logs -f
  ```
  
### Build the images
  ```shell
  docker-compose -f docker-compose.prod.yml up -d --build
  ```

### Down the images
  ```shell
  docker-compose -f docker-compose.prod.yml down 
  ```
### Releated link

* https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/#nginx
* https://www.tinystacks.com/blog-post/flask-crud-api-with-postgres/
