App Firewall (WAF)
==================

Scenario
--------

We have been informed of multiple attacks targeting the application. 
Create and attach a **App Firewall (WAF)** to mitigate further threats.

Objective
---------

Successfully mitigate attacks against the application by creating 
and attaching the following:

- App Firewall (WAF)

Exercise 1: Create a Route
--------------------------

**Quick Reference**

+-------------------+-------------------+
| Name              | ``<namespace>-af``|
+-------------------+-------------------+
| Enforcement Mode  | Blocking          |
+-------------------+-------------------+


Exercise 2: Attach Route to HTTP Load Balancer
----------------------------------------------

**Quick Reference**

+-------------------------------+-------------------+
| Web Application Firewall (WAF)| Enable            |
+-------------------------------+-------------------+
| Enable (WAF object)           | <namespace>-af    |
+-------------------------------+-------------------+
