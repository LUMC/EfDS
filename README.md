# Essentials for Data Science (2022/2023)

A course of [Statistics and Data Science master](https://www.universiteitleiden.nl/en/education/study-programmes/master/statistics--data-science), Leiden University.

:warning: :warning: :warning: Prepare your laptop as described in the [installation section](#installation) below.

## Teachers

- Szymon M. Kiełbasa [[LUMC/BDS](https://www.lumc.nl/over-het-lumc/afdelingen/biomedical-data-sciences/)], coordinator, `smkielbasa@lumc.nl`
- Ramin Monajemi [[LUMC/BDS](https://www.lumc.nl/over-het-lumc/afdelingen/biomedical-data-sciences/)], `rmonajemi@lumc.nl`
- Mo Arkani [[LUMC/BDS](https://www.lumc.nl/over-het-lumc/afdelingen/biomedical-data-sciences/)], `markani@lumc.nl`

## Overview

[Python](https://www.python.org/) and [SQL](https://www.w3schools.com/sql/) belong to the most frequently used programming languages of data science.

After this course the student shall be able to program simple reproducible analyses in Python.
An analysis will consist of data reading, cleaning, simple modelling, and reporting steps.
The state-of-the-art Python-specific data manipulation/visualization ([pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/)) and data science libraries will be discussed.

The students will be requested to write Python programs of growing complexity (from basic coding examples to fitting a machine learning model).

Fundamentals of the relational databases and of the SQL language will be discussed in a context of an example database ([SQLite](https://sqlite.org/index.html)).
We will practice database usage through direct SQL statements and through high-level, object-oriented Python library ([SQLAlchemy](https://www.sqlalchemy.org/)).

Moreover, the students will be requested to work in groups and practice shared code development ([git](https://git-scm.com/), [GitHub](https://github.com/)).

Finally, relevance of data stewardship and [FAIR principles](https://en.wikipedia.org/wiki/FAIR_data) (Findable, Accessible, Interoperable, Reusable) will be discussed.

## Course Objectives

During the course you will practice writing [Python](https://www.python.org/) code. After the course you will be able to:

- :writing_hand: use Python collections (`list`, `tuple`, `set`, `dict`)
- :writing_hand: use Python flow control statements (`if`, `for`, `while`, exceptions), context managers (`with`) and define user functions
- :no_entry_sign: understand Python classes (instance variables, methods, inheritance)
- :writing_hand: use Python standard libraries (reading/writing files in different formats; `math`, `statistics`, `random`)
- :writing_hand: use common data science libraries ([NumPy](https://numpy.org/), [pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/))
- :no_entry_sign: understand relational databases and use [SQL](https://www.w3schools.com/sql/) to create, query, update a database
- :no_entry_sign: understand basics of [SQLAlchemy](https://www.sqlalchemy.org/) for Python object-oriented database access
- :writing_hand: understand how to execute several machine learning algorithms
- :no_entry_sign: use [git](https://git-scm.com/) and [GitHub](https://github.com/) for individual and collaborative code development
- :no_entry_sign: explain the relevance of data stewardship and [FAIR principles](https://en.wikipedia.org/wiki/FAIR_data) for scientific research

## Time/location

Check the **Essentials for Data Science** course (`4433EDASCY`) at https://rooster.universiteitleiden.nl/schedule.

## Schedule

- `(01)` Feb. 6th, 2023:
    - General course introduction
    - [Git/GitHub introduction](01_python/git_github_intro.md)
    - Python notebooks
    - [Python basic](01_python/python_basic.ipynb)
    - [Memory organization](01_python/memory_organization.md)
    - [Python lists and tuples](01_python/python_lists_tuples.ipynb)
- `(02)` Feb. 13th:
    - [Python sets and dictionaries](02_python/python_sets_dicts.ipynb)
    - [Git/GitHub practice](02_python/git_practice.md)
- `(03)` Feb. 20th:
    - [Python flow control and user functions](03_python/python_flow_control.ipynb)
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :orange_book: **Assignment A**: start
- `(04)` Feb. 27th:
    - [Python object oriented programming](04_python/python_oop.ipynb)
    - [Git/GitHub assignment preparation](04_python/git_assignment.md)
- `(05)` Mar. 6th:
    - [Python standard libraries and scripts](05_python/python_rest.ipynb)
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :green_book: **Assignment B**: start
- `(06)` Mar. 13th:
    - [Data manipulation:NumPy](06_np/np.ipynb)&nbsp;&nbsp;[[Exercises](06_np/np_exercises.ipynb)]&nbsp;&nbsp;[[Solutions](06_np/np_exercises_solutions.ipynb)] 
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :orange_book: **Assignment A**: primary deadline, 17:00
- `(07)` Mar. 20th:
    - [Data manipulation:pandas](07_pd/pd.ipynb)&nbsp;&nbsp;[[Exercises](07_pd/pd_exercises.ipynb)]&nbsp;&nbsp;[[Solutions](07_pd/pd_exercises_solutions.ipynb)]
- `(08)` Apr. 3rd:
    - [Data visualisation](08_dv/dv.ipynb)&nbsp;&nbsp;[[Exercises](08_dv/dv_exercises.ipynb)]
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :green_book: **Assignment B**: primary deadline, 23:59
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :blue_book: **Assignment C**: start
- `(09)` Apr. 17th:
    - Relational databases:
        - [Database, database models and DataBase Management Systems](09_sql/db_database.md)
        - [Database related terms](09_sql/db_related.md)
        - [Relation/table](09_sql/db_table.md)
        - [Keys, primary keys, prime attributes](09_sql/db_keys.md)
    - SQL language:
        - [Downloading and connecting to the example database](09_sql/connect_to_database.ipynb)
        - [Querying and selecting data](09_sql/SELECT_basic.ipynb) (`SELECT`, `LIMIT`, `AS`, `ORDER`, `DISTINCT`, `WHERE`, `IN`, `BETWEEN`, `LIKE`) [[Exercises](09_sql/SELECT_basic.exercises.ipynb)]
        - [Grouping and summarising](09_sql//SELECT_groups.ipynb) (`GROUP BY`, `HAVING`, `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, `GROUP_CONCAT`) [[Exercises](09_sql/SELECT_groups.exercises.ipynb)]
- `(10)` Apr. 24th
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
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :books: **Group Assignment**: start
- `(11)` May 1st:
    - [Python SQL Toolkit and Object Relational Mapper (SQLAlchemy)](11_sql/orm_practice.ipynb)
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :blue_book: **Assignment C**: primary deadline, 23:59
- `(12)` May 8th:
    - [Git branching and merging](12_git/git_branching_merging.md)
    - General Q&A and group assignment Q&A, programming practice
- `(13)` May 15th:
    - Machine learning libraries (examples)
- `(14)` May 22nd:
    - FAIR & data stewardship
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :pencil: **Data stewardship quiz**: start
- `(--)` June 1st:
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :books: **Group Assignment**: deadline, 23:59
- `(--)` June 5th
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :office: **Exam**
- `(--)` June 12th
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :orange_book: :green_book: :blue_book: **Assignments A, B, C**: secondary deadline, 23:59
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :pencil: **Data stewardship quiz**: deadline, 23:59
- `(--)` June 26th
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :office: **Retake**

## Grading

- Components of the final grade:
  - **Assignments A, B, C**:
    - Assignments A, B and C are separately graded.
    - The grade range is 1-10 but when the primary deadline is not met then the maximum grade is 8.
    - The mean grade of Assignments A, B and C is calculated and then rounded to 0.2 steps (e.g. ...7.6, 7.8, 8.0...).
    - To pass the course, the Assignments A, B, C rounded mean grade must be greater than 5.5.
    - The Assignments A, B, C rounded mean grade has weight=3 in the final grade.
  - **Group Assignment (weight 3)**:
    - The grade range is 1-10, rounded to 0.2 steps.
    - To pass the course, the group assignment rounded grade must be greater than 5.5.
    - The group assignment rounded grade has weight=3 in the final grade.
  - **Data stewardship quiz**:
    - To pass the course, the quiz needs to be solved with the PASS result.
    - The quiz grade is not part of the final grade formula.
  - **Exam/Retake (weight 4)**:
    - The grade range is 1-10, rounded to 0.2 steps.
    - To pass the course, the exam/retake grade must be greater than 5.5.
    - The exam/retake grade has weight=4 in the final grade.
    - The exam will cover the course objectives marked with :writing_hand:.
    - The exam will not cover the course objectives marked with :no_entry_sign: - these objectives are evaluated in the group assignment and the quiz.
- Final grade:
    - The final grade is calculated as a weighted mean of the component grades.
    - To pass the course, the final grade needs to be greater or equal 6.0.

## Installation

For the course you will need to bring a laptop with properly installed Python and Jupyter Notebook development environment.  
Install (in the order listed below):

- **Python** (version >= 3.?.?): Follow the download instructions at https://www.python.org/.
- **pip**: The Python Package Installer. It should already be installed during Python installation. If that is not the case, follow https://pip.pypa.io/en/stable/installation/.
- **Jupyter Notebook**: A (web) application for creating and sharing computational documents. Follow the instructions at https://jupyter.org/.

Moreover, you will need:

- **git**: Free and open source distributed version control system. Follow the *Downloads* instructions provided at https://git-scm.com/. Additional GUI (graphical) clients will not be used during the course but might be useful.
