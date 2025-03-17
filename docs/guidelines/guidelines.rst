..
   # *******************************************************************************
   # Copyright (c) 2025 Contributors to the Eclipse Foundation
   #
   # See the NOTICE file(s) distributed with this work for additional
   # information regarding copyright ownership.
   #
   # This program and the accompanying materials are made available under the
   # terms of the Apache License Version 2.0 which is available at
   # https://www.apache.org/licenses/LICENSE-2.0
   #
   # SPDX-License-Identifier: Apache-2.0
   # *******************************************************************************

##########################
Guideline: Test Management
##########################


Run a pytest
************

Install needed dependencies
===========================

.. literalinclude:: /requirements.txt
   :caption: Needed dependencies
   :language: python
   :lineno-match:
   :start-after: #tests start
   :end-before: #tests end

Execute pytest
==============

Within a `yml` file, we can execute `pytest`.

.. literalinclude:: /../.github/workflows/builddoc.yml
   :caption: Execute pytest in yml
   :name: pytest_in_yml
   :language: yaml
   :lineno-match:
   :start-at: - name: Test with pytest
   :end-before: - name: extract data from test coverage.file


Make Test Results and Logs available
====================================

We do make all results and logs availalbe over the `_static` of the webside.

This has to be configured in `conf.py` via `html_static_path = ['_static']`.

.. literalinclude:: /conf.py
   :caption: html_static_path in conf.py
   :language: py
   :lineno-match:
   :start-at: html_static_path = ['_static']
   :end-at: html_static_path = ['_static']


Additionally we make the test result availalbe as artifacts for other jobs:

.. literalinclude:: /../.github/workflows/builddoc.yml
   :caption: Archive test results
   :language: yaml
   :lineno-match:
   :start-at: - name: Archive pytest test results
   :end-at: if: ${{ always() }}


Code Coverage
*************

Within :ref:`pytest_in_yml` we even measured the coverage.


Transform code coverage.file to other formats
=============================================

.. literalinclude:: /../.github/workflows/builddoc.yml
   :caption: coverage.file to other formats
   :language: yaml
   :lineno-match:
   :start-at: - name: extract data from test coverage.file
   :end-before: - name: Archive pytest test results


Make Test Coverage available
============================

.. literalinclude:: /../.github/workflows/builddoc.yml
   :caption: coverage.file to other formats
   :language: yaml
   :lineno-match:
   :start-at: - name: Archive pytest test results
   :end-at: if: ${{ always() }}


Make Test-Results, Test-Log and Coverage available in Sphinx
************************************************************

Test-Results in Sphinx-Needs
============================

Within the extension `sphinx-test-reports <https://sphinx-test-reports.readthedocs.io>`_
is a directive defined to translate complete junit xml files to needs objects:
`test_file <https://sphinx-test-reports.readthedocs.io/en/latest/directives/test_file.html>`_

.. literalinclude:: /tests/tests.rst
   :caption: Example of test_file directive
   :language: rst
   :lineno-match:
   :start-at: Test Results for <Your Product>
   :end-at: :auto_cases:


Test-Log and Coverage in Sphinx-Needs
=====================================

You can make all results available as links:

.. literalinclude:: /tests/tests.rst
   :caption: Example of access of test-Log and coverage
   :language: rst
   :lineno-match:
   :start-at: Test Log for <Your Product>


Maintain Test Specification in the same file as test-implementation
*******************************************************************


Add test folder to `conf.py`
============================

It is necessary that sphinx can find python moduls in the test folder.
For this the folder(s) have to be added in the `conf.py`.

.. literalinclude:: /conf.py
   :caption: Import of tests folder in conf.py
   :language: py
   :lineno-match:
   :start-after: # For test management:
   :end-before: #


Define a docstring in a python file
===================================

.. literalinclude:: /../tests/test_your_product.py
   :caption: Define a docstring in a python file
   :language: py
   :lineno-match:
   :start-at: Your_Product_test_specification
   :end-before: #


Extract Test Specification from python-file
===========================================

With the build in sphinx extension `autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
it is possible to automatically import docstring from source code and
at it to the current document.

We do want to import the test class in the test specification,
to extract the test steps. To not have a double import, we defined the
test specification available with a docstring to sperate into two different
elements.


.. literalinclude:: /tests/tests.rst
   :caption: Usage of autodoc
   :language: rst
   :lineno-match:
   :start-at: Test Specification for <Your Product>
   :end-before: Test Results for <Your Product>

The mentioned sphinx-extenstion has to be added in the `conf.py`:

.. literalinclude:: /conf.py
   :caption: Extensions in conf.py
   :language: py
   :lineno-match:
   :start-after: extensions
   :end-before: ]
