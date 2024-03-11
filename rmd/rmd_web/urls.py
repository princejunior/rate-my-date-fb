from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),
    
    # Authentication URLs
    path('signup/', views.signup, name='signup'),  # User signup
    path('login/', views.user_login, name='login'),  # User login
    path('logout/', views.user_logout, name='logout'),  # User logout
    
    # People/Profile Management
    path('person/', views.createNewPerson, name='createnewperson'),  # Create a new person profile UI
    path('create_person/', views.create_person, name='create_person'),  # Create a new person profile backend
    path('search/', views.search_person, name='searchperson'),  # Search for persons
    path('explore/', views.explore, name='explore'),  # Explore list of persons
    path('viewperson/', views.view_person, name='viewperson'),  # View person profile (unused/placeholder)
    path('viewperson/<str:person_id>/', views.view_person, name='view_person'),  # View person profile by ID
    
    # Posts and Comments
    path('create_post/<str:person_id>/', views.create_post, name='create_post'),  # Create a post for a person
    path('add_comment/', views.add_comment, name='add_comment'),  # Add a comment to a post
]
