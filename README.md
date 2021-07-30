## Task
### Social Network

Object of this task is to create a simple REST API. You can use one framework from this list
(Django Rest Framework, Flask or FastAPI) and all libraries which you are prefer to use with
this frameworks.

##### Basic models:
- User
- Post (always made by a user)

##### Basic Features:
- user signup
- user login
- post creation
- post like
- post unlike
- analytics about how many likes was made. Example url
/api/analitics/?date_from=2020-02-02&date_to=2020-02-15 . API should return analytics
aggregated by day.
- user activity an endpoint which will show when user was login last time and when he
mades a last request to the service.

##### Requirements:
- Implement token authentication (JWT is prefered)

##### Notes:
- ​Clean and usable REST API is important

- the project is not defined in detail, the candidate should use their best judgment for every
non-specified requirements (including chosen tech, third party apps, etc), however

- every decision must be explained and backed by arguments in the interview

- Result should be sent by providing a Git url. This is a mandatory requirement.


## Running locally
Clone the repository to your local machine and **go to the master branch**. With virtualenv enviroment activated install requirements:
```
$ pip3 install -r requirements.txt
```
Make and apply all migrations:
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
Use the following command to start the development server:
```
$ python3 manage.py runserver
```
## Available requests to the server:
##### GET:
> http://127.0.0.1:8000/api/analitic/likes/?date_from=YYYY-MM-DD&date_to=YYYY-MM-DD - analytics about how many likes was made (aggregated by day);

> http://127.0.0.1:8000/api/analitic/users/ - analytics about last activity of all users;

> http://127.0.0.1:8000/api/publications/ - shows all publications (*need to be authorized*)
 
> http://127.0.0.1:8000/api/users/ - shows all users (*need to be authorized*)
##### POST:
> http://127.0.0.1:8000/api/users/register/ - register new user

> http://127.0.0.1:8000/api/publications/create_publication/ - create new publications (*need to be authorized*)

##### PUT:
> http://127.0.0.1:8000/api/publications/<ID>/like/ - like publication (*need to be authorized*)
>>>>>>> 4f5833cc34674dc73ed2963e1fe29be79fe4d2e0
