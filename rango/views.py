from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if less than 5.
    # Place the list in our context_dict dictionary (with our boldmessage!)
    # that will be passed to the template engine.

    
    # queries the Category model to retrieve the top five categories. '-like' is in descending order.  
    # 'like' will be the in ascending order

    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories':category_list,'pages':page_list}

    context_dict = {}

    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    # Render the response and send it back!
    return render(request, 'rango/index.html',context=context_dict)
    # return HttpResponse("Rango says here is the about page!")

def about(request):
    # return HttpResponse("Rango says here is the about page.")
    context_dict = {'boldmessage':'This tutorial has been put together by Jing Xue'}
    return render(request, 'rango/about.html',context=context_dict)

def show_category(request,category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
   
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # The .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all of the associated pages.
        # The filter() will return a list of page objects or an empty list.
        pages = Page.objects.filter(category=category)
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None
# Go render the response and return it to the client.
    return render(request, 'rango/category.html', context=context_dict)

'''
Django的表单处理机制处理通过HTTP POST请求从用户浏览器返回的数据。它不仅可以将表单数据保存到所选模型中，
还可以自动为每个表单字段生成任何错误消息（如果需要）。这意味着Django不会存储任何丢失信息的提交表单，这些
信息可能会对数据库的引用完整性造成问题⁵. 例如，在“类别名称”字段中不提供任何值将返回错误，因为该字段不能为空。 
'''
#The add_category() view function can handle three different scenarios:
# 1、showing a new, blank form for adding a category;
# 2、saving form data provided by the user to the associated model, and redirecting to the Rango homepage
# 3、if there are errors, redisplay the form with error messages.
def add_category(request):
    form = CategoryForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved, we could confirm this.
            # For now, just redirect the user back to the index view.
            return redirect('/rango/')
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)
        # Will handle the bad form, new form, or no form supplied cases.
        # Render the form with error messages (if any).
        return render(request, 'rango/add_category.html', {'form': form})