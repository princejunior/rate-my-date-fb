from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),
    
    # Authentication URLs
    path('signup/', views.signup, name='signup'),  # User signup
    path('login/', views.user_login, name='login'),  # User login
    path('logout/', views.user_logout, name='logout'),  # User logout
    
    # Profile Management
    path('add_user_profile/', views.add_user_profile, name='add_user_profile'),  # Create a new person profile UI
    path('edit_profile/', views.edit_user_profile, name='edit_user_profile_w'),  # Create a new person profile UI
    path('profile/edit/<str:user_email>/', views.edit_user_profile, name='edit_user_profile'),
    path('profile/', views.user_profile, name='user_profile_w'),  # Create a new person profile UI
    path('profile/<str:user_email>/', views.user_profile, name='user_profile'),
     # People
    path('person/', views.createNewPerson, name='createnewperson'),  # Create a new person profile UI
    path('create_person/', views.create_person, name='create_person'),  # Create a new person profile backend
    path('search/', views.search_person, name='searchperson'),  # Search for persons
    path('explore/', views.explore, name='explore'),  # Explore list of persons
    path('viewperson/', views.view_person, name='viewperson'),  # View person profile (unused/placeholder)
    path('viewperson/<str:person_id>/', views.view_person, name='view_person'),  # View person profile by ID
    
    # Posts and Comments
    path('create_post/<str:person_id>/', views.create_post, name='create_post'),  # Create a post for a person
    path('add_comment/', views.add_comment, name='add_comment'),  # Add a comment to a post
    
    # GOOGLE
    path('accounts/signup/google/', views.google_signup, name='google_signup'),
    # path('accounts/profile/', views.profile, name="profile"),
    # path('accounts/other/', views.other, name="other"),
]
