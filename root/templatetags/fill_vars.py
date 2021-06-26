import re
from django import template
from ..models import UserInfo 
from django.utils.translation import ugettext,gettext

register = template.Library()

def rep(value):
    user = UserInfo.objects.first()
    variables = {
        "site_name":user.nom_sur_site,
        "email":user.email,
        "phone":user.phone,
        "adress":user.adresse_local
    }
    output = str(value)
    for i in variables:
        output = output.replace(f'{{{{{i}}}}}',variables[i])
    regex = r"link:(.*?)>"
    for i in re.findall(regex, output):
        link,text = str(i).split("<")
        if 'mailto:' in link or 'tel:' in link:
            # output = re.sub(regex,f'<a href="{link}">{text}</a>',output)
            link_type = True
        else:
            link_type = False
        if link_type:
            # output = re.sub(regex,f'<a href="{link}">{text}</a>',output)
            output = output.replace(f'link:{i}>',f'<a href="{link}">{text}</a>')
        else:
            # output = re.sub(regex,f'<a href="https://xerixy.com/frequent/{link}">{text}</a>',output)
            output = output.replace(f'link:{i}>',f'<a href="https://xerixy.com/frequent/{link}">{text}</a>')
        
    return output


@register.filter(name='template_trans')
def template_trans(text):
    try:
        return ugettext(text)
    except Exception as e:
        return text

register.filter('vars', rep)