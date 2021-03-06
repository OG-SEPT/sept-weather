import os
import unittest
import tempfile
import sept_weather

class FlaskrTestCase(unittest.TestCase):

    def test_stations_info(self):
        self.app = sept_weather.app.test_client()
        result = self.app.get('/')

        assert '<!DOCTYPE html>' in result.data
    
    def test_reset_database(self):
        self.app = sept_weather.app.test_client()
        result = self.app.get('/reset_database')

        assert 'Successful' in result.data
    

if __name__ == '__main__':
    unittest.main()
