from django.shortcuts import render, redirect
from .forms import InvestForm
from rest_framework.response import Response
from rest_framework import status
from .serializers import InvestSerializer
from rest_framework.views import APIView
from .models import Invest


class InvestView(APIView):
    def get(self, request):
        if request.method == 'GET':
            invests = Invest.objects.all()
            print(1)
            print(invests)
            serializer = InvestSerializer(invests, many=True)
            return Response({"Invests": serializer.data}, status=200)

    def post(self, request):
        if request.method == 'POST':
            serializer = InvestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)

            return Response(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        if request.method == 'PUT':
            pk = kwargs.get("pk", None)
            if not pk:
                return Response({"error": "Method PUT not allowed"})

            try:
                instance = Invest.objects.get(id=pk)
            except:
                return Response({"error": "Object does not exists"})
            serializer = InvestSerializer(data=request.data, instance=instance)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if request.method == 'DELETE':
            data = {
                'id': request.data.get('id')
            }
            if data['id'] is None:
                return Response({"error": "Wrong data"}, status=status.HTTP_400_BAD_REQUEST)
            try:
                a = Invest.objects.get(id=data['id'])
            except:
                return Response({"error": "Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)
            a.delete()
            return Response(request.data, status=200)


def index(request):
    investments = Invest.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Вся аналитика', 'investments': investments})


def create(request):
    error = ''
    if request.method == 'POST':
        form = InvestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Ошибка в заполнении"
    form = InvestForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def delete(request):
    if request.method == 'POST':
        ge = request.POST.get('id_field')
        try:
            a = Invest.objects.get(id=ge)
        except:
            return redirect('home')
        a.delete()
        return redirect('home')
    return render(request, 'main/delete.html')


def update(request):
    error = ''
    if request.method == 'POST':
        ge = request.POST.get('id_field')
        form = InvestForm(request.POST)
        if form.is_valid():
            name2 = form.cleaned_data.get("name")
            old = form.cleaned_data.get("old_price")
            new = form.cleaned_data.get("new_price")
            gro = form.cleaned_data.get("growth")
            rec = form.cleaned_data.get("recommendations")
            try:
                Invest.objects.filter(id=ge).update(name=name2, old_price=old, new_price=new, growth=gro,
                                                    recommendations=rec)
            except:
                return redirect('home')
            return redirect('home')
    form = InvestForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/update.html', context)
