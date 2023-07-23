# Docker-python-multiple-container

### Most uses command 

  1. docker ps
  2. docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
  3. docker-compose -f docker-compose.prod.yml down -v
  4. docker ps
  5. docker-compose -f docker-compose.prod.yml down -v
  6. docker-compose -f docker-compose.prod.yml up -d --build
  7. docker
  8. docker ps
  9. docker ps -a
  10. docker-compose -f docker-compose.prod.yml logs -f
  11. docker-compose -f docker-compose.prod.yml down -v
  12. docker-compose -f docker-compose.prod.yml up -d --build
  13. docker-compose -f docker-compose.prod.yml logs -f
  14. docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
  15. docker ps

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

### down the images
  ```shell
  docker-compose -f docker-compose.prod.yml down 
  ```
### releated link

* https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/#nginx
* https://www.tinystacks.com/blog-post/flask-crud-api-with-postgres/
