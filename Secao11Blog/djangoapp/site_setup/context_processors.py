

from site_setup.models import SiteSetup

# Fazemos no proposíto de gerar um context GERAL para todos os templates, fica melhor que criar o mesmo em todas as views, cria aqui, adiciona no template do settings, depois só puxar em qualquer template de todos os apps que quer que apareça isso
# O context_processors.py é um módulo no Django que permite adicionar variáveis ao contexto de todos os templates. Funciona através da definição de funções que recebem uma request e retornam um dicionário. Esse dicionário pode conter qualquer informação que você deseja disponibilizar nos templates.

#     Definição da Função: Para usar um processador de contexto, você cria uma função, por exemplo, site_setup, no arquivo context_processors.py. Essa função deve retornar um dicionário com as variáveis que você quer enviar para todos os templates.

#     Registro do Processador: Após definir sua função, você precisa registrá-la no seu arquivo de configuração do Django, usualmente settings.py. No bloco TEMPLATES, na chave OPTIONS, você vai adicionar seu processador de contexto na lista context_processors.
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