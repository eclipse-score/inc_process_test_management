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

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# sys.path extension for local files is needed, because the conf.py file is not
# executed, but imported by Sphinx
sys.path.insert(0, ".")

# For test management:
sys.path.append(os.path.abspath('../tests'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Score: Incubation Process Test Management"
author = "Score"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_needs",
    "sphinx.ext.autodoc",
    "sphinxcontrib.test_reports",
]

exclude_patterns = [
    "Thumbs.db",
    ".DS_Store",
    "**/_template",
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

templates_path = ["_templates"]

# Enable numref
numfig = True


# -- sphinx-needs configuration --------------------------------------------
# Setting the needs layouts

needs_build_json = True

needs_types = [
    dict(directive="sw_req", title="Software Requirement", prefix="SWRQ_", color="#abcdef", style="artifact"),
    # Testing:
    dict(directive="test_spec", title="Test Specification", prefix="TS_", color="#abcdef", style="artifact"),
]

needs_extra_options = [
   'test_status',
]

needs_extra_links = [
   {
      "option": "tests",
      "incoming": "tested by",
      "outgoing": "tests",
      "style_start": "-right",
      "style_end": "->"
   },
   {
      "option": "verified_by",
      "incoming": "verifies",
      "outgoing": "verified by",
      "style_start": "-right",
      "style_end": "->"
   },
]
