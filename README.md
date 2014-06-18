POJBadge
========

## Introduction

A user badge generator for [POJ](http://poj.org) (Peking University Online Judge System) . 

The generated badge looks like the user badge on [ProjectEuler](https://projecteuler.net/), which can be found below.

![Badge of ProjectEuler](out/psyclaudeZ.png)

Current look of POJBadge (keeps updating).

![POJBadge](out/test.png)

## Dependencies
* python 2.7
* PIL for image generation
* BeautifulSoup for parsing HTML

## How to Use
TBA.

## File Structure
* main: central modules; receives input from users; makes use of other two 
* badge_generator: as name suggests; solely in charge of PNG generation
* crawler: crawls designated user data from online judge
