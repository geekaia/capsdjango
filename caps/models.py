from wsgiref import validate

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

from django.utils.html import format_html

import datetime

CERTIDAO = (
    ('nas', 'Nascimento'),
    ('cas', 'Casamento'),
    ('div', 'Divórcio'),
)

CONSULTA = (
    ('pend', 'Pendente'),
    ('des',  'Desistir'),
    ('rem',  'Remarcar'),
    ('falt', 'Faltou'),
    ('conc', 'Concluído'),
)

PERIODO = (
    ('mat', 'Matutino'),
    ('ves', 'Vespertino'),
)


ESTADOS = (('AC', 'Acre'),
           ('AL', 'Alagoas'),
           ('AP', 'Amapá'),
           ('AM', 'Amazonas'),
           ('BA', 'Bahia'),
           ('CE', 'Ceará'),
           ('DF', 'Distrito Federal'),
           ('ES', 'Espírito Santo'),
           ('GO', 'Goiás'),
           ('MA', 'Maranhão'),
           ('MT', 'Mato Grosso'),
           ('MS', 'Mato Grosso do Sul'),
           ('MG', 'Minas Gerais'),
           ('PA', 'Pará'),
           ('PB', 'Paraíba'),
           ('PR', 'Paraná'),
           ('PE', 'Pernambuco'),
           ('PI', 'Piauí'),
           ('RJ', 'Rio de Janeiro'),
           ('RN', 'Rio Grande do Norte'),
           ('RS', 'Rio Grande do Sul'),
           ('RO', 'Rondônia'),
           ('RR', 'Roraima'),
           ('SC', 'Santa Catarina'),
           ('SP', 'São Paulo'),
           ('SE', 'Sergipe'),
           ('TO', 'Tocantins'))

ENTIEMISS = (('SSP', 'Secretaria de Segurança Pública'),
             ('PM', 'Polícia Militar'),
             ('PC', 'Policia Civil'),
             ('CNT', 'Carteira Nacional de Habilitação'),
             ('DIC', 'Diretoria de Identificação Civil'),
             ('CTPS', 'Carteira de Trabaho e Previdência Social'),
             ('FGTS', 'Fundo de Garantia do Tempo de Serviço'),
             ('IFP', 'Instituto Félix Pacheco'),
             ('IPF', 'Instituto Pereira Faustino'),
             ('IML', 'Instituto Médico-Legal'),
             ('MTE', 'Ministério do Trabalho e Emprego'),
             ('MMA', 'Ministério da Marinha'),
             ('MAE', 'Ministério da Aeronáutica'),
             ('MEX', 'Ministério do Exército'),
             ('POF', 'Polícia Federal'),
             ('POM', 'Polícia Militar'),
             ('SES', 'Carteira de Estrangeiro'),
             ('SJS', 'Secretaria da Justiça e Segurança'),
             ('SJTS', 'Secretaria da Justiça do Trabalho e Segurança'),
             ('ZZZ', 'Outros (inclusive exterior'))

SIMNAO = (
    ('NAO', 'NÃO'),
    ('SIM', 'SIM'),
)

PROFISSIONAISSAUDE = (
    ('psiq', 'Psiquiatra'),
    ('psic', 'Psicólogo(a)'),
    ('enferm', 'Enfermeiro(a)'),
    ('psicoterap', 'Psicoterapeuta'),
    ('assissoc', 'Assistente social'),
    ('fisioterap', 'Fisioterapeuta'),
    ('terapocup', 'Terapeuta ocupacional'),
    ('clinico', 'Clínico Geral'),
)

HORARIO = (
    (1, 'Matutino'),
    (2, 'Vespertino'),
)

LOGRATIPO = (
    ('Aeroporto', 'Aeroporto'),
    ('Alameda', 'Alameda'),
    ('Área', 'Área'),
    ('Avenida', 'Avenida'),
    ('Campo', 'Campo'),
    ('Chácara', 'Chácara'),
    ('Colônia', 'Colônia'),
    ('Condomínio', 'Condomínio'),
    ('Conjunto', 'Conjunto'),
    ('Distrito', 'Distrito'),
    ('Esplanada', 'Esplanada'),
    ('Estação', 'Estação'),
    ('Estrada', 'Estrada'),
    ('Favela', 'Favela'),
    ('Fazenda', 'Fazenda'),
    ('Feira', 'Feira'),
    ('Jardim', 'Jardim'),
    ('Ladeira', 'Ladeira'),
    ('Lago', 'Lago'),
    ('Lagoa', 'Lagoa'),
    ('Largo', 'Largo'),
    ('Loteamento', 'Loteamento'),
    ('Morro', 'Morro'),
    ('Núcleo', 'Núcleo'),
    ('Parque', 'Parque'),
    ('Passarela', 'Passarela'),
    ('Pátio', 'Pátio'),
    ('Praça', 'Praça'),
    ('Quadra', 'Quadra'),
    ('Recanto', 'Recanto'),
    ('Residencial', 'Residencial'),
    ('Rodovia', 'Rodovia'),
    ('Rua', 'Rua'),
    ('Setor', 'Setor'),
    ('Sítio', 'Sítio'),
    ('Travessa', 'Travessa'),
    ('Trecho', 'Trecho'),
    ('Trevo', 'Trevo'),
    ('Vale', 'Vale'),
    ('Vereda', 'Vereda'),
    ('Via', 'Via'),
    ('Viaduto', 'Viaduto'),
    ('Viela', 'Viela'),
    ('Vila', 'Vila'))


