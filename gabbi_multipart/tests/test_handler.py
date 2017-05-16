

import unittest

from gabbi import case
from gabbi import exception
from gabbi import suitemaker

from gabbi_multipart import handler


class TestMultipartHandler(unittest.TestCase):

    def setUp(self):
        super(TestMultipartHandler, self).setUp()
        self.test_class = case.HTTPTestCase
        self.handler = handler.Multipart()
        self.test = suitemaker.TestBuilder(
            'mytest', (self.test_class,),
            {
                'test_data': {
                    'request_headers': {
                        'content-type': 'multipart/form-data',
                    },
                    'data': {
                        'alpha': 1,
                        'beta': 'cow',
                        'gamma': '@<sample.png',
                    },
                },
                'content_handlers': [self.handler]
            }
        )

    def test_handler_accepts_multipart(self):
        self.assertTrue(
            self.handler.accepts(
                self.test.test_data['request_headers']['content-type']))

    def test_dumps_format_error(self):
        self.assertRaises(exception.GabbiFormatError,
                          self.handler.dumps,
                          'foo')
