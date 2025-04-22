# Essentials for Data Science (2024/2025)

A master-level course, part of [Statistics and Data Science master](https://www.universiteitleiden.nl/en/education/study-programmes/master/statistics--data-science), Leiden University.

:warning: :warning: :warning: Prepare your laptop as described in the [installation section](#installation) below.  
:warning: :warning: :warning: Charge your laptop battery before the lecture.

## Teachers

- Szymon M. Kiełbasa [[LUMC/BDS](https://www.lumc.nl/over-het-lumc/afdelingen/biomedical-data-sciences/)], coordinator, `smkielbasa@lumc.nl`
- Ramin Monajemi [[LUMC/BDS](https://www.lumc.nl/over-het-lumc/afdelingen/biomedical-data-sciences/)]
- Daniela Grandón Silva [[LU/MATH](https://www.universiteitleiden.nl/en/staffmembers/daniela-grandon-silva#tab-1)]

## Admission requirements

Elementary statistical skills and elements of linear algebra.

## Description

The course offers a practical introduction to a few programming languages and tools currently used in data science:

- [Python](https://www.python.org/) is a general-purpose, high-level and easy to learn programming language. It provides a large number of data science libraries (e.g. machine learning, neural networks, data manipulation, data visualization).
- [SQL](https://www.w3schools.com/sql/) is a standard language used to create, query, update and manage relational databases. For example, such databases are used to store large tables with results of experiments.
- [Git](https://git-scm.com/) is a tool that allows to track changes in files during development of programs. It is the current standard for collaborative code development.

During the course you will develop Python programs of growing complexity.  
You will use state-of-the-art Python-specific data manipulation/visualization (e.g. [pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/)) data science libraries. You will apply several standard machine learning methods.  
After the course you will be able to program simple reproducible data analyses (consisting of data reading, cleaning, simple modelling, and reporting steps).  
You will also learn about fundamentals of the relational databases and of the SQL language, and you will practice this knowledge on an example database ([SQLite](https://sqlite.org/index.html)).

First, you will work alone and practice code development. You will submit your assignments through [GitHub](https://github.com/).  
Later, shared code development will be practiced in groups. The members of the group will be requested to use [git](https://git-scm.com/) to track changes in their code and to share their code with other students through GitHub.

## Course Objectives

During the course you will practice writing [Python](https://www.python.org/) and [SQL](https://www.w3schools.com/sql/) code.
After the course you will be able to:

1. :writing_hand: Use Python collections (`list`, `tuple`, `set`, `dict`).
1. :writing_hand: Use Python flow control statements (`if`, `for`, `while`, exceptions), context managers (`with`) and define user functions.
1. :writing_hand: Use Python standard libraries (reading/writing files in different formats; `math`, `statistics`, `random`).
1. :writing_hand: Use common data science libraries ([NumPy](https://numpy.org/), [pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/)).
1. :writing_hand: Use common machine learning libraries to apply simple regression, classification, clustering and dimensionality reduction methods.
1. :writing_hand: Understand Python classes (instance variables, methods, inheritance).
1. :writing_hand: Understand relational databases and elementary SQL.  
       :no_entry_sign: Use SQL to create, query, update a database.
1. :writing_hand: Understand ideas behind project versioning with [git](https://git-scm.com/) and [GitHub](https://github.com/).  
       :no_entry_sign: Use git and GitHub for individual and collaborative code development.

## Timetable

The schedule given below might change:

- The primary source for lecture, exam and retake dates/locations is **Essentials for Data Science** course `4433EDASCY` schedule at https://rooster.universiteitleiden.nl/. The dates on this page are manually copied and may lag behind. 
- **Important note:** The currently assigned lecture room does not provide individual power sockets, so please bring your laptops with enough battery charge for 4h session.
- The order/content of the future lectures might be adjusted.
- The dates of the assignments and the group assignment might be adjusted if order of the lectures changes.

The schedule:

- `(01)` Feb. 3rd, 2025 (Szymon/Ramin):
  - General course introduction
  - Python notebooks
  - [Python basic](01_python/python_basic.ipynb)
  - [Python lists and tuples](01_python/python_lists_tuples.ipynb)
  - [Memory organization](01_python/memory_organization.md)
  - [Git/GitHub: introduction](01_python/git_github_intro.md)
- `(02)` Feb. 10th (Szymon/Daniela+Ramin):
  - [Python sets and dictionaries](02_python/python_sets_dicts.ipynb)
  - [Git/GitHub: practice](02_python/git_practice.md)
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :orange_book: **Assignment A** (not graded): start
- `(03)` Feb. 17th (Szymon/Daniela):
  - [Python flow control and user functions](03_python/python_flow_control.ipynb)
  - [Git/GitHub: how to deliver assignments](03_python/git_assignment.md)
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :green_book: **Assignment B** (graded): start
- `(04)` Feb. 24th (Szymon/Ramin):
  - [Python object oriented programming](04_python/python_oop.ipynb)
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :orange_book: **Assignment A**: discussion of solutions
- `(05)` Mar. 3rd (Szymon/Daniela):
  - [Python standard libraries and scripts](05_python/python_rest.ipynb)
- `(06)` Mar. 10th (Ramin/Daniela):
  - [Data manipulation: NumPy](06_np/np.ipynb)
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :green_book: **Assignment B**: deadline (end-of-day)
- `(07)` Mar. 17th (Ramin/Daniela):
  - [Data manipulation: pandas](07_pd/pd.ipynb) 
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :blue_book: **Assignment C** (graded): start
- `(08)` Mar. 31st (Ramin):
  - [Data visualisation](08_dv/dv.ipynb) 
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :green_book: **Assignment B**: grades and feedback
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :books: **Group Assignment**: create groups
- `(09)` Apr. 7th (Szymon):
  - Relational databases:
    - [Database, database models and DataBase Management Systems](09_sql/db_database.md)
    - [Database related terms](09_sql/db_related.md)
    - [Relation/table](09_sql/db_table.md)
    - [Keys, primary keys, prime attributes](09_sql/db_keys.md)
  - SQL language:
    - [Downloading and connecting to the example database](09_sql/connect_to_database.ipynb)
    - [Querying and selecting data](09_sql/SELECT_basic.ipynb) (`SELECT`, `LIMIT`, `AS`, `ORDER`, `DISTINCT`, `WHERE`, `IN`, `BETWEEN`, `LIKE`) [[Exercises](09_sql/SELECT_basic.exercises.ipynb)]
    - [Grouping and summarising](09_sql//SELECT_groups.ipynb) (`GROUP BY`, `HAVING`, `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, `GROUP_CONCAT`) [[Exercises](09_sql/SELECT_groups.exercises.ipynb)]
- `(10)` Apr. 14th (Szymon):
  - Relational databases:
    - [Database design anomalies](10_sql/db_design_anomalies.md)
    - [Database normalisation](10_sql/db_normalisation.md)
    - [Types of relationships](10_sql/db_relationship_types.md)
    - [Column data types](10_sql/db_data_types.md)
    - [Advantages/disadvantages of relational databases](10_sql/db_reldb_adv_disadv.md)
  - SQL language:
    - [Modification statements](10_sql/UPDATE_INSERT_DELETE.ipynb) (`UPDATE`, `INSERT`, `DELETE`) [[Exercises](10_sql/UPDATE_INSERT_DELETE.exercises.ipynb)]
    - [Data definition language](10_sql/CREATE_TABLE.ipynb) (`CREATE TABLE`, `DROP TABLE`)
    - [Joining tables 1](10_sql/JOIN_basic.ipynb) (`INNER JOIN`, `LEFT JOIN`, `CREATE TEMP TABLE`) [[Exercises](10_sql/JOIN_basic.exercises.ipynb)]
    - [Joining tables 2](10_sql/JOIN_adv.ipynb) (`UNION`, `EXCEPT`, `INTERSECT`, self joins, `CROSS JOIN`, subqueries, `EXIST`) [[Exercises](10_sql/JOIN_adv.exercises.ipynb)]
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :books: **Group Assignment** (graded): start
- `(11)` Apr. 28th (Szymon):
  - [Git branching and merging](12_git/git_branching_merging.md)
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :blue_book: **Assignment C**: deadline (end-of-day)
- `(12)` May 12th (Daniela):
  - Machine learning libraries
- `(13)` May 19th (Daniela):
  - Machine learning libraries
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :blue_book: **Assignment C**: grades and feedback
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :books: **Group Assignment**: deadline (end-of-day)
- `(14)` May 26th (Szymon):
  - General Q&A, programming practice
- `(--)` June 13th:
  - :office: **Exam**
- `(--)` July 4th:
  - :office: **Retake**
- Extra materials (in case of interest):
  - [Python SQL Toolkit and Object Relational Mapper (SQLAlchemy)](11_sql/orm_practice.ipynb)

## Assessment method

Two homework assignments (each 10% of the final grade), a group assignment (20%), the final written exam (60%).

- Components of the final grade:
  - **Assignments B, C (total weight 0.2)**:
    - Assignments B and C are separately graded.
    - The grade range is 1-10 for submissions before the deadline. The grade range is 1-7 for submissions after the deadline but before the feedback moment. No submissions will be accepted later (the grade is 1).
    - To pass the course, the mean of Assignment B and C grades must be greater than 5.5.
    - The Assignments B, C rounded mean grade has weight=0.2 in the final grade.
  - **Group Assignment (weight 0.2)**:
    - The grade range is 1-10 for submissions before the deadline. The grade range is 1-7 for submissions after the deadline but before the exam day. No submissions will be accepted later (the grade is 1).
    - To pass the course, the group assignment rounded grade must be greater than 5.5.
    - The group assignment rounded grade has weight=0.2 in the final grade.
  - **Exam/Retake (weight 0.6)**:
    - **Usage of AI-based tools will be prohibited during the exam.**
    - The exam consists of two parts: a pen-and-paper quiz and a programming part.
    - The grade range is 1-10.
    - To pass the course, the exam/retake grade must be greater than 5.5.
    - The exam/retake grade has weight=0.6 in the final grade.
    - The exam will cover the course objectives marked with :writing_hand:.
    - The exam will not cover the course objectives marked with :no_entry_sign: - these objectives are evaluated in the group assignment.
- Final grade:
  - The final grade is calculated as a weighted mean of the component grades.
  - To pass the course, the final grade needs to be greater or equal 6.0.
  - The final grade is rounded to the nearest half integer.

## Installation

For the course you will need to bring a laptop with properly installed Python and a development environment.  
Install:

- **Microsoft Visual Code**: A free source-code editor made by Microsoft for Windows, Linux and MacOS. Follow the instructions at https://code.visualstudio.com/. Run the editor and install extensions for Python development (possibly, you will not need to install Python and pip separately).

You may additionally need to install:

- **Python** (version >= 3.9.?, optimally >= 3.12.?): Follow the download instructions at https://www.python.org/.
- **pip**: The Python Package Installer. It should already be installed during Python installation. If that is not the case, follow https://pip.pypa.io/en/stable/installation/.
- **git**: Free and open source distributed version control system. Follow the *Downloads* instructions provided at https://git-scm.com/. Visual Code extensions for git are recommended.
