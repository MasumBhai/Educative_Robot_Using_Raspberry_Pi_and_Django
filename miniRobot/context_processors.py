from .models import *

def add_variable_to_context(request):
    try:
        companyInfo = project_team.objects.get(team_code__exact="coded by Brainy_Fool(+8801551805248)")
    except:
        companyInfo = project_team.objects.all()

    everyWhere = {
        'companyInfo': companyInfo,
    }
    return everyWhere