from django.urls import path
from user_app.api.views import registration_view, logout_view, userListView, AllUsersBorrowedBooksView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup/', registration_view, name="signup"),
    path('logout/', logout_view, name="logout_account"),
    path('login/', obtain_auth_token, name="login_account"),
    path('users/lists/', userListView.as_view(), name="userList"),
    path('all-users-borrowed-books/', AllUsersBorrowedBooksView.as_view(), name='all-users-borrowed-books'),
]
