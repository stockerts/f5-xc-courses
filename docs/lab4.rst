App Firewall (WAF)
==================

Introduction
------------

During this lab, you will create a App Firewall (WAF).

Learning Objectives
-------------------

By the end of the lab you will be able to create the following objects:

- App Firewall (WAF)

Exercise 1: Create a Route
--------------------------

**Details**

+-------------------+-------------------+
| Name              | ``<namespace>-af``|
+-------------------+-------------------+
| Enforcement Mode  | ``Blocking``      |
+-------------------+-------------------+


Exercise 2: Attach Route to HTTP Load Balancer
----------------------------------------------

**Details**

+-------------------------------+-------------------+
| Web Application Firewall (WAF)| ``Enable``        |
+-------------------------------+-------------------+
| Enable (WAF object)           | ``<namespace>-af``|
+-------------------------------+-------------------+
