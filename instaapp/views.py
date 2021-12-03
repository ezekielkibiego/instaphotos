from cloudinary.models import CloudinaryField
from django.shortcuts import redirect, render
from django.http  import HttpResponse
from .models import Images,Profile
# import cloudinary.uploader
import cloudinary.api
from django.contrib.auth.decorators import login_required

def welcome(request):
    return HttpResponse('Welcome to Instaphotos')

@login_required(login_url='/accounts/login/')
def index(request):

    Image = Images.objects.all().order_by('-id')

    return render(request, 'all-insta/index.html',{'Image':Image})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    images = Images.objects.filter(user_id=current_user.id)
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, 'profile.html', {"images": images, "profile": profile})

@login_required(login_url='/accounts/login/')
def save_image(request):
    if request.method == 'POST':
        name = request.POST['image_name']
        caption = request.POST['image_caption']
        image_file = request.FILES['image_file']
        image_file = CloudinaryField.uploader.upload(image_file)
        image_url = image_file['url']
        image = Images(name=name, caption=caption, image=image_url,
                      profile_id=request.POST['user_id'], user_id=request.POST['user_id'])
        image.save_image()
        return redirect('/profile', {'success': 'Image Uploaded Successfully'})
    else:
        return render(request, 'profile.html', {'danger': 'Image Upload Failed'})