from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import include, path

router = DefaultRouter()
router.register(r'category', CategoryView)
router.register(r'trip', TripView)
router.register(r'image', ImageView)
router.register(r'customUser', CustomUserView)
router.register(r'booking', BookingView)
router.register(r'payment', PaymentView)
router.register(r'availability', AvailabilityView)
router.register(r'conversation-history', ConversationHistoryViewSet)
router.register(r'conversations/(?P<history_id>\d+)/', ConversationViewSet, basename='conversation')

urlpatterns = [
    path('api/', include(router.urls)),
    path('tripScore/<int:tripId>/', ScoreAverageView.as_view(), name='trip-score-average'),
    path('api/conversations/<int:user_id>/', ConversationHistoryViewSet.as_view({'get': 'list'}), name='conversation_history_list'),
    path('chatbot/', ChatBotAPIView.as_view(), name='chatbot'),
    path('api/', include(router.urls)),
]
