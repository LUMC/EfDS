# General databases knowledge

## Example

A grocery store network needs to have a shared database with products, sales, etc.  
Let's try to estimate the size a table keeping data about cash bills:

- there are more than 8 mln households in the Netherlands
- let's say, 1/4 of that are customers of one of the grocery store networks
- each household buys at least 10 products per week

Then, 20 mln records are generated per week, more than 1 bln records per year.  
These data are generated continuously by ca. 1000 stores and need to be reliably preserved.

## Database

A *database* is a *collection of data* with (context dependent) additional properties:

- Efficient organisation (with respect to a chosen database model).
- Access methods through a database query language and/or an application programming interface (providing ability to query and modify the data/data structure).
- Remote access.
- Secured access and protection of sensitive information.
- Fault tolerance.
- (Transparent) scalability.
- Concurrent access and transaction control.
- Support for different storage options (local filesystem or hosted from a cluster or cloud).

## Database models

A *database model* defines how data are organised in the database. The model defines allowed data types and representation of relationships between data. These choices define how the data are stored, how fast/easily they can be accessed, how they can be protected from unauthorized access, etc.

There are several [general types of database models](https://medium.com/practicum-by-yandex/database-models-ec4f0dba8985):
  - Relational (SQL),
  - Non-relational (NoSQL):
    - Hierarchical,
    - Network/Graph (non-hierarchical),
    - Key-Value

In the [relational model](https://en.wikipedia.org/wiki/Relational_model) (SQL) data are stored in form of multiple related regular tables. A normalisation process ([Edgar F. Codd](https://en.wikipedia.org/wiki/Edgar_F._Codd), 1970) describes how to optimally represent user data according to the relational model:
  - Data are clearly separated from applications.
  - There are very well established, highly (vertically) scalable, industry grade implementations of relational databases.
  - There is a well standardised language to access/modify data: SQL.
  - Access to data from object-oriented languages suffers from [*object-relational impedance mismatch*](https://en.wikipedia.org/wiki/Object%E2%80%93relational_impedance_mismatch). Using relational data models with object-oriented programming techniques requires complex intermediate layers.
  - Evolution of the database structure (horizontal scalability) is non-trivial.

[Object-oriented model](https://en.wikipedia.org/wiki/Object_database) (networks; 1990s) addresses above problems:
  - Interface is well but tightly connected to objects in an object-oriented application.
  - No well established general standards for querying such databases.
  - Some (simple) operations might be time-costly.
  - Smaller user community than for relational databases.

[Object-relational model](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) is a hybrid of an object-oriented model implemented on the top of a relational database. In this course we will use an [object-relational mapper](https://docs.sqlalchemy.org/en/14/orm/tutorial.html) provided by SQLAlchemy.

More info on database models can be found [here](https://www.lucidchart.com/pages/database-diagram/database-models).

*NoSQL* (approx. “not only SQL”, non-SQL) are databases not following the relational model. They are designed to store/retrieve unstructured (much less structured than relational) data.

In some sense, *git* can be seen as a [simple key-value store](https://www.kenneth-truyers.net/2016/10/13/git-nosql-database/#:~:text=Git%20is%20a*%20content%2Daddressable,to%20retrieve%20that%20content%20later.) database.

## DataBase Management Systems

A DataBase Management System (DBMS) is “software system that enables users to define, create, maintain and control access to the database”. For relational databases there are some very well known examples: SQLite, MySQL, PostgresSQL, Oracle Database, Microsoft Access. Several NoSQL examples: MongoDB, Redis, Apache CouchDB.

[Here](https://improvado.io/blog/top-25-best-database-management-software) a recent list of DBMSs.
