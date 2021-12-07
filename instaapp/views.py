from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http  import HttpResponse
from django.shortcuts import render, get_object_or_404

import cloudinary
import cloudinary.uploader
import cloudinary.api
from instaapp.forms import CommentForm, PicImageForm
from .models import Image, Like,Profile
import cloudinary.api
from django.contrib.auth.decorators import login_required, user_passes_test

def welcome(request):
    return HttpResponse('Welcome to Instaphotos')

@login_required(login_url='/accounts/login/')
def index(request):

    Images = Image.objects.all().order_by('-id')
    users = Profile.objects.all()
    if request.method == 'POST':  
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = request.user
            com.save()
            return redirect('index')
    
    else:
        form = CommentForm()
  
    return render(request, 'all-insta/index.html',{'Images':Images,'form':form,'users':users})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    images = Image.objects.filter(user_id=current_user.id)
    profile = Profile.objects.filter(user_id=current_user.id).first()
    form = PicImageForm()
    if request.method == 'POST':
        form = PicImageForm (request.POST , request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        redirect('profile')
    return render(request, 'profile.html', {"images": images, "profile": profile, 'form':form})

@login_required(login_url='/accounts/login/')
def save_image(request):
    if request.method == 'POST':
        name = request.POST['image_name']
        caption = request.POST['image_caption']
        image_file = request.FILES['image_file']
        image_file = CloudinaryField.uploader.upload(image_file)
        image_url = image_file['url']
        image = Image(name=name, caption=caption, image=image_url,
                      profile_id=request.POST['user_id'], user_id=request.POST['user_id'])
        image.save_image()
        return redirect('/profile', {'success': 'Image Uploaded Successfully'})
    else:
        return render(request, 'profile.html', {'danger': 'Image Upload Failed'})

@login_required
def search(request):

    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        search_photo = Image.search_by_photo_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"search_photo": search_photo})

    else:
        message = "You haven't searched for any user"
        return render(request, 'search.html',{"message1":message})

@login_required
def user_profile(request,pk):
  
  user = user_passes_test.objects.get(pk = pk)
  photos = Image.objects.filter(user = user)
  c_user = request.user
  
  return render(request,'user_profile.html',{"user":user,
  "photos":photos,"c_user":c_user})

def like_image(request):
    user = request.user
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image_pic =Image.objects.get(id=image_id)
        if user in image_pic.liked.all():
            image_pic.liked.add(user)
        else:
            image_pic.liked.add(user)    
            
        like,created =Like.objects.get_or_create(user=user, image_id=image_id)
        if not created:
            if like.value =='Like':
               like.value = 'Unlike'
        else:
               like.value = 'Like'

        like.save()       
    return redirect('index')

@login_required
def comments(request,image_id):
  form = CommentForm()
  image = Image.objects.filter(pk = image_id).first()
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit = False)
      comment.user = request.user
      comment.image = image
      comment.save() 
  return redirect('index')

def user_profile(request,user_id):
    user_profile = Profile.objects.filter(user_id = user_id).first()
    images = Image.objects.filter(user_id = user_id)

    return render(request, 'userprofile.html', {'user_profile':user_profile, 'images':images})
