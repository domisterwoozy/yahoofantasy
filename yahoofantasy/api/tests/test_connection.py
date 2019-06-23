from unittest import TestCase
from unittest.mock import patch
from yahoo_sdk.connection import Connection
from yahoo_sdk.tests.sample_responses import make_test_request


class TestConnection(TestCase):

    @patch('yahoo_sdk.connection.make_request', return_value={})
    @patch('yahoo_sdk.util.xml.from_response_object')
    def test_fetch_no_persist(self, _, mock_request):
        con = Connection(persist=None)
        con.fetch()
        import pdb
        pdb.set_trace()  # XXX BREAKPOINT
        pass