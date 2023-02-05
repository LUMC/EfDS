# Projects, git, github intro

## A typical data science project

- multiple files with data analysis scripts
- development takes time - scripts evolve and have multiple versions
- growing - multiple directories/subdirectories after some time
- multiple files with data (but note: large files or files with sensitive content require different handling)
- self-shared (e.g. developed on a laptop and on a desktop machine)
- shared development with other contributors (programmers, supervisors, etc.)
- different states (snapshots) of the project exist on different computers

## Git

Git:

- "Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency."
- https://git-scm.com/

Important points:

- Let's assume that you have a directory with all files and subdirectories of a project. At first a new git repository is `initialized` and the directory becomes the **working directory**. From now on, it will be possible to track changes in files and subdirectories introduced during development.
- A `commit` is a moment when a copy (snapshot) of all project files is made. The copy is kept in a hidden **local repository**.
- At any moment all files of the project can be `checked out` (i.e. recreated from the local repository in the working directory, to have exactly the same content as at the moment of an earlier commit).
- A new, independent working directory for the project can be `cloned` and later synchronized (`merged`).

![](git_simple_cmds.jpg)

## GitHub

GitHub is a cloud-based web service where users can store and share developed code, based on git repository system.

Some example repositories:
- Materials of this course are hosted at GitHub, at the followig location: https://github.com/LUMC/EfDS
- Another course which we developed with help of GitHub; the course has a longer development history:
    - The source code/materials are here: https://github.com/LUMC/rcourse
    - The web pages served by GitHub based on the sources: https://lumc.github.io/rcourse/
- Many python related repositories: https://github.com/python

