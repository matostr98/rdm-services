from rest_framework import routers
from person_service import views as person_views

router = routers.DefaultRouter()
router.register(r'persons', person_views.PersonViewset)