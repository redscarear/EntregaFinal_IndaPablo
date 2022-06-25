from django.urls import path
from mensajeria import views
app_name='mensajeria'
urlpatterns = [
    		path('mensajeria', views.MensajeriaListView.as_view(), name='mensajeria-list'),
    		path('mensajeria/add/', views.MensajeriaCreateView.as_view(), name='mensajeria-add'),
    		path('mensajeria/<int:pk>/detail', views.MensajeriaDetailView.as_view(), name='mensajeria-detail'),
    		path('mensajeria/<int:pk>/update', views.MensajeriaUpdateView.as_view(), name='mensajeria-update'),
    		path('mensajeria/<int:pk>/delete', views.MensajeriaDeleteView.as_view(), name='mensajeria-delete'),
			path('mensajeria/enviados', views.MensajeriaEnviadosView.as_view(), name='mensajeria-enviados'),
			path('mensajeria/recibidos', views.MensajeriaRecibidosView.as_view(), name='mensajeria-recibidos')
]