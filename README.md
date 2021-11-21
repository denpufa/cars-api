# How to Use
- docker-compose up
- docker-compose exec web python manage.py makemigrations client
- docker-compose exec web python manage.py makemigrations car 
- docker-compose exec web python manage.py migrate

# Endpoints 
 - host/client -> POST create your client with "username","email","phone","password" 
 - host/auth -> POST your email as "username" and your "password" to get yout Token
 - User Authorization: Token 'your_token' on header
 - host/cars -> GET to get all cars
 - host/cars -> POST create a car with "plate_number"(string),"color"(string),"year"(number),"model"(String)
 - host/car/"plate_number" -> GET,UPDATE,DELETE a car
 - you can use limit and offset to paginate if you want

# Throttling
 - anounnimous request without token 10/day
 - users request 10000/day
 



 
