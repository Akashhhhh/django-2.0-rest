from django.contrib import admin
from .models import Poll, Choice
from django.urls import path

from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, PollViewSet, ChoiceListByPollId

from rest_framework.routers import DefaultRouter

# if we are using viewset then it doesn't need to add the url in the url patterns
router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

admin.site.register(Poll)
admin.site.register(Choice)

urlpatterns = [
    # path("polls/", polls_list, name="polls_list"),
    # path("polls/<int:pk>/", polls_detail, name="polls_detail") 
    
    #path("polls/", PollList.as_view(), name="polls_list"),
    #path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("vote/", CreateVote.as_view(), name="create_vote"),
    path("polls/<int:pk>/choices/", ChoiceListByPollId.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    

]

urlpatterns += router.urls


