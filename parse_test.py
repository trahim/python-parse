from parse import *
import unittest
from httmock import urlmatch, with_httmock, response
from StringIO import StringIO
import sys

class TestParse(unittest.TestCase):

    @urlmatch(netloc=r'(.*\.)?198.61.207.112$')
    def invent_mock(url, request):
        invent = json.dumps({'count': 20, 'text': 'testing 1 2 3'})
        HEADERS = {'content-type': 'application/json'}
        return response(200, invent, HEADERS, None, 5, request)

    @with_httmock(invent_mock)
    def test_get_invent(self):
        result = get_inventory('198.61.207.112')
        self.assertIsInstance(result, dict)
        self.assertEqual(result['count'], 20)
        self.assertEqual(result['text'], 'testing 1 2 3')

    def test_get_values(self):
        invent = json.dumps({'count': 20, 'text': 'testing 1 2 3'})
        self.assertEqual(get_values(invent), (20, "testing 1 2 3"))

    def test_print_inventory(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            print_inventory(10, '12345 678910')
            output = out.getvalue().strip()
            self.assertEqual(output, '12345\n678910')
        finally:
            sys.stdout = saved_stdout


if __name__ == '__main__':
    unittest.main()