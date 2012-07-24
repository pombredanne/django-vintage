===============
Getting Started
===============

.. contents::
   :depth:  1
   :local:
   :backlinks: top

Setting it up
=============

#. Create a directory called ``vintage`` in your template directory

#. Create a new template called ``default.html`` in that directory


Creating a page manually
========================

#. Click on the new page button in the admin.

#. Enter the URL path of the old page. Should be everything after the http://domainname.com. For Example: ``/articles/2010/may/01/bigfoot-sighted/``.

#. Enter the page's title.

#. View the source of the page you are archiving.

#. Select the appropriate HTML content (such as everything between the ``<body>`` tags).

#. Paste it into the content field.

#. Select a template (leave blank for default) see :ref:`How Django Vintage selects the template<how-django-vintage-selects-the-template>`

#. Enter in any of the page's metadata fields: ``page_id``, ``image``, ``description``, ``keywords``, and ``author``.


For the future
==============

Importing a page
----------------

Need: URL and CSS selector (like ``body`` or ``#main-content``)
Does: Loads the page, imports the content based on the CSS selector, sets the title, URL and metadata fields based on the page attributes.
