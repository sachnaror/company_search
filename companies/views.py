from django.shortcuts import render

from .forms import CompanySearchForm
from .models import Company
from .search_indexes import CompanyIndex


def index(request):
    return render(request, 'companies/index.html')

def search(request):
    query = request.GET.get('query')
    if query:
        search_results = CompanyIndex.search().query("match", registered_name=query)[:10]
        return render(request, 'companies/search_results.html', {'results': search_results})
    return render(request, 'companies/index.html')

def company_detail(request, registration_number):
    company = Company.objects.get(registration_number=registration_number)
    return render(request, 'companies/company_detail.html', {'company': company})



def company_add(request):
    if request.method == 'POST':
        form = CompanySearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanySearchForm()
    return render(request, 'companies/company_add.html', {'form': form})

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})
