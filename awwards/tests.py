from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project, Profile

# Create your tests here.
class ProfileTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.profile1 = Profile.objects.create(profile_pic='https://unsplash.it/1200/768.jpg?image=1033',
                                     bio='Like it',
                                     user=cls.new_user)

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
                              description='Portfolio', country='ghana',url='http://photogall.com', profile=cls.profile1)

    # Testing  instance
    def test_instance(self):
       self.assertTrue(isinstance(self.new_project, Project))

    # Testing Save Method
    def save_method_test(self):
        self.new_project.save_Project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    # Teardown
    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()

    # Testing Delete Method
    def delete_method_test(self):
        self.new_project.save_image()
        filtered_img = Image.objects.filter(name='Lancelin')
        Image.delete_image(filtered_img)
        final_images = Image.objects.all()
        self.assertTrue(len(final_images) == 0)

    # Testing Update Method
    def update_method_test(self):
        self.new_project.save_image()
        filtered_img = Image.update_image('Lancelin','Dunes')
        fetched = Image.objects.get(name='Dunes')
        self.assertEqual(fetched.name,'Dunes')

    # Testing get image Method
    def get_image_by_id_test_method(self):
        self.new_project.save_image()
        fetched_image = Image.get_image_by_id(1)
        self.assertEqual(fetched_image.id,1)

    # Testing search image Method
    def search_by_Project_test_method(self):
        self.new_project.save_image()
        fetch_specific = Project.objects.get(title='Food')
        self.assertTrue(fetch_specific.title=='Food')


    # Testing filter Profile Method
    def filter_by_Profile_test_method(self):
        self.new_project.save_image()
        fetch_specific = Profile.objects.get(country='Tanzania')
        self.assertTrue(fetch_specific.country=='Tanzania')

    #  test all images
    def display_all_images_test_method(self):
        self.new_project.save_image()
        final_images = Image.retrieve_all()
        self.assertEqual(final_images.name,'Lancelin')

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