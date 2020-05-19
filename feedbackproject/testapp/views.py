from django.shortcuts import render
from testapp.forms import FeedbackForm

# Create your views here.
def feedback_form_view(request):
    feedback_submitted=False
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            print('Basic Validation Completed and Printing Data')
            print('Name:',form.cleaned_data['name'])
            print('RollNo:',form.cleaned_data['rollno'])
            print('Email:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback'])
            feedback_submitted=True
    form=FeedbackForm()
    return render(request,'testapp/feedback.html',{'form':form,'feedback_submitted':feedback_submitted})
