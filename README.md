# docker-python-multiple-container

most uses command 

docker-compose up -d --build
docker-compose up -d
  636  docker ps
  637  docker-compose down -v
  638  docker ps
  639  docker-compose -f docker-compose.prod.yml up -d --build
  640  docker ps
  641  docker-compose down -v
  642  docker ps
  643  docker-compose down -v
  644  docker-compose -f docker-compose.prod.yml up -d --build
  645  docker ps
  646  docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
   docker-compose -f docker-compose.prod.yml logs -f
