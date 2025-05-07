from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView

from DjangoProject.model_test.models import Book, Author

from DjangoProject.model_test.serializers import BookSerializer, AuthorSerializer


# Create your views here.
class ModelTest(APIView):

    def get(self, request):
        # data = BookSerializer(Book.objects.all(),many=True).data
        # return JsonResponse(data, safe=False)
        data = AuthorSerializer(Author.objects.all(), many=True).data
        return JsonResponse(data, safe=False)


from ninja import NinjaAPI
from .models import Experiment, Dataset
from .schemas import ExperimentOut, ExperimentCreate, DatasetOut

api = NinjaAPI()


@api.get("/datasets", response=list[DatasetOut])
def list_datasets(request):
    return Dataset.objects.all()


@api.post("/experiments", response=ExperimentOut)
def create_experiment(request, data: ExperimentCreate):
    dataset = Dataset.objects.get(id=data.dataset_id)
    exp = Experiment.objects.create(
        name=data.name,
        dataset=dataset,
        config=data.config
    )
    return exp



@api.get("/experiments", response=list[ExperimentOut])
def list_experiments(request):
    return Experiment.objects.select_related("dataset").all()
