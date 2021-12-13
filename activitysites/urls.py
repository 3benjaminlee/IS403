from django.urls import path
from .views import indexPageView
from .views import couplesPageView
from .views import editPageView
from .views import updateActivityPageView
from .views import deleteActivityPageView
from .views import addActivityPageView

urlpatterns = [
    path("addactivity", addActivityPageView, name="addActivity"),
    path("editactivity/<int:id>", editPageView, name="editactivity"),
    path("couples/", couplesPageView, name="couples"),
    path("updateActivity/", updateActivityPageView, name="updateActivity"),
    path("deleteActivity/<int:id>", deleteActivityPageView, name="deleteActivity"),
    path("", indexPageView, name="index")
]
