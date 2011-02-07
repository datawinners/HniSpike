import csv
from django.contrib.auth import logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template.loader import get_template
from django.template import Context
from mongoengine.django.auth import User
from bookmarks.forms import RegistrationForm
from bookmarks.models import Bookmarks

def main_page(request):
#    template = get_template('main_page.html')
    variables=RequestContext(request,{
        'user':request.user,
        'page_body' : u'Where you can store and share bookmarks'})
#    output = template.render(variables)
#    return HttpResponse(output)
    return render_to_response(
        'main_page.html',
        variables
    )

def is_user_bookmark(bookmark,username):
    return bookmark.user.username==username

def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except :
        raise Http404(u'Requested User not found')


#    bookmarks = user.bookmarks_set.all()
    bookmarks = [user_bookmark for user_bookmark in Bookmarks.objects if is_user_bookmark(user_bookmark,username)]


    variables=RequestContext(request,{
        'username' : username,
        'bookmarks' : bookmarks})
#    return HttpResponse(output)
    return render_to_response(
            'user_page.html',
            variables
        )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/login")

def register_page(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            return HttpResponseRedirect("/register/success")
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('registration/register.html',variables)

def export_bookmarks_to_csv(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition']='attachment;filename=myfile.csv'
    writer = csv.writer(response)
    writer.writerow(['title','link'])
    writer.writerow(['second','two','2'])
    return response