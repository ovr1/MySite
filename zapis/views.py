from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from zapis.forms import AddTaskForm, TodoItemExportForm, TodoItemForm
from zapis.models import TodoItem
from django.shortcuts import redirect, render, get_object_or_404
from taggit.models import Tag


class ZapisDetailsView(DetailView):
    model = TodoItem
    template_name = 'zapis/details.html'



@login_required


def complete_zapis(request, uid):
    t = TodoItem.objects.get(id=uid)
    t.is_completed = True
    t.save()
    return HttpResponse("OK")


def add_zapis(request):
    if request.method == "POST":
        desc = request.POST["description"]
        t = TodoItem(description=desc)
        t.save()
    return redirect(reverse("zapis:list"))


def delete_zapis(request, uid):
    t = TodoItem.objects.get(id=uid)
    t.delete()
    return redirect(reverse("zapis:list"))


class ZapisListView(LoginRequiredMixin, ListView):
    model = TodoItem
    context_object_name = "zapis"
    template_name = "zapis/list.html"

    def get_queryset(self):
        u = self.request.user
        qs = super().get_queryset()
        return qs.filter(owner=u)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_zapis = self.get_queryset()
        tags = []
        for t in user_zapis:
            tags.append(list(t.tags.all()))

        def filter_tags(tags_by_task):
            t = []
            for tags in tags_by_task:
                for tag in tags:
                    if tag not in t:
                        t.append(tag)
            return t

        context['tags'] = filter_tags(tags)
        return context


class ZapisCreateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = TodoItemForm(request.POST)
        if form.is_valid():
            new_zapis = form.save(commit=False)
            new_zapis.owner = request.user
            new_zapis.save()
            return redirect(reverse("zapis:list"))

        return render(request, "zapis/create.html", {"form": form})

    def get(self, request, *args, **kwargs):
        form = TodoItemForm()
        return render(request, "zapis/create.html", {"form": form})


class ZapisEditView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        t = TodoItem.objects.get(id=pk)
        form = TodoItemForm(request.POST, instance=t)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            form.save_m2m()
            return redirect(reverse("zapis:list"))

        return render(request, "zapis/edit.html", {"form": form})

    def get(self, request, pk, *args, **kwargs):
        t = TodoItem.objects.get(id=pk)
        form = TodoItemForm(instance=t)
        return render(request, "zapis/edit.html", {"form": form, "zapis": t})



class ZapisExportView(LoginRequiredMixin, View):
    def generate_body(self, user, priorities):
        q = Q()
        if priorities["prio_high"]:
            q = q | Q(priority=TodoItem.PRIORITY_HIGH)
        if priorities["prio_med"]:
            q = q | Q(priority=TodoItem.PRIORITY_MEDIUM)
        if priorities["prio_low"]:
            q = q | Q(priority=TodoItem.PRIORITY_LOW)
        zapis = TodoItem.objects.filter(owner=user).filter(q).all()

        body = "Ваши записи и процедуры:\n"
        for t in list(zapis):
            if t.is_completed:
                body += f"[x] {t.description} ({t.get_priority_display()})\n"
            else:
                body += f"[ ] {t.description} ({t.get_priority_display()})\n"

        return body

    def post(self, request, *args, **kwargs):
        form = TodoItemExportForm(request.POST)
        if form.is_valid():
            email = request.user.email
            body = self.generate_body(request.user, form.cleaned_data)
            send_mail("Записи", body, settings.EMAIL_HOST_USER, [email])
            messages.success(request, "Записи были отправлены на почту %s" % email)
        else:
            messages.error(request, "Что-то пошло не так, попробуйте ещё раз")
        return redirect(reverse("zapis:list"))

    def get(self, request, *args, **kwargs):
        form = TodoItemExportForm()
        return render(request, "zapis/export.html", {"form": form})


def zapis_by_tag(request, tag_slug=None):
    u = request.user
    zapis = TodoItem.objects.filter(owner=u).all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        zapis = zapis.filter(tags__in=[tag])

    all_tags = []
    for t in zapis:
        all_tags.append(list(t.tags.all()))

    def filter_tags(tags_by_zapis):
        t = []
        for tags in tags_by_zapis:
            for tag in tags:
                if tag not in t:
                    t.append(tag)
        return t

    all_tags = filter_tags(all_tags)

    return render(
        request,
        "zapis/list.html",
        {"tag": tag, "zapis": zapis, "all_tags": all_tags},
    )
