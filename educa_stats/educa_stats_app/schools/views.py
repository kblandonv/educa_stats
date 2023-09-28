from django.shortcuts import render
from .models import School

# Create your views here.

def school_list(request):
    schools = School.objects.all()
    return render(request, 'schools/school_list.html', {'schools': schools})

def school_detail(request, pk):
    school = School.objects.get(pk=pk)
    return render(request, 'schools/school_detail.html', {'school': school})

def school_search(request):
    return render(request, 'schools/school_search.html')

def school_search_results(request):
    return render(request, 'schools/school_search_results.html')

def school_search_results_detail(request):
    return render(request, 'schools/school_search_results_detail.html')

def school_search_results_detail_add(request):
    return render(request, 'schools/school_search_results_detail_add.html')

def school_search_results_detail_add_success(request):
    return render(request, 'schools/school_search_results_detail_add_success.html')

def school_search_results_detail_add_fail(request):
    return render(request, 'schools/school_search_results_detail_add_fail.html')

def school_search_results_detail_edit(request):
    return render(request, 'schools/school_search_results_detail_edit.html')

def school_search_results_detail_edit_success(request):
    return render(request, 'schools/school_search_results_detail_edit_success.html')

def school_search_results_detail_edit_fail(request):
    return render(request, 'schools/school_search_results_detail_edit_fail.html')

def school_search_results_detail_delete(request):
    return render(request, 'schools/school_search_results_detail_delete.html')

def school_search_results_detail_delete_success(request):
    return render(request, 'schools/school_search_results_detail_delete_success.html')

def school_search_results_detail_delete_fail(request):
    return render(request, 'schools/school_search_results_detail_delete_fail.html')

def map_view(request):
    # Capture all schools in the database
    schools = School.objects.all()
    return render(request, 'schools/map.html', {'schools': schools})

