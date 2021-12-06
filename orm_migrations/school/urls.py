from django.urls import path
import debug_toolbar
from django.urls import include, path
from school.views import students_list

urlpatterns = [
    path('', students_list, name='student'),
    path('__debug__/', include(debug_toolbar.urls))
]

