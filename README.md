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

After the course you will be able to:

- write and execute a Python program or Python-notebook script/report
- read/write data stored in standard tabular/hierarchical formats
- perform data manipulation operations (table filtering, merging, wide/long conversion)
- visualise histograms, scatter plots, etc.
- execute several machine learning algorithms
- explain the relevance of data stewardship for scientific research
- properly handle research data during the complete data life cycle (planning research, collecting data, processing & analyzing data, preserving data, giving access to data, re-using data)
- apply the FAIR principles (Findable, Accessible, Interoperable, Reusable)

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
    - [Data manipulation: NumPy](06_np/np.ipynb)&nbsp;&nbsp;[[Exercises](06_np/np_exercises.ipynb)]
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :orange_book: **Assignment A**: primary deadline, 17:00
- `(07)` Mar. 20th:
    - Data manipulation
- `(08)` Apr. 3rd:
    - Data visualisation
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :green_book: **Assignment B**: primary deadline, 17:00
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :blue_book: **Assignment C**: start
- `(09)` Apr. 17th:
    - Relational databases and SQL language
- `(10)` Apr. 24th
    - Relational databases and SQL language
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :books: **Group Assignment**: start
- `(11)` May 1st:
    - Python SQL Toolkit and Object Relational Mapper (SQLAlchemy)
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :blue_book: **Assignment C**: primary deadline, 17:00
- `(12)` May 8th:
    - General Q&A and group assignment Q&A, programming practice
- `(13)` May 15th:
    - Machine learning libraries (examples)
- `(14)` May 22nd:
    - FAIR & data stewardship
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :pencil: **Data stewardship quiz**: start
- `(--)` May 29th:
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :books: **Group Assignment**: deadline (17:00)
- `(--)` June 5th
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :office: **Exam**
- `(--)` June 12th
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :orange_book: :green_book: :blue_book: **Assignments A, B, C**: secondary deadline, 17:00
    - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :pencil: **Data stewardship quiz**: deadline, 17:00
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
