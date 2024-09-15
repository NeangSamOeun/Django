from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import product
from shop.models import Category

class productdetailview(TemplateView):
    template_name = 'shop/productdetail.html'

    def get(self, request, id):
        categories = Category.objects.order_by("name")
        products = product.objects.get(id=id)
        context = {
            "category" : [{"id": c.id, "name": c.name} for c in Category],
            "title" : products.name,
            "description" : products.description,
            "price" : products.price,
            "volume" : products.volume,
            "image" : products.image
        }
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))