class paciente(models.Model):
    numsus = models.CharField(max_length=255)
    nprontuario = models.CharField(max_length=255, default="", null=True, blank=True)
    nome = models.CharField(max_length=255)
    tipoendereco = models.CharField(max_length=30,choices=LOGRATIPO, default="", null=True, blank=True)
    logradouro = models.CharField(max_length=255, default="", null=True, blank=True)
    logradouronum = models.CharField(max_length=30, default="", null=True, blank=True)
    pontoreferencia = models.CharField(max_length=255, default="", null=True, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=2, choices=ESTADOS,  default="", null=True, blank=True)
    fone = models.CharField(max_length=16,  default="", null=True, blank=True)
    fonefixo = models.CharField(max_length=15,  default="", null=True, blank=True)
    email = models.CharField(max_length=255,  default="", null=True, blank=True)
    certidao = models.CharField(max_length=3, choices=CERTIDAO)
    livro = models.CharField(max_length=100,  default="", null=True, blank=True)
    fls = models.CharField(max_length=100,  default="", null=True, blank=True)
    termo = models.CharField(max_length=100,  default="", null=True, blank=True)
    dataemissao = models.DateField(auto_now=False, null=True, blank=True)
    datanascimento = models.DateField(auto_now=False)
    rg = models.CharField(max_length=50)
    rgorgemissor = models.CharField(max_length=255, choices=ENTIEMISS)
    rguf = models.CharField(max_length=2, choices=ESTADOS)
    rgdataemissao = models.DateField(auto_now=False)
    cpf = models.CharField(max_length=15)
    apelido = models.CharField(max_length=255, default="", null=True, blank=True)
    nomepai = models.CharField(max_length=255)
    nomemae = models.CharField(max_length=255)
    nomeresponsavel = models.CharField(max_length=255, default="", null=True, blank=True)
    festratamento = models.CharField(max_length=255, choices=SIMNAO)
    encaminhadopor = models.CharField(max_length=255, default="", null=True, blank=True)

    foto = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    entregadedocumentos = models.BooleanField(default=False)
    avaliacaopsiquiatrica = models.BooleanField(default=False)
    enfermagem = models.BooleanField(default=False)
    psicologa = models.BooleanField(default=False)
    #psicoterapeuta =  models.BooleanField(default=False)
    assistentesocial = models.BooleanField(default=False)
    fisioterapeuta = models.BooleanField(default=False)
    #terapeutaocupacional = models.BooleanField(default=False)

    def ficha(self):
        return format_html(
            '<a href="/genpdf/{}" target="_blank">Ficha</a>',
            self.id,
        )


    def __str__(self):
        return self.nome

from django import forms
from material import Layout, Fieldset, Row


class Profissional(models.Model):
    nome = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    especialidade = models.CharField(max_length=255, choices=PROFISSIONAISSAUDE)
    quantmaxconsulta = models.IntegerField(null=True, blank=True) # Quantidade de consultas por período
    disponivel = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name()

class ProfissionalForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(ProfissionalForm, self).__init__(*args, **kwargs)
        self.fields['quantmaxconsulta'].label = "Quantidade máxima de consultas por período"

    class Meta:
        model = Profissional
        exclude = ['nome']

from  django.utils.timezone import now

class Horario(models.Model):
    segundaM = models.BooleanField(default=False)
    tercaM = models.BooleanField(default=False)
    quartaM = models.BooleanField(default=False)
    quintaM = models.BooleanField(default=False)
    sextaM = models.BooleanField(default=False)

    segundaT = models.BooleanField(default=False)
    tercaT = models.BooleanField(default=False)
    quartaT = models.BooleanField(default=False)
    quintaT = models.BooleanField(default=False)
    sextaT = models.BooleanField(default=False)

    horainicioM = models.TimeField(null=True, blank=True)
    horafimM = models.TimeField(null=True, blank=True)

    horainicioT = models.TimeField(null=True, blank=True)
    horafimT = models.TimeField(null=True, blank=True)

    validadeinicio = models.DateField(null=True, blank=True)
    validadefim = models.DateField(null=True, blank=True)

    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)



