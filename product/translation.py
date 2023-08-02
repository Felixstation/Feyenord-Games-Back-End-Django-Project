from modeltranslation.translator import translator, TranslationOptions
from product.models import *


class ProductVersionTranslationOptions(TranslationOptions):
    fields = ( 'description' ,)

translator.register(ProductVersion, ProductVersionTranslationOptions)