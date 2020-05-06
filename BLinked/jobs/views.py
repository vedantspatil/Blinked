from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from blink.models import Job, Qualification, User, Education

def index(request):
    """
    renders the index page of job

    :param request: request Object from Client
    :return: index page with multiple jobs
    """
    job = Job.objects.all()

    template = loader.get_template('jobs/jobs2.html')
    context = {
        'page': 'jobs',
        'joblist': job
    }
    return HttpResponse(template.render(context, request))


def job(request, jobId):
    """
    renders the job page with job id = jobID

    :param request: request Object from Client
    :param jobId: id of the job requested for
    :return: page of that specific jobID
    """
    myJob = Job.objects.get(id=jobId)
    degrees = Qualification.objects.filter(job=myJob)

    profileUser = None
    if request.user.is_authenticated:
        profileUser = User.objects.get(username=request.user.username)

    qualifications = []


    canApply = True

    for degree in degrees:
        eligible = False
        if profileUser:
            education = Education.objects.filter(user=profileUser, degree=degree.degree)
            if education.exists():
                for ed in education:
                    eligible = eligible or ed.legitimate
        canApply = canApply and eligible
        qualifications.append({'degree': degree.degree, 'eligible': eligible})

    if profileUser is None:
        canApply = True

    template = loader.get_template('jobs/job_details.html')
    context = {
        'page': myJob.title,
        'load_job': myJob,
        'qualifications': qualifications,
        'canApply': canApply
    }
    return HttpResponse(template.render(context, request))
