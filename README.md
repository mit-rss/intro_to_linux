| Deliverable | Due Date              |
|---------------|----------------------------------------------------------------------------|
| Base Installation (nothing to submit)  | Wednesday, February 5th at 1:00PM EST |
| Intro to Linux [Gradescope Submission](https://www.gradescope.com/courses/973988/assignments/5710353)  | Monday, February 10th at 1:00PM EST |
| Intro to Git [Gradescope Submission](https://www.gradescope.com/courses/973988/assignments/5710354)  | Monday, February 10th at 1:00PM EST |

# Intro to Linux

## Table of Contents

* [Introduction](https://github.com/mit-rss/intro_to_linux#introduction)
* [Gradescope Submission](https://github.com/mit-rss/intro_to_linux#gradescope-submission)
* [References](https://github.com/mit-rss/intro_to_linux#references)
* [Instructions](https://github.com/mit-rss/intro_to_linux#instructions)
* [Problems](https://github.com/mit-rss/intro_to_linux#problems)

## Introduction

Linux is an essential part of the class, so it's important to get some
experience with this before working with the robots. Although you're
encouraged to collaborate with others if you are stuck, the lab should
be completed individually so you can get practice with skills that
will be essential later on in the course when you are in teams. If you
have general questions, please post on
[Piazza](https://piazza.com/mit/spring2026/64200164052124/home) so other students
can benefit from the answer. If you have a question about your
individual submission, please make a private post. Make sure you're
using a Debian terminal if you're testing the commands. Instructions
for setting up the course software is
[here](https://github.com/mit-rss/racecar_docker). Alternatively,
you can use your Athena terminal to test commands by typing `ssh
<kerberos>@athena.dialup.mit.edu` in your terminal, substituting
`<kerberos>` for your own kerberos username. Most of the commands below
should work, although a few of them may not.

## Gradescope Submission

In order to get credit for this assignment, you will submit a `.zip`
file to [Gradescope](https://www.gradescope.com/courses/973988/assignments/5710353) under
**Lab 1A: Intro To Linux**. The format of the file will be specified in
Problem 4. Your submission will not get graded properly if you don't
put it in the right format.
          
## References

If you don't have previous experience with Linux, we recommend that
you read the following tutorials by the Software Carpentry Foundation
before starting on the exercises. Otherwise, you can just use the

resources as you need.
1. [Setup](https://swcarpentry.github.io/shell-novice/index.html)
2. [Introducing the Shell](https://swcarpentry.github.io/shell-novice/01-intro.html)
3. [Navigating files and directories](https://swcarpentry.github.io/shell-novice/02-filedir.html)
4. [Working with files and directories](https://swcarpentry.github.io/shell-novice/03-create.html)
5. [Pipes and filters](https://swcarpentry.github.io/shell-novice/04-pipefilter.html)
6. [Finding things](https://swcarpentry.github.io/shell-novice/07-find.html)

Additionally, there is a universally available reference bundled with
almost every Unix system called "man pages" or manual pages. By typing
`man <command>` in the terminal, where `<command>` is the command you
want to learn about, you can see comprehensive documentation about the
command. Many commands also display useful information when called with the
help option by running `<command> -h` or `<command> --help`.

## Instructions

1. Clone this repository by typing `git clone
   https://github.com/mit-rss/intro_to_linux.git` into your terminal. 
   **Please make sure you do this in ~/racecar_ws/src if you are using the Docker image.**
2. Place your answers to problems 1-3 in `linux_exercise.txt`. Every command
   should go between the `#####<question_number>#######` and `#####End
   of Question#######` lines.
3. During this class, you will need to be familiar with at least one
   terminal-based text editor like [vim](https://www.vim.org/),
   [nano](https://www.nano-editor.org/), or
   [emacs](https://www.gnu.org/software/emacs/). We recommend getting
   some practice with a terminal-based text editor when you're editing
   `linux_exercise.txt`.
4. Run `sanity_checker.py` to double check that your answers are
   correctly formatted.
5. Provide a single command for each of the following problems. If
   multiple answers are possible, choose the shortest answer. All of
   your commands should work regardless of your current working
   directory. [Hint](https://www.gnu.org/software/bash/manual/html_node/Tilde-Expansion.html)

## Problems

Complete the following exercises **inside your Docker container** to access a Linux terminal.

### Problem 1: Navigating your Home

The first thing you need to learn in the command-line is how to
navigate the filesystem and view the contents of directories and
files.

a. Navigate to your home directory
b. Navigate to your root directory
c. Navigate to the parent directory of your current directory
d. List all the files/directories in your home directory, including hidden ones, in long listing format
e. Print your current working directory

### Problem 2: Installing and Controlling Programs

One of the awesome features of UNIX-based operating systems is how simple it is to install
programs through the terminal. For this problem, use the Advanced Packaging Tool or **APT**,
which is the recommended way to install and manage Debian packages.

a. Install a program called `inxi`
b. Show output control options for `inxi` in the terminal to see what it does
c. Use `inxi` to show information about your hardware disk info
d. Uninstall `inxi`
e. Update the list of available Debian packages
f. Upgrade all existing packages

> **Note:** In APT, *updating* fetches the latest version of the package list 

### Problem 3: SSH

Another cool feature that you will be using often in this class is SSH
(Secure SHell), which enables you to access the terminals of other
Linux-powered remote devices or systems as long as you have access
credentials. This is how you will access the racecars.

a. From your Docker container, log into a remote shell with the address `athena.dialup.mit.edu`
   and your kerberos as the username. This will give you secure remote access to a shell running on
   an Athena machine running Linux.
b. Logged into your Athena account, download the contents from `https://tinyurl.com/ya67uga4`
   into a file named `pic.png` in your Athena home directory.
c. Exit the ssh session.
d. Using the `scp` command from your Docker container,
   move the photo you just downloaded from your Athena account, `~/pic.png`,
   into the home directory on your Docker container.
   This is useful for transferring files between your computer and the Racecar.

### Problem 4: Tmux

In this class, you are going to be doing a lot of stuff in the terminal. A lot, a lot of stuff.
Running multiple launch scripts, debugging, echoing ros2 topics, etc. Instead of having 15 tabs,
where you have to run the same commands to initialize each, and can only see one at a time,
we can use something called a **terminal multiplexer**, or [tmux](https://github.com/tmux/tmux/wiki).
Tmux allows us to run multiple terminals, see them all on the same screen, and run commands to start each automatically.
It can even allow us to run stuff in a terminal in the background, if we so desire. If we get super fancy, multiple people
can attach to the same tmux session, and look at the same stuff at the same time.

### Problem 5: Dotfiles



### Problem 6: Docker


