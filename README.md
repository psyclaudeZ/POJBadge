POJBadge
========

A user badge generator for [POJ](http://poj.org) (Peking University Online Judge System) . 

The generated badge looks like the user badge on [ProjectEuler](https://projecteuler.net/), which can be found below.

![Badge of ProjectEuler](http://projecteuler.net/profile/psyclaudeZ.png)

## Structure
* POJBadge_generator: central modules; receives input from users; makes use of other two 
* badge_generator: as name suggests; solely in charge of PNG generation
* crawler: crawl designated user data from online judge
