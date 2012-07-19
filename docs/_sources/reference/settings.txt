========
Settings
========

.. contents::
   :depth:  1
   :local:
   :backlinks: top

Default settings
================

.. code-block:: python

    VINTAGE_SETTINGS = {
        'METADATA_FORM': 'vintage.metadata_form.MetadataForm',
    }

.. _metadata-form-setting:

METADATA_FORM
=============

This string is a Python path to the Django :py:class:`Form` that displays, manages and validates the metadata.