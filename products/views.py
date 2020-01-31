from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .forms import CommentForm

from .models import Product


class ProductList(ListView):
    model = Product
    paginate_by = 50
    template_name = 'products/product-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductList, self).get_context_data(object_list=None, **kwargs)
        context.update(
            {
                "new_arrival": Product.objects.filter(is_new=True),
                "sales": Product.objects.filter(sale=True),
                "populars": Product.objects.filter(popular=True)
            }
        )
        return context


class ProductDetail(FormMixin, DetailView):
    model = Product
    template_name = 'products/product-detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('products:detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = User.objects.filter(username=self.request.user.username).get()
        comment.product = self.object
        comment.save()
        return super(ProductDetail, self).form_valid(form)
