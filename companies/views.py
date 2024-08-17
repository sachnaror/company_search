from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from elasticsearch import Elasticsearch

from .models import Company
from .search_indexes import CompanyIndex


def index(request):
    return render(request, 'companies/index.html')

def search(request):
    query = request.GET.get('query')
    if query:
        search_results = CompanyIndex.search().query("match", name=query)[:10]
        return render(request, 'companies/search_results.html', {'results': search_results})
    return render(request, 'companies/index.html')

from django.shortcuts import get_object_or_404, render

from .models import Company  # Update this with your actual model


def company_detail(request, registration_number):
    company = get_object_or_404(Company, registration_number=registration_number)
    return render(request, 'companies/company_detail.html', {'company': company})
def search_suggestions(request):
    query = request.GET.get('query', '')
    if len(query) < 3:
        return JsonResponse({'suggestions': []})

    search_results = CompanyIndex.search().query("match", name=query)[:10]
    suggestions = [{'id': company.id, 'name': company.name} for company in search_results]
    return JsonResponse({'suggestions': suggestions})


from django.http import JsonResponse
from elasticsearch import Elasticsearch

# Initialize Elasticsearch client
es = Elasticsearch(['http://localhost:9200'])

def search(request):
    query = request.GET.get('query', '')
    if query:
        results = es.search(index='your_index_name', body={
            'query': {
                'match': {
                    'name': {
                        'query': query,
                        'fuzziness': 'AUTO'
                    }
                }
            }
        })
        suggestions = [hit['_source']['name'] for hit in results['hits']['hits']]
        return JsonResponse({'suggestions': suggestions})
    return JsonResponse({'suggestions': []})
