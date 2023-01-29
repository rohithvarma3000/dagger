=======================================
dagger
=======================================

.. image:: https://github.com/rohithvarma3000/dagger/actions/workflows/python-package.yml/badge.svg
   :target: https://github.com/rohithvarma3000/dagger/actions/workflows/python-package.yml
   :alt: Python package
.. image:: https://readthedocs.org/projects/dagger/badge/?version=latest
   :target: https://dagger.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://codecov.io/gh/rohithvarma3000/dagger/branch/main/graph/badge.svg?token=VtrYdLrEMV
   :target: https://codecov.io/gh/rohithvarma3000/dagger
.. image:: http://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/rohithvarma3000/dagger/main/LICENSE
   :alt: License


**A Python implementation for controlling Pluto Drone.**

Installation
============

Installing the Current Release
------------------------------

If you have Python installed you can install the current release using either pip: ::

   pip install pluto-dagger


Installing the package from source
----------------------------------

1. Get the latest source by cloning this repo: ::

      git clone https://github.com/rohithvarma3000/dagger.git

2. Install the dependencies: ::

      pip install -r requirements.txt

3. Install dagger: ::

      pip install .

Examples
========

Connecting to Pluto ::

      import dagger
      Pluto_IP = "192.168.4.1"
      Pluto_PORT = 23
      pluto = dagger.PlutoConnection()
      pluto.connect((Pluto_IP, Pluto_PORT))

Intiating the SetRawRc Object for Controlling the pluto Drone using the RC params ::

      rc = dagger.SetRawRC(pluto)

Arming the drone ::

      rc.arm_drone()

Disarming the drone::

   rc.disarm_drone()

General Information
===================

- `Website and Documentation <link URL>`_
- `Tutorial <https://github.com/rohithvarma3000/dagger/blob/main/tutorials/dagger_example.ipynb>`_

How to Use?
===========
Refer to our `tutorial <https://github.com/rohithvarma3000/dagger/blob/main/tutorials/dagger_example.ipynb>`_ to get started with dagger


.. _dagger : https://github.com/rohithvarma3000/dagger.git


