
This project uses SQLALCHEMY ORM with POSTGRESQL with flask FOR PERFORMING CRUD Operations

# Set the ENV variables:

$ export FLASK_ENV=development

$ export DATABASE_URL= postgres://name:password@houst:port/crud_api_db

$ export JWT_SECRET_KEY = hhgaghhgsdhdhdd

$ createdb crud_api_db

$ python manage.py db init

$ python manage.py db migrate


# Installations and Run the app:

pipenv shell

python run.py



# API's:

# Purpose: Create a Book in the DB

POST : http://127.0.0.1:5000/api/v1/books/


# Body:

{
    "authors": "Raghu",
    "country": "USA",
    "id": 12,
    "isbn": "456-987-9876",
    "name": "Men are from Mars",
    "pages": "128",
    "publisher": "TATA",
    "release_date": "12/06/2012"
}

# RES:

{
  "data": {
    "authors": "Raghu",
    "country": "USA",
    "id": 12,
    "isbn": "456-987-9876",
    "name": "Men are from Mars",
    "pages": "128",
    "publisher": "TATA",
    "release_date": "12/06/2012"
  },
  "status": "Success",
  "status_code": 201
}

# Purpose: Update a existing Book in the DB

PUT/Update : http://127.0.0.1:5000/api/v1/books/6


# BODY:

{"authors": "Raghu", "country": "USA", "created_at": "2019-06-29T08:12:24.075104+00:00", "id": 6, "isbn": "456-987-9876", "modified_at": "2019-06-29T08:12:24.075104+00:00", "name": "Men are from Mars", "pages": "128", "publisher": "TATA_MCGRawHill", "release_date": "12/06/2012"}

# RES:

{
  "authors": "Raghu",
  "country": "USA",
  "created_at": "2019-06-29T07:28:24.193180+00:00",
  "id": 1,
  "isbn": "456-987-9876",
  "modified_at": "2019-06-29T12:53:34.390472+00:00",
  "name": "Men are from Mars",
  "pages": "128",
  "publisher": "TATA_MCGRawHill",
  "release_date": "12/06/2012"
}


# Purpose: Delete a existing Book from DB

DELETE: http://127.0.0.1:5000/api/v1/books/6


# RES:
{
  "data": {
    "message": "deleted"
  },
  "status": "Success",
  "status_code": 201
}


# Purpose: Get all books with meta data from DB

GET http://127.0.0.1:5000/api/v1/books/


# RES:

[
  {
    "authors": "Raghu",
    "country": "USA",
    "created_at": "2019-06-29T07:46:06.093676+00:00",
    "id": 3,
    "isbn": "456-987-9876",
    "modified_at": "2019-06-29T07:46:06.093676+00:00",
    "name": "Success is never ending",
    "pages": "128",
    "publisher": "TATA",
    "release_date": "12/06/2012"
  },
  {
    "authors": "Raghu",
    "country": "USA",
    "created_at": "2019-06-29T07:47:16.535375+00:00",
    "id": 4,
    "isbn": "456-987-9876",
    "modified_at": "2019-06-29T07:47:16.535375+00:00",
    "name": "Walk the Talk",
    "pages": "128",
    "publisher": "TATA",
    "release_date": "12/06/2012"
  },
  {
    "authors": "Raghu",
    "country": "USA",
    "created_at": "2019-06-29T08:14:47.397114+00:00",
    "id": 8,
    "isbn": "456-987-9876",
    "modified_at": "2019-06-29T08:14:47.397114+00:00",
    "name": "Men are from Mars",
    "pages": "128",
    "publisher": "TATA",
    "release_date": "12/06/2012"
  },
  {
    "authors": "Raghu",
    "country": "USA",
    "created_at": "2019-06-29T08:19:28.195475+00:00",
    "id": 9,
    "isbn": "456-987-9876",
    "modified_at": "2019-06-29T08:19:28.195475+00:00",
    "name": "Men are from Mars",
    "pages": "128",
    "publisher": "TATA",
    "release_date": "12/06/2012"
  },
  {
    "authors": "Raghu",
    "country": "USA",
    "created_at": "2019-06-29T12:15:31.670362+00:00",
    "id": 10,
    "isbn": "456-987-9876",
    "modified_at": "2019-06-29T12:15:31.670362+00:00",
    "name": "Men are from Mars",
    "pages": "128",
    "publisher": "TATA",
    "release_date": "12/06/2012"
  },
  {
    "authors": "Raghu",
    "country": "USA",
    "created_at": "2019-06-29T12:20:49.665446+00:00",
    "id": 11,
    "isbn": "456-987-9876",
    "modified_at": "2019-06-29T12:20:49.665446+00:00",
    "name": "Men are from Mars",
    "pages": "128",
    "publisher": "TATA",
    "release_date": "12/06/2012"
  },
  {
    "authors": "Raghu",
    "country": "USA",
    "created_at": "2019-06-29T07:28:24.193180+00:00",
    "id": 1,
    "isbn": "456-987-9876",
    "modified_at": "2019-06-29T12:53:34.390472+00:00",
    "name": "Men are from Mars",
    "pages": "128",
    "publisher": "TATA_MCGRawHill",
    "release_date": "12/06/2012"
  },
  {
    "authors": "Raghu",
    "country": "USA",
    "created_at": "2019-06-29T12:54:25.687126+00:00",
    "id": 12,
    "isbn": "456-987-9876",
    "modified_at": "2019-06-29T12:54:25.687126+00:00",
    "name": "Men are from Mars",
    "pages": "128",
    "publisher": "TATA",
    "release_date": "12/06/2012"
  }
]


# Purpose:Hook to external Ice And Fire API and process the data to extract the relevant json objects

GET http://127.0.0.1:5000/external-books?name=A Game of Thrones

# RES:

{
  "data": [
    {
      "authors": [
        "George R. R. Martin"
      ],
      "country": "United States",
      "isbn": "978-0553103540",
      "name": "A Game of Thrones",
      "number_of_pages": 694,
      "publisher": "Bantam Books",
      "release_date": "1996-08-01T00:00:00"
    }
  ],
  "status": "Success",
  "status_code": 200
}

# Purpose:Gracefully handle exceptions

GET http://127.0.0.1:5000/external-books?name=A Game of Monkey

# RES:

{
  "data": [],
  "status": "Success",
  "status_code": 200
}

# Purpose:Get a single book by id

GET http://127.0.0.1:5000/api/v1/books/8

# RES:

{
  "data": {
    "authors": "Raghu",
    "country": "USA",
    "created_at": "2019-06-29T08:14:47.397114+00:00",
    "id": 8,
    "isbn": "456-987-9876",
    "modified_at": "2019-06-29T08:14:47.397114+00:00",
    "name": "Men are from Mars",
    "pages": "128",
    "publisher": "TATA",
    "release_date": "12/06/2012"
  },
  "status": "Success",
  "status_code": 201
}

# DB:

The DB table name called user is created

the table has below columns:

CREATE TABLE crud_api_db.users(
   id INTEGER PRIMARY KEY,
   name VARCHAR (128) NOT NULL,
   isbn VARCHAR (128) NOT NULL,
   authors VARCHAR (128) NOT NULL,
   country VARCHAR (128) NOT NULL,
   pages VARCHAR (128) NOT NULL,
   publisher VARCHAR (128) NOT NULL,
   release_date VARCHAR (128) NOT NULL,
   created_at TIMESTAMP,
   modified_at TIMESTAMP
);


# To Run test coverage:

py.test --cov=src --cov-config .coveragerc
