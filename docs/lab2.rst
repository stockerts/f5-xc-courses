Service Policy
==============

Introduction
------------

During this lab, you will create a Service Policy.

Learning Objectives
-------------------

By the end of the lab you will be able to create the following objects:

- Service Policy (IP Deny)

Exercise 1: Create a Service Policy
-----------------------------------

Details
+--------------------+----------------------------+
| Name               | ``<namespace>-ipdeny-sp``  |
+--------------------+----------------------------+
| Rule               | ``Denied Sources``         |
+--------------------+----------------------------+
| IPv4 Prefix List   | ``IP will be provided``    |
+--------------------+----------------------------+
| Default Action     | ``Next Policy``            |
+--------------------+----------------------------+


Exercise 2: Attach Service Policy to a HTTP Load Balancer
---------------------------------------------------------

Details
+-------------------+---------------------------------------+
| Service Policies  | ``Apply Specified Service Polices``   |
+-------------------+---------------------------------------+
| Order 1           | ``<namespace>-ipdeny-sp``             |
+-------------------+---------------------------------------+
| Order 2           | ``ves-io-shared/ves-io-allow-all``    |
+-------------------+---------------------------------------+