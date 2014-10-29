from django.conf.urls import patterns, include, url
from django.contrib import admin
from mrCheck.views import *
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^patient/$', patient_view.as_view()),
    url(r'^patient/(?P<id>\d+)/$', patient_detail_view.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework'))
    ]

#urlpatterns = patterns('',
    ## Examples:
    ## url(r'^$', 'mriWeb.views.home', name='home'),
    ## url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),

    #url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),


    #url(r'^patient/$', patient_view.as_view()),
    #url(r'^patient/(?P<id>\d+)/$', patient_detail_view.as_view()),
    #url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),


#)

##urlpatterns += patterns('',
            ##url(r'^api-auth/', ))

##urlpatterns += patterns('',
            ##url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
            ##)
