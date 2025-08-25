Route
=====

Introduction
------------

During this lab, you will create a Route.

Learning Objectives
-------------------

By the end of the lab you will be able to create the following objects:

- Route (Redirect)

Exercise 1: Create Route on HTTP Load Balancer
----------------------------------------------

**Details**

+----------------+------------------------------------------+
| Route Type     | Redirect Route                           |
+----------------+------------------------------------------+
| Method         | Any                                      |
+----------------+------------------------------------------+
| Prefix Match   | ``/member/login``                        |
+----------------+------------------------------------------+
| Protocol       | incoming-proto``                         |
+----------------+------------------------------------------+
| Host           | ``<namespace>.lab-sec.f5demos.com``      |
+----------------+------------------------------------------+
| Redirect Path  | ``/login``                               |
+----------------+------------------------------------------+
