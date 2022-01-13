from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
from rest_framework import permissions

from .serializers import TodoSerializer


@permission_classes([permissions.IsAuthenticated])
class TodoViewSet(ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        request = self.request
        queryset = request.user.todos.all()
        if "sort" in request.query_params:
            order = ""
            if "order" in request.query_params:
                order = "-" if request.query_params["order"] == "desc" else ""
            order += request.query_params["sort"]
            return queryset.order_by(order)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
