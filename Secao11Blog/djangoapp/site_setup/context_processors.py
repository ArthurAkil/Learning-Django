

from site_setup.models import SiteSetup

# Fazemos no proposíto de gerar um context GERAL para todos os templates, fica melhor que criar o mesmo em todas as views, cria aqui, adiciona no template do settings, depois só puxar em qualquer template de todos os apps que quer que apareça isso
def context_processors_example(request):
    return{
        'example': 'veio do context_processors.py (example)'
    }

def site_setup(request):
    # puxamos o setup criado no site setup (title, description, etc) e pegamos o primeiro valor
    setup = SiteSetup.objects.order_by('-id').first()

    # com isso aqui dinâmico podemos alterar do admin mesmo e vai ser responsivo o titulo com o que escrevemos lá
    return{
        # primeiro valor atribuido a site_setup
        'site_setup': setup
    }