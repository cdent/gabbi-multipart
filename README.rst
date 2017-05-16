
gabbi-multipart
---------

A content-handler for gabbi that can handle multipart/form-data request bodies.

Usage
=====

Add the handler to your test building code:

.. code:: python

  def load_tests(loader, tests, pattern):
    test_dir = os.path.join(os.path.dirname(__file__), TESTS_DIR)
    return driver.build_tests(test_dir, loader,
                              host='site.com',
                              content_handlers=[Multipart])

Then write a test:

.. code:: yaml

  name: multipart test
  POST: /somewhere
  request_headers:
    content-type: multipart/form-data
    data:
      key: val
      index: 1
      picture: @<sample.png
  status: 201
