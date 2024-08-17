from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from elasticsearch import Elasticsearch

from .models import Company  # Update this with your actual model
from .search_indexes import CompanyIndex

# Initialize Elasticsearch client
es = Elasticsearch(['http://localhost:9200'])


def index(request):
    return render(request, 'companies/index.html')

def search(request):
    query = request.GET.get('query')
    if query:
        search_results = CompanyIndex.search().query("match", name=query)[:10]
        return render(request, 'companies/search_results.html', {'results': search_results})
    return render(request, 'companies/index.html')



from django.shortcuts import get_object_or_404, render

from .models import Company  # Ensure this points to your actual Company model


def company_detail(request, registration_number):
    company = get_object_or_404(Company, registration_number=registration_number)
    return render(request, 'companies/company_detail.html', {'company': company})

def search_suggestions(request):
    query = request.GET.get('query', '')
    if len(query) < 3:
        return JsonResponse({'suggestions': []})

    results = es.search(index='company_index', body={
        'query': {
            'match': {
                'name': {
                    'query': query,
                    'fuzziness': 'AUTO'
                }
            }
        },
        'size': 10
    })

    suggestions = [
        {
            'name': hit['_source']['name'],
            'registration_number': hit['_source']['registration_number']
        }
        for hit in results['hits']['hits']
    ]
    return JsonResponse({'suggestions': suggestions})



def search(request):
    query = request.GET.get('query', '')
    if query:
        results = es.search(index='company_index', body={
            'query': {
                'match': {
                    'name': {
                        'query': query,
                        'fuzziness': 'AUTO'
                    }
                }
            },
            'size': 10
        })

        # Prepare the results for rendering in the template
        hits = results['hits']['hits']
        companies = [
            {
                'name': hit['_source']['name'],
                'registration_number': hit['_source']['registration_number']
            }
            for hit in hits
        ]

        return render(request, 'companies/search_results.html', {'results': companies})
        return render(request, 'companies/index.html')

