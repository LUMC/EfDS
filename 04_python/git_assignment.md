# Git/GitHub assignment prepraration

## Introduction

The steps described in this document can be performed with [GitHub Desktop](https://desktop.github.com/), a useful tool to interact with a Git repository stored on GitHub servers. Since a repository does not need to be stored on GitHub, in this document we describe the processes using `git` command line interface.

## Create a new repository in GitHub

The goal of this step is to create a new repository at GitHub.  
This repository will be created with a few initial files (e.g. `README.md`).  
This repository will be stored in the cloud; nothing will be created on your laptop yet.

Steps:
- Go to the GitHub page (https://github.com/) and sign in to your account.
- Use the button "New" to *Create a new repository*:
    - Use *no template*.
    - You are the owner.
    - As *repository name* type: `EfDS_assignments`.
    - As *description* type: `Essentials for Data Science assignments`.
    - Select *private* (this repository should not be public).
    - Enable the option *add a `README` file*.
    - Select `.gitignore` template for Python.
    - No need to select any license.
    - Press *create repository`.
- You should now have a new repository created at GitHub.
- Get familiar with the new repository:
    - When you go to the main GitHub page (https://github.com/) you should be able to find the new repository listed on the left screen side.
    - Click on the name of the new repository to open the repository contents.
    - Click on the green *code* button to find HTTPS or SSH addresses needed to clone your repository to your laptop.

## Clone the new GitHub repository on your laptop

The goals of this step are:
- Clone (make a copy of) the GitHub repository at your laptop.
- Create a working directory with the newest files from the repository; you will later work in this directory.  

Steps:
- On your laptop start the system console (`cmd`, terminal, command line interface - names differ between operating systems).
- In the system console execute the `git` command. You should see output similar to:
```
> git
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index
```

- If you see error messages they need to be resolved. These are possible reasons:
    - `git` is not installed correctly.
    - `git` is not accessible in the system path.
    - You are in the `python` console, not in the system console.

Steps (once you know that the `git` command works):

- Change the current drive/directory to a directory where you want to clone the GitHub repository:
    - Windows: https://www.digitalcitizen.life/command-prompt-how-use-basic-commands/
    - Mac/Linux: https://medium.com/macoclock/10-essential-mac-terminal-commands-9a100805918c

- In the following line replace the URL with the HTTPS or SSH address of your repository.  
    Then execute the line to clone the GitHub repository to your laptop.  
    A directory named `EfDS_assignments` (the last argument) will be created.
```bash
git clone https://github.com/SzMK/EfDS_assignments.git EfDS_assignments
```

- Change the current directory to `EfDS_assignments` and list the content.  
    You should see output similar to:
```
> ls -ltr
total 8
-rw-r--r--  1 smkielbasa  staff  24 Feb 25 22:13 README.md
```

- With the following command you may check whether you are indeed associated with the GitHub repository:
```
> git remote -v
origin	https://github.com/SzMK/EfDS_assignments.git (fetch)
origin	https://github.com/SzMK/EfDS_assignments.git (push)
```

- Now you have a working directory with the newest state of the project known to GitHub.  

## Working on the assignments

The plan:
- You will be asked to share your GitHub assignments repository with the teachers.
- The solutions of the assignments are expected in the following files (located at the top level of your GitHub repository):
    - `assignment_A.ipynb`
    - `assignment_B.ipynb`
    - `assignment_C.ipynb`
- The files in their newest versions before the deadlines will be evaluated.

Steps:
- Copy the assignment file(s) to the working directory.
- Edit the solutions.
- When you decide to store the current state of your files use `git add` and `git commit` commands to store the files in the local repository.  
    Example (first change the current directory to the git working directory):
```bash
git add assignment_A.ipynb
git commit -m "solved task 2"
```
- After a `commit` operation you may want to `push` the newest state to the GitHub repository.  
    Example (first change the current directory to the git working directory):
```bash
git push
```
- After `push` you should see files of the newest `commit` on the GitHub page.

## Grant access

In order to evaluate your solutions, the teachers need read access to your repository.  
On the GitHub page of your repository go to *Settings* and next *Collaborators and Teams*.  
Use *Add people* button to grant *Read* access to the teachers: `SzMK-LUMC` and `Mo-LUMC`.

## Register your repository

In order to submit your grade, the teachers need to link your GitHub repository with your university account.  
In the following Python code edit your name, your student id and the SSH link to your GitHub assignments repository.  
Run the edited Python code to generate `assignments.json` file.  
In *Brightspace*, submit this file as a solution of the *SSH link to your GitHub repository* assignment.

```python
import json

assignmentsInfo = {
    "firstName": "John",                          # [1] put your first name here (spelled as in Brightspace)
    "lastName": "Smith",                          # [2] put your last name here (spelled as in Brightspace)
    "studentId": "s12345678",                     # [3] put your student id (spelled as in Brightspace)
    "sshGitHub": "git@github.com:LUMC/EfDS.git"   # [4] copy here the SSH address of your GitHub repository
                                                  #     (you may find it when you press the green Code button)
}

with open( "assignments.json", "w" ) as f:        # [5] run this cell to generate assignments.json file
    json.dump( obj = assignmentsInfo, fp = f )

                                                  # [6] submit the assignments.json file as a solution of
                                                  #     "SSH link to your GitHub repository"
                                                  #     assignment
```
