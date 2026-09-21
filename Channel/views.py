from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Channels, Category, Video, Like, Comment, Follow

def video_list(request):
    search = request.GET.get('search')
    
    if search:
        videos = Video.objects.filter(title__icontains=search)
    else:
        videos = Video.objects.all()

    return render(request, 'video_list.html', {'videos': videos, 'search': search})


def video_detail(request, id):
    video = get_object_or_404(Video, id=id)
    is_liked = False
    if request.user.is_authenticated:
        is_liked = Like.objects.filter(like_users=request.user, like_video=video).exists()

    comments = video.comments.filter(comment_id__isnull=True)
    likes_count = video.likes.count()

    return render(request, 'video_detail.html', {
        'video': video,
        'is_liked': is_liked,
        'likes_count': likes_count,
        'comments': comments
    })


@login_required
def like_video(request, id):
    video = get_object_or_404(Video, id=id)
    like_qs = Like.objects.filter(like_users=request.user, like_video=video)
    if like_qs.exists():
        like_qs.delete()
    else:
        Like.objects.create(like_users=request.user, like_video=video)
    return redirect('video_detail', id=id)


@login_required
def comment_create(request, id):
    video = get_object_or_404(Video, id=id)
    if request.method == 'POST':
        text = request.POST.get('text')
        parent_id = request.POST.get('comment_id')
        parent_obj = None
        if parent_id:
            parent_obj = Comment.objects.filter(id=parent_id).first()

        Comment.objects.create(
            user=request.user,
            video=video,
            text=text,
            comment_id=parent_obj
        )
    return redirect('video_detail', id=id)


@login_required
def create_channel(request):
    if not request.user.is_verified:
        return redirect('verified')

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        avatar = request.FILES.get('avatar')

        if not title:
            return render(request, 'create_channel.html', {'error': 'title is required'})

        channel = Channels.objects.create(
            title=title,
            description=description,
            avatar=avatar,
            owner=request.user
        )
        return redirect('channel_detail', id=channel.id)

    return render(request, 'create_channel.html')


def channel_detail(request, id):
    channel = get_object_or_404(Channels, id=id)
    subscribers_count = channel.channel_follow.count()
    total_likes = Like.objects.filter(like_video__channel=channel).count()

    is_following = False
    if request.user.is_authenticated:
        is_following = Follow.objects.filter(user=request.user, channel=channel).exists()

    videos = channel.videos.all()

    return render(request, 'channel_detail.html', {
        'channel': channel,
        'subscribers_count': subscribers_count,
        'total_likes': total_likes,
        'is_following': is_following,
        'videos': videos
    })


@login_required
def follow_channel(request, id):
    channel = get_object_or_404(Channels, id=id)
    follow_qs = Follow.objects.filter(user=request.user, channel=channel)
    if follow_qs.exists():
        follow_qs.delete()
    else:
        Follow.objects.create(user=request.user, channel=channel)
    return redirect('channel_detail', id=id)


@login_required
def video_create(request, id):
    channel = get_object_or_404(Channels, id=id)

    if channel.owner != request.user:
        return render(request, 'video_create.html', {'error': 'ne tvoy channel'})

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        video_file = request.FILES.get('video_file')

        category = get_object_or_404(Category, id=category_id)

        Video.objects.create(
            title=title,
            description=description,
            video_file=video_file,
            category=category,
            channel=channel
        )
        return redirect('channel_detail', id=channel.id)

    categories = Category.objects.all()
    return render(request, 'video_create.html', {'channel': channel, 'categories': categories})