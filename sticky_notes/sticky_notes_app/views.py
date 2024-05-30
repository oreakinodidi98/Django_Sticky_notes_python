from django.shortcuts import render, redirect, get_object_or_404
from .models import Stick_notes, Author
from .forms import Stick_notesForm, AuthorForm

# Create your views here.

def home(request):
    notes = Stick_notes.objects.all()
    # context dictionary to pass data to template
    context = {
        'notes': notes,
        'page_title': 'Home Page'
               }
    return render(request, 'home.html', context)
# views for CRUD functionality

# view for creating notes
def notes_create(request):
    # if request is post then save the data
    if request.method == "POST":
        # form object
        note_form = Stick_notesForm(request.POST)
        # if form is valid then save the data
        if note_form.is_valid():
            # save the data to database
            note= note_form.save(commit=False)
            # if user is authenticated then set the author
            if request.user.is_authenticated:
                # set the author
                note.author = request.user
                # save the data
            note.save()
            # redirect to home page
            return redirect('home') 
    else:
        # if request is get then create the form object
        note_form = Stick_notesForm()
    return render(request, 'notes_form.html', {'note_form': note_form})

# views for details of specific notes
def notes_detail(request, pk):
    # get the notes object
    note = get_object_or_404(Stick_notes, pk=pk)
    # context dictionary to pass data to template
    context = {
        'note': note
    }
    return render(request, 'notes_detail.html', context)

# view for updating notes
def notes_update(request, pk):
    # get the notes object
    note = get_object_or_404(Stick_notes, pk=pk)
    # if request is post then save the data
    if request.method == "POST":
        # form object
        note_form = Stick_notesForm(request.POST, instance=note)
        # if form is valid then save the data
        if note_form.is_valid():
            # save the data to database
            note = note_form.save(commit=False)
            # if user is authenticated then set the author
            if request.user.is_authenticated:
                # set the author
                note.author = request.user
                # save the data
            note.save()
            # redirect to home page
            return redirect('home') 
    else:
        # if request is get then create the form object
        note_form = Stick_notesForm(instance=note)
    return render(request, 'notes_form.html', {'note_form': note_form})

# view for deleting notes
def notes_delete(request, pk):
    # get the notes object
    note = get_object_or_404(Stick_notes, pk=pk)
    # delete the data
    note.delete()
    # redirect to home page
    return redirect('home')
    
# view for signing in user
def author_create(request):
    #get login object (author)
    login = Author.objects.all()
    # if request is post then save the data
    if request.method == "POST":
        # form object
        author_form  = AuthorForm(request.POST)
        # if username matches with the database username and password matches with the database password then redirect to home page and display login successful
        for i in login:
            if i.username == request.POST['username'] and i.password == request.POST['password']:
                # display login successful in terminal
                print("login successful")
                return redirect('home')
            else:
                # display login failed in terminal
                print("login failed")
                # return back to login page
                return redirect('author_create')  
    else:
        # if request is get then create the form object
        author_form = AuthorForm()
    # context dictionary to pass data to template
    context = {
        'page_title': 'Login Page',
        'author_form': author_form
               }
    return render(request, 'login.html', context)

# view for registering user
def author_register(request):
   
    # if request is post then save the data
    if request.method == "POST":
        # form object
        author_form = AuthorForm(request.POST)
        # if form is valid then save the data
        if author_form.is_valid():
            # save the data to database
            author_form.save()
            # redirect to login page
            return redirect('author_create') 
    else:
        # if request is get then create the form object
        author_form = AuthorForm()
    # context dictionary to pass data to template
    context = {
        'page_title': 'Login Page',
        'author_form': author_form
               }
    return render(request, 'register.html', context)

# view for signing out user
def author_logout(request):
    return redirect('home')

# view for

