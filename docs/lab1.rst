HTTP Load Balancer
==================

Introduction
------------

During this lab, you will create a HTTP Load Balancer along with all child objects.

Learning Objectives
-------------------

By the end of the lab you will be able to create the following objects:

- Health check
- Origin Pool (Public)
- Load Balancer (Public)

Exercise 1: Create a Health Check
---------------------------------

Details

:Name : ``<namespace>-hc``

Exercise 2: Create a Origin Pool and attached Health Check
----------------------------------------------------------

Details

Name: ``<namespace>-op``

Type: ``Public DNS Name of Origin Server``

DNS Name: ``demoapp.lab-sec.f5demos.com``

Port: ``80``

TLS: ``Disabled``

Exercise 3: Create a HTTP Load Balancer and attach Origin Pool
--------------------------------------------------------------

Details

:Name : ``<namespace>-lb``
:Domain : ``<namespace>-lab-sec.f5demos.com``
:Load Balancer Type: ``HTTPS with Custom Certificate``
:HTTP Redirect to HTTPS: ``Check``
:HTTPS Port: ``443``
:TLS Certificate: ``shared/lab-sec-wildcard``
:Origin Pool: ``<namespace>/<namespace>-op``
:VIP Advertisement: ``Internet``