"""
<Your_Product> for Test Management:
"""

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

Your_Product_test_specification = ''
"""
.. test_spec:: Test of <your product>
   :id: TS_ID
   :status: new
   :verified_by: TEST_ID
   :tests: SWRQ_ID,

   This is a test specification for <your product>.

   **Test execution**

   Run tests in test class with pytest. Command: `pytest -q test_your_product.py`

   **Test steps**

   .. autoclass:: test_your_product.Test_Your_Product
      :member-order: bysource
      :members:
      :undoc-members:

"""

# Depending on the test level, you have to make your source code availabel,
# or you have to run a compiled application.

import pytest

class Test_Your_Product:

    def test_example_case_2(self):
        """2. Secound example comparing function output with expected output."""

        input_a = 42

        output_x = input_a*2

        assert output_x == 84

    def test_example_case_1(self):
        """1. Easy example comparing function output with expected output."""

        # We broke the ordering of the function numbering with intention,
        # so we can see that the auto import (autoclass) in the test specification
        # is done on ordering the names of the function and not on fifo.

        input_a = 21

        output_x = input_a*2

        assert output_x == 42

