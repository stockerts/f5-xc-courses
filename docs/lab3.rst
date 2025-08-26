Route
=====

Scenario
--------

The development team has introduced a bug where the login page link no longer 
directs users correctly. Configure a **Route** to redirect requests to the proper login page.

Objective
---------

Successfully redirect requests by configuring the following:

- Route (Redirect)

Exercise 1: Configure a Route on HTTP Load Balancer
---------------------------------------------------

**Details**

+----------------+------------------------------------------+
| Route Type     | Redirect Route                           |
+----------------+------------------------------------------+
| Method         | Any                                      |
+----------------+------------------------------------------+
| Prefix Match   | ``/member/login``                        |
+----------------+------------------------------------------+
| Protocol       | incoming-proto                           |
+----------------+------------------------------------------+
| Host           | ``<namespace>.lab-sec.f5demos.com``      |
+----------------+------------------------------------------+
| Redirect Path  | ``/login``                               |
+----------------+------------------------------------------+
