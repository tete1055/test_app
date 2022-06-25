from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreatePostForm
from django.contrib.auth.decorators import login_required
from .models import Post, Good
from accounts.models import CustomUser
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Sum
# import json
from django.http import JsonResponse

# Create your views here.

@login_required
def IndexView(request, page=1):
    # userのデータを取得
    my_data = CustomUser.objects.get(id=request.user.id)
    # userへの投稿の総合数を取得
    my_posts = Post.objects.filter(to_user=request.user.pk).count()
    # それな！も総合数を取得
    my_goods = Post.objects.filter(to_user=request.user.pk).aggregate(Sum('good_count'))['good_count__sum']
    if (my_goods == None):
        my_goods = 0
    print(my_goods)
    

    # userに送られたpostを取得
    posts = Post.objects.filter(to_user=request.user.id).order_by('good_count').reverse()
    data = Paginator(posts, 8)
    params = {
        'login_user':request.user,
        'my_data':my_data,
        'posts': data.get_page(page),
        'my_posts':my_posts,
        'my_goods':my_goods,
    }

    return render(request, 'index.html', params)

@login_required
def createpost(request, pk, page=1):
    # <int:id>の取得をする
    to_user = CustomUser.objects.get(pk=pk)
    # userへの投稿の総合数を取得
    to_posts = Post.objects.filter(to_user=to_user).count()
    # それな！も総合数を取得
    to_goods = Post.objects.filter(to_user=to_user).aggregate(Sum('good_count'))['good_count__sum']

    # 印象を匿名で送信する
    if request.method == 'POST':
        # c = request.POST['content']
        c = request.POST.get('content')
        # postを作成する
        p = Post()
        p.owner_id = request.user.pk
        # page/<int:id>を引っ張ってきてto_userにする
        p.to_user = to_user
        p.content = c
        p.save()
        print(c)
        d = {
            'content': p.content,
        }
        return JsonResponse(d, json_dumps_params={'ensure_ascii': False})
        # return redirect(to='post:posts', pk=to_user.id)

    # UserへのPostを取得
    posts = Post.objects.filter(to_user=pk).order_by('good_count').reverse()
    data = Paginator(posts, 8)

    # 共通処理
    params = {
            'login_user':request.user,
            'form':CreatePostForm,
            'to_user':to_user,
            'posts':data.get_page(page),
            'to_posts':to_posts,
            'to_goods':to_goods,
        }

    return render(request, 'post.html', params)

@login_required
def mypage(request):

    # 共通処理
    params = {
        'login_user':request.user,
    }

    return render(request, 'mypage.html', params)

@login_required
def good(request):
    if request.method == 'GET':
        good = request.GET.get('good_id')
        print(good)
        # goodするpostを取得
        good_post = Post.objects.get(id=good)
        # 自分がpostにgoodした数を調べる
        is_good = Good.objects.filter(owner=request.user).filter(post=good_post).count()
        # ゼロより大きければすでにgood済み
        if is_good > 0:
            error_data = {
                'good_id':good_post.id,
                'error':'既にそれな！しています。',
            }
            return JsonResponse(error_data)
        
        # Postのgood_countを1増やす
        good_post.good_count += 1
        good_post.save()
        # Goodを作成し、設定して保存
        good = Good()
        good.owner = request.user
        good.post = good_post
        good.save()
        d = {
            'good_id':good_post.id,
            'good_count':good_post.good_count,
            'success':'それな！しました。'
        }
        return JsonResponse(d)

@login_required
def delete(request, delete_id):
    # deleteするpostを取得
    delete_id = Post.objects.get(id=delete_id)
    # postを削除
    delete_id.delete()
    messages.success(request, '削除しました！')
    return redirect('post:index')

@login_required
def users(request):
    # 総登録者数を取得
    users = CustomUser.objects.all().count()

    if request.method == 'GET':
        if request.GET.get('count'):
            count = request.GET.get('count')
            now_users = CustomUser.objects.all().count()
            print(count)
            d = {
                'count': now_users,
            }
            print(count)
            print(now_users)
            print(now_users - int(count))
            return JsonResponse(d)

    #共通処理
    params = {
        'login_user': request.user,
        'users': users,
    }

    return render(request, 'users.html', params)

class explain(TemplateView):
    '''
    '''
    template_name = 'explain.html'