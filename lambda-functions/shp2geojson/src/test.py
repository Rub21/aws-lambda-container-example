import os
import unittest
import app


class TestApplication(unittest.TestCase):

    def test_app_returns_ok_message(self):
        os.environ['SHAPEFILE_ZIP_URL'] = 'https://raw.githubusercontent.com/wmgeolab/geoBoundaries/729d59ed25f7bcc7664fc6ca58755b4e8567e80c/releaseData/gbOpen/UKR/ADM0/geoBoundaries-UKR-ADM0-all.zip'
        os.environ['S3_PATH'] = 's3://ds-data-projects/test_mercy'
        os.environ['COUNTRY'] = 'UKR'
        result = app.handler(None, None)
        self.assertEqual(200, result['statusCode'])