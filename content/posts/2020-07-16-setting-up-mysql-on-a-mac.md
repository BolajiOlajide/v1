---
template: post
title: Setting up MySQL on a Macbook
slug: setting-up-mysql-mac
draft: true
date: 2020-07-16T01:11:33.827Z
description: >-
  Setting up a new database on mac can be a pain for some developers. In this
  tutorial, I take you through the steps I take to install and set up MySQL on
  my MacBook for my development.
category: tech
tags:
  - mac
  - mysql
  - sql
  - database
---
> MySQL is an open-source relational database management system. Its name is a combination of "My", the name of co-founder Michael Widenius's daughter, and "SQL", the abbreviation for Structured Query Language. - [Source](https://en.wikipedia.org/wiki/MySQL)

Setting up MySQL for development on your Mac can be tricky and stressful at times, a lot of developers I know don't like to go through that hassle. This prompted me to write this article to walk you through the steps I take to set up MySQL on my mac.

## Prerequisites

1. A mac book
2. Homebrew installed on your mac (Installation guide can [be found here](https://brew.sh/)) 

### Installing MySQL

I usually install MySQL via Homebrew. Confirm you have Homebrew installed by running the command below in terminal:

```sh
brew -v
```

Once you've confirmed you have Homebrew installed, the next step is to install MySQL using the command

```sh
brew install mysql
```

Once the installation is done, you can start MySQL as a background service with the command

```sh
brew services start mysql
```

or 

```sh
mysql.server start
```

if you don't need it as a background service.
This tutorial makes use of version 8 of MySQL.

### Setting up MySQL

Once MySQL has been installed we need to create a user and assign roles to that user. The first step we'll take is to access the `mysql` shell using the `root` user - to do this we'll use the command

```sh
mysql -u root
```

This will take you to the `mysql` shell and you should see the `mysql>` prompt.
Now that we're in the `mysql` shell, we'll be writing MySQL statements to perform several actions for us.

```sh
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.21 Homebrew

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

We'll approach the setup in three phases:

1. Create a new user
2. Grant privileges to the new user
3. Access the shell using the newly created user

#### Create new user

To create a new MySQL user, we'll use the command

```sql
CREATE USER 'user_name'@'localhost' IDENTIFIED BY 'user_password';
```

Remember to replace `user_name` and `user_password` with the username and password you'd like to access MySQL with and also ensure you terminate the statement with a semicolon (`;`), else the statement won't be acted upon by MySQL.

#### Grant Privileges

Now that we've created our user, we need to grant privileges, this will determine how much power this new user wields. Here's a breakdown of the different types of privileges in MySQL:

* ALL PRIVILEGES: Gives the said user access to all privileges.
* CREATE: Allow a user to be able to create a database(s).
* DROP: Allow a user to delete a database(s).
* DELETE: Allow a user to delete rows from a table.
* INSERT: Allow a user insert rows into a table.
* SELECT: Allow a user query for records in a table.
* UPDATE: Allow a user to update rows of records in a table.
* GRANT OPTION: Allow a user to grant/remove other user's privileges.

Depending on whichever privilege you prefer to grant the newly created user, you can actually grant the privilege with the command:

```sql
GRANT privilege ON *.* TO ‘user_name’@'localhost’;
```

An example is `GRANT ALL PRIVILEGES ON *.* TO 'bolaji'@'localhost';` to grant the user with the name `bolaji` all privileges.

Once you're done granting permissions, you can use the `SHOW GRANTS` command to show the privileges assigned to any user, an example is shown below:

```sql
SHOW GRANTS FOR 'bolaji'@'localhost';
```

Now that we've created a user and granted the said user some privileges. Let's quit our current mysql session by entering the command `quit` in the mysql shell.

#### Access the shell

We can start another session of mysql using the user we just created. This time we'll be using a different command

```sh
mysql -u user_name -p
```

The `-p` flag means that we'd be prompted for a password once we hit the enter key. For super users like `root`, we didn't need to enter the `-p` flag because no password was set for the `root` user.

Once we are in, we can confirm the current user with the command below:

```sql
SELECT CURRENT_USER();
```

Now that we're done, you can use mysql for any of your dev project using the credentials you created your user with.


If this was helpful, feel free to share and/or drop a comment.

If you've got questions, feel free to share them in the comment section or reach out to me [on twitter](https://twitter.com/Bolaji___).
