# Essentials for Data Science (2025/2026)

A master-level course, part of [Statistics and Data Science master](https://www.universiteitleiden.nl/en/education/study-programmes/master/statistics--data-science), Leiden University.

:warning: :warning: :warning: Prepare your laptop as described in the [installation section](#installation) below.  
:warning: :warning: :warning: Charge your laptop battery before the lecture. The currently assigned lecture room does not provide enough power sockets, so please bring your laptops with enough battery charge for a 4h session.


## Teachers

- Szymon M. Kiełbasa [[LUMC/BDS](https://www.lumc.nl/over-het-lumc/afdelingen/biomedical-data-sciences/)], coordinator, `smkielbasa@lumc.nl`
- Ramin Monajemi [[LUMC/BDS](https://www.lumc.nl/over-het-lumc/afdelingen/biomedical-data-sciences/)]
- Serena Della Corte

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

1. :writing_hand: Create Python code using collections (`list`, `tuple`, `set`, `dict`), flow control statements (`if`, `for`, `while`, exceptions), context managers (`with`).
2. :writing_hand: Develop user functions.
3. :writing_hand: Use Python classes (instance variables, methods, inheritance).
4. :writing_hand: Combine functions from the Python standard libraries (reading/writing files in different formats; `math`, `statistics`, `random`) into own code.
5. :writing_hand: Analyse example data with common data science libraries ([NumPy](https://numpy.org/), [pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/)).
6. Understand relational databases and apply the SQL language to create, query, and update a relational database:
    - :writing_hand: Understand ideas behind relational databases and elementary SQL.
    - :no_entry_sign: Use SQL to create, query, update a database.
7. :writing_hand: Practice Python programming through running several machine learning algorithms.
8. Practice individual and collaborative code development by using [git](https://git-scm.com/) and [GitHub](https://github.com/):
    - :writing_hand: Understand ideas behind project versioning.
    - :no_entry_sign: Use git and GitHub for individual and collaborative code development.

## Timetable

The primary source for lecture, exam and retake dates/locations is **Essentials for Data Science** course `4433ESSDSY` schedule at https://rooster.universiteitleiden.nl/. The dates given below are manually copied and may contain mistakes. Always check the official schedule. The order/content of the future lectures as well as the submission dates of the assignments might be adjusted.

The schedule:

- `(01)` Feb. 2nd, 2026 (Szymon/Ramin+Serena):
  - General course introduction
  - Python notebooks
  - [Python basic](01_python/python_basic.ipynb)
  - [Python lists and tuples](01_python/python_lists_tuples.ipynb)
  - [Memory organization](01_python/memory_organization.md)
  - [Git/GitHub: introduction](01_python/git_github_intro.md)
- `(02)` Feb. 16th (Szymon/Serena):
  - [Python sets and dictionaries](02_python/python_sets_dicts.ipynb)
  - [Git/GitHub: practice](02_python/git_practice.md)
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :orange_book: **Assignment A** (not graded): start
- `(03)` Feb. 23rd (Szymon/Serena):
  - [Python flow control and user functions](03_python/python_flow_control.ipynb)
  - [Git/GitHub: how to deliver assignments](03_python/git_assignment.md)
- `(04)` Mar. 02nd (Szymon/Serena):
  - [Python object oriented programming](04_python/python_oop.ipynb)
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :orange_book: **Assignment A**: discussion of solutions
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :green_book: **Assignment B** (not graded): start
- `(05)` Mar. 09th (Szymon/Serena):
  - [Python standard libraries and scripts](05_python/python_rest.ipynb)
- `(06)` Mar. 16th (Ramin/Serena):
  - [Data manipulation: NumPy](06_np/np.ipynb)
- `(07)` Mar. 23rd (Ramin/Serena):
  - [Data manipulation: pandas](07_pd/pd.ipynb) 
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :green_book: **Assignment B**: discussion of solutions
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :blue_book: **Assignment C** (graded): start
- `(08)` Mar. 30th (Ramin/Serena):
  - [Data visualisation](08_dv/dv.ipynb)
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :books: **Group Assignment**: create groups
- `(09)` Apr. 13th (Szymon/Serena):
  - Relational databases:
    - [Database, database models and DataBase Management Systems](09_sql/db_database.md)
    - [Database related terms](09_sql/db_related.md)
    - [Relation/table](09_sql/db_table.md)
    - [Keys, primary keys, prime attributes](09_sql/db_keys.md)
  - SQL language:
    - [Downloading and connecting to the example database](09_sql/connect_to_database.ipynb)
    - [Querying and selecting data](09_sql/SELECT_basic.ipynb) (`SELECT`, `LIMIT`, `AS`, `ORDER`, `DISTINCT`, `WHERE`, `IN`, `BETWEEN`, `LIKE`) [[Exercises](09_sql/SELECT_basic.exercises.ipynb)]
    - [Grouping and summarising](09_sql//SELECT_groups.ipynb) (`GROUP BY`, `HAVING`, `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, `GROUP_CONCAT`) [[Exercises](09_sql/SELECT_groups.exercises.ipynb)]
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :blue_book: **Assignment C**: deadline (end-of-day)
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :books: **Group Assignment** (graded): start
- `(10)` Apr. 20th (Szymon/Serena):
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
- `(11)` May 04th (Szymon/Ramin):
  - [Git branching and merging](12_git/git_branching_merging.md)
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :blue_book: **Assignment C**: grades and feedback
- `(12)` May 11th (?/Serena):
  - [Machine Learning with sklearn](13_ml/lecture_13_ML.ipynb) [[Exercises](13_ml/Exercises_ML.ipynb)]
  - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :books: **Group Assignment**: deadline (end-of-day)
- `(13)` May 18th (?/Serena):
  - Exam information, Final Q&A
  - [Deep learning with Keras](13_ml/lecture_14_ML_ANN.ipynb) [[Exercises](13_ml/Exercise_ANN_regression.ipynb)]
- `(--)` June 01st:
  - :office: **Exam**
- `(--)` June 29th:
  - :office: **Retake**
- Extra materials (in case of interest):
  - [Python SQL Toolkit and Object Relational Mapper (SQLAlchemy)](11_sql/orm_practice.ipynb)

## Assessment method

Components of the final grade:

- **Assignment C (weight 0.1 in the final grade)**:
  - The grade range is 1-10 for submissions before the deadline. The grade range is 1-7 for submissions after the deadline but before the feedback moment. No submissions will be accepted later (then, the grade is 1).
- **Group Assignment (weight 0.2 in the final grade)**:
  - The grade range is 1-10 for submissions before the deadline. The grade range is 1-7 for submissions after the deadline but before the exam day. No submissions will be accepted later (then, the grade is 1).
  - To pass the course, the group assignment rounded grade must be greater than 5.5.
- **Exam/Retake (weight 0.7 in the final grade)**:
  - The exam consists of two parts: a pen-and-paper quiz and a programming part. **Usage of AI tools is prohibited during the pen-and-paper quiz part.**
  - The grade range is 1-10.
  - To pass the course, the exam/retake grade must be greater than 5.5.
  - The exam will cover the course objectives marked above with :writing_hand:, and will not cover the ones with :no_entry_sign: (these objectives are evaluated in the assignments).

The final grade:

- The final grade is calculated as a weighted mean of the grade components.
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
