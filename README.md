| Deliverable                                                                                            | Due Date                              |
|--------------------------------------------------------------------------------------------------------|---------------------------------------|
| Base Installation (nothing to submit)                                                                  | Wednesday, February 4th at 1:00PM EST |
| Intro to Linux [Gradescope Submission](https://www.gradescope.com/courses/1227626/assignments/7471274) | Monday,    February 9th at 1:00PM EST |
| Intro to Git [Gradescope Submission](https://www.gradescope.com/courses/1227626/assignments/7471275)   | Monday,    February 9th at 1:00PM EST |

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
using an Ubuntu terminal if you're testing the commands. Instructions
for setting up the course software is
[here](https://github.com/mit-rss/racecar_docker).

## Gradescope Submission

Once you have completed the exercises below and filled in your `lab1/linux_exercise.txt`, you will submit a `.zip`
file named `lab1.zip` **containing your `lab1` directory** to [Gradescope](https://www.gradescope.com/courses/1227626/assignments/7471274)
under **Lab 1A: Intro To Linux**. In Linux, the correct zip command is `zip -r lab1 lab1`. When you unzip `lab1.zip`, you
should see a directory named `lab1` containing a file named `linux_exercise.txt`.
          
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

Additionally, you may find the following IAP course useful: [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/).

## Instructions

1. Clone this repository by typing `git clone
   https://github.com/mit-rss/intro_to_linux.git` into your terminal. 
   **Please make sure you do this in ~/racecar_ws/src if you are using the Docker image.**
2. Place your answers to problems 1-5 in `lab1/linux_exercise.txt`. Do not create your own
   `linux_exercise.txt`Every command
   should go between the `#####<question_number>#######` and `#####End of Question#######` lines.
3. During this class, you will need to be familiar with at least one
   terminal-based text editor like [vim](https://www.vim.org/),
   [nano](https://www.nano-editor.org/), or
   [emacs](https://www.gnu.org/software/emacs/). We recommend getting
   some practice with a terminal-based text editor when you're editing
   `lab1/linux_exercise.txt`.
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

**a.** Navigate to your root directory.\
**b.** Navigate to your home directory.\
**c.** Navigate to the parent directory of your current directory.\
**d.** Create a new directory `~/test`.\
**e.** List all the files/directories in your home directory, including hidden ones, in long listing format.\
**f.** Print your current working directory.\
**g.** Remove the new directory `~/test`.\
**h.** Display the contents of the file `/etc/bash.bashrc`.

> **Note:** `/etc/bash.bashrc` is a system-wide file that is executed every time you open a new terminal. If you would like
> to add custom commands, please modify `~/.bashrc` as done in problem 4, as changes outside the home directory are not
> saved on `docker compose down`.

### Problem 2: Installing and Controlling Programs

One of the awesome features of UNIX-based operating systems is how simple it is to install
programs through the terminal. For this problem, use the Advanced Packaging Tool or **APT**,
which is the recommended way to install and manage Ubuntu packages.

**a.** Install a program called `inxi`.\
**b.** Many commands display useful information when called with the help option.
       Enter a command to show the `inxi` help menu in the terminal to see what it does.\
**c.** ~Additionally, there is a universally available reference bundled with almost every Unix system called
       "man pages" or manual pages. Enter a command to view the `inxi` man page for more detailed information.~\
       The docker container we provide does not provide the `man` command. For this question, enter `man inxi`.\
**d.** Use `inxi` to show information about your hardware disk info.\
**e.** Uninstall `inxi`.\
**f.** Update the list of available Ubuntu packages.\
**g.** Upgrade all existing packages.

> **Note:** In APT, *updating* fetches the latest version of the package list,
> while *upgrading* upgrades the actual packages installed on your system.
> Before installing or upgrading, it is always a good idea to update the package list.

### Problem 3: SSH

Another cool feature that you will be using often in this class is SSH
(Secure SHell), which enables you to access the terminals of other
Linux-powered remote devices or systems as long as you have access
credentials. This is how you will access the racecars.

**a.** From your Docker container, log into a remote shell with the address `athena.dialup.mit.edu`
       and your kerberos as the username. This will give you secure remote access to a shell running on
       an Athena machine running Linux.\
**b.** Logged into your Athena account, use `wget` to download the contents from
       `https://tinyurl.com/ya67uga4` into a file named `pic.png` in your Athena home directory.\
**c.** Exit the ssh session.\
**d.** Using the `scp` command from your Docker container,
       move the photo you just downloaded from your Athena account, `~/pic.png`,
       into the `~/racecar_ws` directory in your Docker container.
       This is useful for transferring files between your computer and the racecar.

### Problem 4: Tmux

In this class, you are going to be doing a lot of stuff in the terminal. A lot, a lot of stuff.
Running multiple launch scripts, debugging, echoing ros2 topics, etc. Instead of having 15 tabs,
where you have to run the same commands to initialize each and can only see one at a time,
we can use something called a **terminal multiplexer**, or [tmux](https://github.com/tmux/tmux/wiki).
Tmux allows us to run multiple terminals, see them all on the same screen, and run commands to start each automatically.
It can even allow us to run stuff in a terminal in the background, if we so desire. If we get super fancy, multiple people
can attach to the same tmux session, and look at the same stuff at the same time.

**a.** Start a new tmux session named `racecar` from an existing terminal.

Now you should be in a tmux session! The following are some useful but by no means extensive set of commands to
navigate inside a tmux session. Tmux uses `Ctrl+b` as the prefix key, meaning for the command `Ctrl+b d`, you press
`Ctrl+b`, release `Ctrl+b`, then type `d`:

| Command                   | Description             |
|---------------------------|-------------------------|
| `Ctrl+b %`                | Split pane vertically   |
| `Ctrl+b "`                | Split pane horizontally |
| `Ctrl+b <arrow_key>`      | Switch between panes    |
| `Ctrl+b <Ctrl+arrow_key>` | Change pane size        |
| `Ctrl+b c`                | Create new tab          |
| `Ctrl+b n`                | Switch between tabs     |

More commands can be found in this [cheatsheet](https://tmuxcheatsheet.com/). Explore some tmux commands!

**b.** Detach from your current tmux session. This is similar to "saving and exiting" your tmux session.

> When answering this question, you can use the corresponding `tmux` command or the keybinding.
> For the keybinding, enter in the following format: `Ctrl+b <key>`. For example, `Ctrl+b c` for creating a new tab.

**c.** List all active tmux sessions. You should see your `racecar` session!\
**d.** Attach to the `racecar` tmux session.

You should now see that your previous `racecar` session is saved. Again, run the command to detach from your current tmux session.

**e.** Kill the `racecar` tmux session, ending all processes running in that session.\
**f.** Enter a one-line command to add an alias `tks` for `tmux kill-session` to `~/.bashrc`. Your `~/.bashrc`
       file executes every time your new terminal opens, so you can now use the short command `tks` to kill your tmux session.

> **Hint:** Use the `echo` and redirect (`>>`) commands.

> **Note:** To be more exact, this command will work from the next time you open a new terminal. If you want to use the `tks` command in
> your current shell, you must run the command `source ~/.bashrc`, which executes the `~/.bashrc` file in the current shell.

`~/.bashrc` is one of the many **dotfiles**. Dotfiles are configuration files that start with a dot (.), which makes them hidden by default.
You cannot see them using the regular `ls` command; you need the `-a` flag (e.g., `ls -a ~`). These files customize your shell environment,
editor settings, and various tools. For example, to configure your tmux keybindings, appearance, and behavior, you can
create and modify the `~/.tmux.conf` file.

**g.** Enter a one-line command to add the line `set -g mouse on` to your `~/.tmux.conf` file. This allows you to click
       to select panes, resize windows, and scroll with your mouse wheel in tmux sessions.

Lastly, we can also use the `tmuxp` command to load `tmux` sessions from configuration files. We provide `tmux_template.yaml` which
launches a tmux session named `rss_tmux_template` with multiple panes and tabs.

**h.** Load `tmux_template.yaml` using `tmuxp`. 

Explore the tmux session. With your new alias and `~/.tmux.conf` file, you should now be able to move between panes and tabs using
your mouse and kill the tmux session by typing `tks`. You can explore other tmux configuration options
[here](https://github.com/tmux/tmux/wiki/Getting-Started#configuring-tmux).

### Problem 5: Environment Variables

Environment variables are dynamic values that affect the behavior of processes in your shell.
They store configuration like your home directory (`$HOME`), executable search paths (`$PATH`),
and application-specific settings such as `$ROS_DISTRO`.

**a.** Print the value of the `HOME` environment variable. This variable defines your home directory, `~`.\
**b.** Set the value of your `HOME` variable to `/home/racecar/racecar_ws` for the current session.\
**c.** List all environment variables currently set in your shell. You should see your `HOME` variable set to
       `/home/racecar/racecar_ws`.

Try running `cd ~ && pwd` now. You should see that your home directory is now set to `/home/racecar/racecar_ws`.
This is an example of how environment variables affect the behavior of your processes. For example, in ROS,
running `source /opt/ros/<ros_distro>/setup.bash` sets up the required environment variables to have ROS
properly functioning. More on this will be covered in Lab 1C.

