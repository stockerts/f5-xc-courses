Route
=====

Introduction
------------

During this lab, you will create a Route.

Learning Objectives
-------------------

By the end of the lab you will be able to create the following objects:

- Route (Redirect)

Exercise 1: Create a Route
--------------------------

Details

:Name: ``<namespace>-ipdeny-sp``
:Rule: ``Denied Sources``
:IPv4 Prefix List: ``IP will be provided``
:Default Action: ``Next Policy``

Exercise 2: Attach Route to HTTP Load Balancer
----------------------------------------------

Details

:Route Type: ``Redirect Route``
:Method: ``Any``
:Prefix Match: ``/member/login``
:Protocal: ``incoming-proto``
:Host: ``<namespace>.lab-sec.f5demos.com``
:Redirect Path: ``/login``