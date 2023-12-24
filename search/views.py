from django.shortcuts import render
from sellers.models import sell
# Create your views here.

def search_results(request):
    if 'search' in request.GET:
        query = request.GET['search']
        results = sell.objects.filter(productname__icontains=query)
        return render(request, 'search_results.html', {'results': results, 'query': query})
    else:
        return render(request, 'search_results.html')  
