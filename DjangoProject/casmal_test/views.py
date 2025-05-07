# views.py
from rest_framework.viewsets import ModelViewSet
from .models import Experiment
from .serializers import ExperimentSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status


class ExperimentViewSet(ModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer

    @swagger_auto_schema(
        responses={201: ExperimentSerializer}
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
