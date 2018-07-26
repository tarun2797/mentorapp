from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from onlineapp.views import *
from onlineapp.models import *
from django.shortcuts import render, get_object_or_404
from django import forms
from django.urls import reverse_lazy
from django.shortcuts import *

class CollegeView(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,*args,**kwargs):
        #import ipdb
        #ipdb.set_trace()
        colleges = college.objects.values('id','name','acronym')
        context={
            'college_details':colleges
        }
        return render(
            request,
            template_name = 'bootstrap.html',
            context=context,
        )
        pass

class CollegeDetailsView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    model = college
    template_name = 'college_details.html'

    def get_object(self, queryset=None):
        return get_object_or_404(college,**self.kwargs)

    def get_context_data(self, **kwargs):
        context = super(CollegeDetailsView,self).get_context_data(**kwargs)
        #print("context=",context)
        college = context.get('college')
        #print("college=",college)
        #self.model.objects.values()
        students = list(college.student_set.order_by("-mocktest1__total"))
        #print(students)
        #import ipdb
        #ipdb.set_trace()
        context.update({
            'students':students,
            'user_permissions':self.request.user.get_all_permissions()
        })

        return context

class AddCollege(LoginRequiredMixin,forms.ModelForm):
    class Meta:
        model = college
        exclude = ['id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'acronym': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'})
        }

class AddStudent(LoginRequiredMixin,forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['id','dob','college']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':""}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""}),
            'db_folder': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""}),
            #'college':forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""}),
            'dropped_out':forms.CheckboxInput(attrs={'class':'form-check-input'})
        }

class CreateCollegeView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model=college
    # import ipdb
    # ipdb.set_trace()
    form_class=AddCollege
    template_name='colleges_html.html'
    success_url=reverse_lazy("onlineapp:bootstrap.html")

class MockTestForm(LoginRequiredMixin,forms.ModelForm):
    class Meta:
        model = MockTest1
        exclude = ['id','students','total']
        widgets = {
            'problem1': forms.TextInput(attrs={'class':'form-control','placeholder':""}),
            'problem2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""}),
            'problem3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""}),
            'problem4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
        }

class createCollegeView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    '''
    permission_required = 'onlineappgeneric.add_college'
    permission_denied_message = "user doesn't have permission to create a college"
    raise_exception = True
    '''
    model = college
    template_name = 'colleges_html.html'
    form_class = AddCollege
    success_url = reverse_lazy('onlineapp:colleges_html.html')

class createStudentView(LoginRequiredMixin,CreateView):
    '''
    login_url = '/login/'
    permission_required = 'onlineappgeneric.add_college'
    permission_denied_message = "user doesn't have permission to create a college"
    raise_exception = True
    model = Student
    template_name = 'student_form.html'
    form_class = AddStudent
    # success_url = reverse_lazy('onlineapp:students_html.html')

    def get_context_data(self, *args, **kwargs):
        context = super(createStudentView, self).get_context_data(**kwargs)
        student_form = context.get('form')
        mocktest_form = MockTestForm()

        #print("context = ",context)
        #print(college_name[0]['acronym'])
        #print("check = ",context['form'].fields)
        #print("name value = ",self.cleaned_data['name'])

        context.update({
            'student_form':student_form,
            'test_form':mocktest_form,
        })

        return context

    def post(self, request, *args, **kwargs):

        COLLEGE = get_object_or_404(college, pk=kwargs['pk'])
        print(COLLEGE)
        student_form = AddStudent(request.POST)
        mocktest_form = MockTestForm(request.POST)

        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.college = COLLEGE
            student.save()
            if mocktest_form.is_valid():
                mocktest = mocktest_form.save(commit=False)
                mocktest.student = Student.objects.get(id=student.id)
                import ipdb
                ipdb.set_trace()
                tempdata = models.IntegerField()
                tempdata = sum(mocktest_form.cleaned_data.values())
                mocktest.total = tempdata
                mocktest.save()

        return redirect('/colleges/%d'%'college_id')
    '''
    login_url = '/login/'
    model=Student
    template_name='student_form.html'
    form_class=AddStudent

    def get_context_data(self, **kwargs):
        context=super(createStudentView, self).get_context_data(**kwargs)
        test_form = MockTestForm()
        context.update({
            'student_form':context.get('form'),
            'test_form': test_form,
        })
        return context

    def post(self, request, *args, **kwargs):
        COLLEGE=get_object_or_404(college,pk=kwargs.get('pk'))
        student_form=AddStudent(request.POST)
        test_form=MockTestForm(request.POST)

        if student_form.is_valid():
            student=student_form.save(commit=False)
            #print("student = ",student)
            student.college=COLLEGE
            student.save()

            if test_form.is_valid():
                score=test_form.save(commit=False)
                score.total=sum(test_form.cleaned_data.values())
                score.students=student
                score.save()
        return redirect('/colleges/')

class EditStudentView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    '''
    model=Student
    form_class=AddStudent
    template_name="student_form.html"

    def get_context_data(self, **kwargs):
        context = super(EditStudentView, self).get_context_data(**kwargs)
        #print("toooooooooooooooooooooooo")
        student_form = context.get('student')
        student=get_object_or_404(Student,email=context['student_form'].initial['email'])
        MockTest=get_object_or_404(MockTest1,students=student)
        test_form = MockTestForm(instance=MockTest)
        context.update({
            'student_form': context.get('form'),
            'test_form': test_form,
        })

        return context

    def post(self, request, *args, **kwargs):
        student = Student.objects.get(pk=kwargs.get('pk'))
        print("check student = ",student)
        form = AddStudent(request.POST, instance=student)
        test_form = MockTestForm(request.POST, instance=student.mocktest1)
        test = test_form.save(False)
        test.total = sum(test_form.cleaned_data.values())
        form.save()
        test_form.save()
        return redirect('/colleges/')
        '''
    model=Student
    form_class=AddStudent
    template_name="student_form.html"

    def get_context_data(self, **kwargs):
        context = super(EditStudentView, self).get_context_data(**kwargs)
        print("context = ",context)
        student_form = context.get('student')
        print("sf = ",student_form)
        test_form = MockTestForm(instance=student_form.mocktest1)
        print(context.get('form'))
        context.update({
            'student_form': context.get('form'),
            'test_form': test_form,
        })

        return context

    def post(self, request, *args, **kwargs):
        student = Student.objects.get(pk=kwargs.get('pk'))
        print("pk = ",student)
        form = AddStudent(request.POST, instance=student)  # student form
        test_form = MockTestForm(request.POST, instance=student.mocktest1) # mocktest form

        print("stu_form = ",form)
        print("mock_form = ",test_form)

        test = test_form.save(False)
        test.total = sum(test_form.cleaned_data.values())

        form.save() #student form
        test_form.save()  # mocktest form

        #return redirect('onlineapp:redirect_page', pk=self.kwargs.get('pk'))
        return redirect('/colleges/')

class DeleteStudentView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    model=Student
    success_url = reverse_lazy('onlineapp:bootstrap.html')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.delete(request,args,kwargs)
        #print("check for id = ",self.kwargs.get('college_id'))
        return redirect('onlineapp:redirect_page',pk=self.kwargs.get('clg_id'))
        #return redirect('/colleges/')

class EditCollegeView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    model = college
    form_class = AddCollege
    template_name = 'colleges_html.html'
    success_url = reverse_lazy('onlineapp:colleges_html.html')
