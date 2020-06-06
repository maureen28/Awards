from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project, Profile

# Create your tests here.
class ProfileTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.user = User.objects.create_user('Happy', 'secret')
        cls.profile1 = Profile.objects.create(profile_pic='https://unsplash.it/1200/768.jpg?image=1033',
                                     bio='Like it',
                                     user=cls.user)

    # Testing  instance
    def test_instance(self):
       self.assertTrue(isinstance(self.profile1, Profile))

    # Testing Save Method
    def save_method_test(self):
        self.profile1.save_Profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

# Project Test

class ProjectTestClass(TestCase):
      # Set up method
    @classmethod
    def setUpTestData(cls):
        cls.new_project = Project.objects.create(title="new_project",my_image='https://unsplash.it/1200/768.jpg?image=76',
                              description='Portfolio', country='ghana',link='http://photogall.com', profile=cls.profile1)

    # Testing  instance
    def test_instance(self):
       self.assertTrue(isinstance(self.new_project, Project))

    # Testing Save Method
    def save_method_test(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)
 
    # Testing Delete Method
    def delete_method_test(self):
        self.new_project.delete_project()
        projects = Project.search_project('test')
        self.assertTrue(len(projects) < 1)

    # get method
    def get_projects_test(self):
        self.new_project.save()
        projects = Project.all_project()
        self.assertTrue(len(projects) > 0)

    def test_search_post(self):
        self.new_project.save()
        projects = Project.search_project('test')
        self.assertTrue(len(projects) > 0)


# Rating
class RatingTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.new_project = Project.objects.create(title="new_project",my_image='https://unsplash.it/1200/768.jpg?image=76',
                              description='Portfolio', country='ghana',url='http://photogall.com', profile=cls.profile1)
        cls.profile1 = Profile.objects.create(profile_pic='https://unsplash.it/1200/768.jpg?image=1033',
                                     bio='Like it',
                                     user=cls.new_user)
        cls.rating = Rating.objects.create(id=1, design=6, usability=7, content=9, profile=cls.profile1, new_project=cls.new_project)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_get_new_project_rating(self, id):
        self.rating.save()
        rating = Rating.get_ratings(new_project_id=id)
        self.assertTrue(len(rating) == 1)

    # Teardown
    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()
        User.objects.all().delete()
        Rating.objects.all().delete()
