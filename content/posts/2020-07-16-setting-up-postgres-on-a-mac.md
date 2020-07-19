---
template: post
title: Setting up MySQL on a Macbook
slug: setting-up-mysql-mac
draft: true
date: 2020-07-16T01:11:33.827Z
description: >-
  Setting up Postgres can be a pain sometimes, in this article we walk through
  setting up Postgres with all the required permissions on a new PC.
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
 
### Setting up MySQL
 
Once MySQL has been installed we need to create a user and assign roles to that user. The first step we'll take is to access the `mysql` shell using the `root` user - to do this we'll use the command
```sh
mysql -u root
```
