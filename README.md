# Social Blade API demo

This repository contains a simple Python script to query the [Social Blade](https://socialblade.com/) API to find Twitter data for a given user.

## Setup:

First install requirements.txt: 

`$ pip install -r requirements.txt`

Save the Social Blade user ID and access token as environment variables, named as below (these will be read by the Python script):

`$ export ID=yourID`

`$ export TOKEN=yourtoken`

## Usage:

The script can be run from command line and takes two arguments, a Twitter handle and a category name (basically the directory to create and save results in).

Example:

`$ python socialblade_twitter.py corintxt journalists`