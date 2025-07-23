from django.urls import path

from .views import note_detail, note_list, user_detail, users_list

urlpatterns = [
    path('', view=note_list, name='note_list'),
    path('users/', view=users_list, name="users_list"),
    path('notes/<int:note_id>/', view=note_detail, name='note_detail'),
    path('users/<int:user_id>/', view=user_detail, name='user_detail')
]
