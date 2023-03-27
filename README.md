# Docker-python-multiple-container

# Most uses command 

  docker ps
  docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
  docker-compose -f docker-compose.prod.yml down -v
  docker ps
  docker-compose -f docker-compose.prod.yml down -v
  docker-compose -f docker-compose.prod.yml up -d --build
  docker
  docker ps
  docker ps -a
  docker-compose -f docker-compose.prod.yml logs -f
  docker-compose -f docker-compose.prod.yml down -v
  docker-compose -f docker-compose.prod.yml up -d --build
  docker-compose -f docker-compose.prod.yml logs -f
  docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
  docker ps

# Running the application 
  
  docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
  
# Check the logs
  
  docker-compose -f docker-compose.prod.yml logs -f
  
# Build the images

  docker-compose -f docker-compose.prod.yml up -d --build
  
# check