class HorarioForm(forms.ModelForm):
    # validadeinicio = forms.DateField(input_formats = ("%d/%m/%Y"), required=False)
    # validadefim = forms.DateField(input_formats =("%d/%m/%Y"), required=False)
    class Meta:
        model = Horario
        fields = '__all__'
        exclude = ('validadeinicio', 'validadefim')
# Gera birthchoides de 100 anos

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','password', 'first_name', 'last_name', 'email')

class PacientForm(forms.ModelForm):
    id = forms.HiddenInput()

    def __init__(self, *args, **kwargs):

        super(PacientForm, self).__init__(*args, **kwargs)
        self.fields['nome'].label = "Nome Completo"
        self.fields['dataemissao'].label = "Data de Emissão"
        self.fields['numsus'].label = "Número do SUS"
        self.fields['pontoreferencia'].label = "Ponto de referência"
        self.fields['fone'].label = "Telefone Celular"
        self.fields['fonefixo'].label = "Telefone Fixo"
        self.fields['rgorgemissor'].label = "Orgão emissor"
        self.fields['rguf'].label = "Estado"
        self.fields['cpf'].label = "CPF"
        self.fields['nomepai'].label = "Nome do pai"
        self.fields['nomemae'].label = "Nome da mãe"
        self.fields['festratamento'].label = "Já fez tratamento?"
        self.fields['encaminhadopor'].label = "Encaminhado por"
        self.fields['datanascimento'].label = "Data de nascimento"
        self.fields['rgdataemissao'].label = "Data de emissão do RG"

        self.fields['fls'].label = "Folha"
        self.fields['rg'].label = "RG"
        self.fields['logradouronum'].label = "Número"

        self.fields['nomeresponsavel'].label = "Nome do responsável"
        self.fields['entregadedocumentos'].label = "Entrega de documentos"
        self.fields['avaliacaopsiquiatrica'].label = "Avaliação Psiquiátrica"
        self.fields['psicologa'].label = "Psicóloga"
        self.fields['assistentesocial'].label = "Assistente Social"
        self.fields['fisioterapeuta'].label = "Fisioterapeuta"
#        self.fields['terapeutaocupacional'].label = "Terapeuta ocupacional"
        self.fields['nprontuario'].label = "Número do prontuário"




    class Meta:
        model = paciente
        fields = '__all__'

    layout = Layout('foto','numsus', 'nprontuario', 'nome', 'apelido',
                    Fieldset('Endereço',
                             Row('tipoendereco', 'logradouro', 'logradouronum'),
                             'pontoreferencia',
                             'bairro',
                             'cidade',
                             'uf'),

                    Fieldset('Contato',
                             Row('fone', 'fonefixo'), 'email'),

                    Fieldset('Certidão',
                             Row('datanascimento', 'certidao', 'livro', 'fls', 'termo'),
                             'dataemissao'),

                    Fieldset('Documentos',
                             Row('rgorgemissor', 'rguf', 'rg', 'rgdataemissao'),
                             'cpf'),



                    Fieldset('Outras informações',
                             Row('nomepai', 'nomemae'),
                             'nomeresponsavel',
                             'festratamento',
                             'encaminhadopor',
                             ),


                    Fieldset('Etapas',
                             'entregadedocumentos', 'avaliacaopsiquiatrica', 'enfermagem', 'psicologa',
                            # 'psicoterapeuta',
                             'assistentesocial', 'fisioterapeuta', #'terapeutaocupacional'
                             ),

                    )


class UsuarioForm(forms.Form):
    usuario = forms.CharField(max_length=255)
    senha = forms.CharField(max_length=255, widget=forms.PasswordInput)

#
# STATUS = (
#     ('')
# )

class Consulta(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data = models.DateField() # Data padrão
    hora = models.TimeField(null=True, blank=True)
    periodo = models.CharField(choices=PERIODO, max_length=50, null=True, blank=True)
    status = models.CharField(choices=CONSULTA, max_length=50, default='pend', null=True, blank=True)
    anotacoes = models.TextField(null=True, blank=True)
    horario = models.ForeignKey(Horario,
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE) # Deixei assim, mas depois tenho que mudar


    def __str__(self):
        return str(self.id)


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields ="__all__"

class Teste(models.Model):
    fone = models.CharField(max_length=255)


class Evolucao(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    anotacoes = models.TextField()
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    anotacaoconsulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, null=True, blank=True)
    ultimaatualizacao = models.DateTimeField()






