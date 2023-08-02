from django_unicorn.components import UnicornView
from product.models import Review , ProductVersion
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentsView(UnicornView):
    author: User = None
    id : ProductVersion = None
    review: Review = None
    content: str = ""

    def mount(self):
        
        self.author = self.request.user
        print(self.request.user)


        return super().mount()
