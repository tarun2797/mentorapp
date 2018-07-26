from django.test import TestCase

# Create your tests here.
from onlineapp.models import college
from onlineapp.serializers import *

class college_serializer_tester(TestCase):
    def setUp(self):
        self.college_data = college.objects.create(name='IndInsTec',location='Hyd',acronym='IIT',contact='iit@gmail.com')
        self.college_serialize = collegeSerializer(self.college_data)
    def test_valid_data(self):
        pass
        self.assertEqual( self.college_serialize,{'name':'IndInsTec','location':'Hyd','acronym':'IIT','contact':'iit@gmail.com'})
    def test_invalid_data(self):
        pass
        self.assertNotEqual(self.college_serialize,{'name': 'IndInsTec1', 'location': 'Hyd', 'acronym': 'IIT', 'contact': 'iit@gmail.com'})