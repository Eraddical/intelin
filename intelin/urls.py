from django.urls import path
from .views import base_views, argument_views, refute_views

app_name = 'intelin'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:argument_id>/', base_views.detail, name='detail'),

    path('argument/create/', argument_views.argument_create, name='argument_create'),
    path('argument/modify/<int:argument_id>', argument_views.argument_modify, name='argument_modify'),
    path('argument/delete/<int:argument_id>', argument_views.argument_delete, name='argument_delete'),
    path('argument/vote/<int:argument_id>', argument_views.argument_vote, name='argument_vote'),

    path('refute/create/<int:argument_id>/', refute_views.refute_create, name='refute_create'),
    path('refute/modify/<int:refute_id>/', refute_views.refute_modify, name='refute_modify'),
    path('refute/delete/<int:refute_id>/', refute_views.refute_delete, name='refute_delete'),
    path('refute/vote/<int:refute_id>/', refute_views.refute_vote, name='refute_vote'),
]
