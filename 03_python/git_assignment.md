# Git/GitHub: how to deliver assignments

## Overview

Learning how to use Git and GitHub is an important part of the course. Therefore, we will ask you to deliver your assignments using Git and GitHub:

- You will need to create an **own, free GitHub account**. Once you have an account, you will be able to create own repositories or join repositories of others.
- Using own GitHub account you will create **a new repository for the individual assignments**:
  - This repository will be private and shared only with the teachers.
  - In this repository you will create a `json` file with your personal data (your name, email, student id).
  - In this repository you will deliver the solutions of the individual assignments.
- Later, for the group assignment, you will be asked to create/join **a team repository**:
  - This repository will be private and shared only with the members of the group and the teachers.
  - In this repository you will create a special `json` file with the names and student ids of the group members.
  - In this repository the group will deliver the solutions of the group assignment.
- The solutions present in the GitHub repository at the deadlines will be evaluated.
- You will use your laptop to work on the assignments. You will need to install Git on your laptop. You will synchronize the files between the laptop and the GitHub repository using Git commands (e.g. `add`, `commit`, `push`, `pull`).

*Note:* The commands shown in this document are based on the `git` command line interface. Many of the operations can be performed using the [GitHub Desktop](https://desktop.github.com/) application or Git/GitHub plugins in the [VSCode](https://code.visualstudio.com/) editor, etc. Use the tools you are most comfortable with.

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
  - Select *private* **(this repository must not be public)**.
  - Enable the option *add a `README` file*.
  - Select `.gitignore` template for Python.
  - No need to select any license.
  - Press "Create repository".
- You should now have a new repository created at GitHub.
- Get familiar with the new repository:
  - When you go to the main GitHub page (https://github.com/) you should be able to find your new repository.
  - Click on the name of the new repository to open the repository contents.
  - Click on the green "Code" button to find HTTPS or SSH addresses needed to clone your repository to your laptop.

## Identify your repository and grant access to the teachers

Later, in order to evaluate your solutions, the teachers need read access to your repository. On the GitHub page of your repository go to *Settings* and next *Collaborators and Teams*. Use the "Add people" button to grant *Read* access to the teachers (search for users: `SzMK-LUMC` and `RM-LUMC`).  

Once the teachers have access to your repository, they will be able to see the content of the repository. Still, the teachers will not know who you are. Therefore, you will need to create a special file with your personal data and store it in the repository.  

On the GitHub page of your repository use the "Add file" button to create a new file. The name of the file should be `student2025.json` (use exactly this name, small letters, no spaces). The file should be stored in the top directory of the repository. The content of the file should be in the `json` format. Copy the following text to the file and edit the fields with your personal data. Once you are ready, commit the file to the repository.

```json
{
    "firstName": "John",
    "lastName": "Smith",
    "studentId": "s12345678",
    "email": "s12345678@mail.leidenuniv.nl"
}
```

## Clone the new GitHub repository on your laptop

The goal of this step is to `clone` (make a copy of) the GitHub repository on your laptop. A working directory will be created. Later, you will work in this directory. You may clone the repository with a `clone` command of your text editor (e.g. VSCode) or with the `git` command line interface (CLI).

### `git` CLI: check whether `git` is properly installed

- On your laptop start the system console (`cmd`, terminal, command line interface - names differ between operating systems).
- In the system console execute the `git` command. You should see output similar to:

```{bash}
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

### `git` CLI: clone the GitHub repository

- Change the current drive/directory to a directory where you want to clone the GitHub repository:
  - Windows: https://www.digitalcitizen.life/command-prompt-how-use-basic-commands/
  - Mac/Linux: https://medium.com/macoclock/10-essential-mac-terminal-commands-9a100805918c

- In the following line replace the URL with the HTTPS or SSH address of your repository.  
    Then execute the line to clone the GitHub repository to your laptop.  
    A directory named `EfDS_assignments` (the last argument) will be created.

```bash
git clone https://github.com/SzMK/EfDS_assignments.git EfDS_assignments
```

### `git` CLI: investigate the cloned repository

- Change the current directory to `EfDS_assignments` and list the content.  
    You should see output similar to:

```bash
> ls -ltr
total 8
-rw-r--r--  1 smkielbasa  staff  24 Feb 25 22:13 README.md
```

- With the following command you may check whether you are indeed associated with the GitHub repository:

```bash
> git remote -v
origin	https://github.com/SzMK/EfDS_assignments.git (fetch)
origin	https://github.com/SzMK/EfDS_assignments.git (push)
```

- Now you have a working directory with the newest state of the project known to GitHub.  

## Working on the assignments

You will be asked to deliver the solutions in files with specific names (the names will be given later, for example: `assignment_B.ipynb`). The spelling of the file names is important. Pay attention to the capital letters and the file extension. Files in wrong formats or with wrong spellings of the file names will not be evaluated. The files will need to be stored in the top directory of the repository. Files located in other directories will not be evaluated.

Steps (general):

- The files with assignments will be provided in Brightspace. Download the assignment file(s) to the working directory of your repository on your laptop.
- Edit the file, fill in the solutions.
- When you decide to store the current state of your files in the repository:
  - First, in VSCode, **use the "Clear All Outputs" button to remove the outputs from the Jupyter notebook**.
  - Save the file.
  - Then `add` and `commit` the file to the local repository. Later `push` the newest state to the GitHub repository.
  - You may `commit` and `push` the files multiple times before the deadline. The last commit before the deadline will be evaluated.

### `git` CLI: Adding/updating files in the local repository

- When you decide to store the current state of your files use `git add` and `git commit` commands to store the files in the local repository.  
    Example (first change the current directory to the git working directory):

```bash
git add assignment_B.ipynb
git commit -m "solved task 2"
```

### `git` CLI: Pushing the local repository to the GitHub repository

- After a `commit` operation you may want to `push` the newest state to the GitHub repository.  
    Example (first change the current directory to the git working directory):

```bash
git push
```

- After `push` you should see files of the newest `commit` on the GitHub page.
