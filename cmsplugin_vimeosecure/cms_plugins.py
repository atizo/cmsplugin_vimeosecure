from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from models import VimeoSecure

class VimeoSecurePlugin(CMSPluginBase):
    model = VimeoSecure
    name = _("Vimeo")
    render_template = "cms/plugins/vimeosecure.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(VimeoSecurePlugin)
