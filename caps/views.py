from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.http import HttpResponse
# Create your views here.

from django.contrib.auth.decorators import login_required

from reportlab.lib import colors
from django.db.models import Q

import time
from datetime import date, timedelta
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT, TA_LEFT
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Frame, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from .models import paciente
from io import BytesIO

import datetime
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from reportlab.platypus.flowables import Spacer, HRFlowable, PageBreak, CondPageBreak
from reportlab.lib.units import cm

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
import json
from django.http import JsonResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User


@login_required
def gerarFicha(request, id):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    nomearquivo="ficha"+datetime.date.today().strftime("%d/%m/%Y")+".pdf"
    response['Content-Disposition'] = 'filename="'+nomearquivo+'"' # attachment; filename=
    buff = BytesIO()

    doc = SimpleDocTemplate(buff, pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)

    Story = []
    logo = os.path.join(BASE_DIR,"logopref.png")

    im = Image(logo, 0.7 * inch, 0.7 * inch)
    Story.append(im)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
    styles.add(ParagraphStyle(name='Left', alignment=TA_LEFT))

    p = paciente.objects.get(pk=id)

    ptext = "PREFEITURA DE BARRA DO GARÇAS<br/>"
    ptext += "SECRETARIA MUNICIPAL DE SAÚDE<br/>"
    ptext += "Centro de Atenção Psicossoail CAPS II TM<br/><br/>"
    ptext += "<br/>IMPORTANTE -- Cartão SUS nº: "+str( p.numsus )
    ptext += "<br/><br/><br/>FICHA DE ACOLHIMENTO<br/><br/><br/><br/>"

    Story.append(Paragraph(ptext, styles["Center"]))
    try:
        ptext = "Número do prontuário: "+p.nprontuario
    except:
        ptext = "Número do prontuário: "

    ptext += "<br/>Nome: "+p.nome
    try:
        ptext +="<br/>Endereço: "+ p.get_tipoendereco_display()+" "+p.logradouro+", n° "+p.logradouronum
    except:
        pass

    try:
        ptext +="<br />Ponto de referência: "+p.pontoreferencia
    except:
        pass

    try:
        ptext +="<br />Bairro: "+p.bairro
    except:
        pass

    try:
        ptext += "  Cidade: "+p.cidade
    except:
        pass

    try:
        ptext +=" Fone: " + p.fone
    except:
        ptext += " Fone: "
        pass

    try:
        ptext +="<br />Certidão de: " + p.get_certidao_display()
    except:
        ptext += "<br />Certidão de: "
        pass

    try:
        ptext +=" Livro: " + p.livro
    except:
        ptext += " Livro: "
        pass

    try:
        ptext += " Folha: " +p.fls
    except:
        ptext += " Folha: "
        pass

    try:
        ptext += "<br/>Termo: "+p.termo
    except:
        ptext += "<br/>Termo: "

    try:
        ptext +=" Data de emissão: "+ p.dataemissao.isoformat().capitalize()
    except:
        ptext += " Data de emissão: "

    try:
        ptext += " Data de nascimento: " + p.datanascimento.isoformat().capitalize()
    except:
        ptext += " Data de nascimento: "


    try:
        ptext += " RG: "+p.rg
    except:
        ptext += " RG: "


    try:
        ptext += " Orgão emissor: "+ p.get_rgorgemissor_display()
    except:
        ptext += " Orgão emissor: "

    try:
        ptext += " UF: " + p.rguf
    except:
        ptext += " UF: "

    try:
        ptext += " Data de emissão: " + p.rgdataemissao.isoformat().capitalize()
    except:
        ptext += " Data de emissão: "

    try:
        ptext += "<br />CPF: " + p.cpf
    except:
        ptext += "<br />CPF: "

    try:
        ptext += "<br/>Apelido: " + p.apelido
    except:
        ptext += "<br/>Apelido: "

    try:
        ptext += "<br/>Nome do pai: " + p.nomepai
    except:
        ptext += "<br/>Nome do pai: "

    try:
        ptext += "<br/>Nome da mãe: " + p.nomemae
    except:
        ptext += "<br/>Nome da mãe: "

    try:
        ptext += "<br/>Nome do responsável: " + p.nomeresponsavel
    except:
        ptext += "<br/>Nome do responsável: "

    try:
        ptext += "<br/>Já fez tratamento anteriormente? " + p.get_festratamento_display()
    except:
        ptext += "<br/>Já fez tratamento anteriormente? "

    try:
        ptext += "<br/>Encaminhado por: " + p.encaminhadopor
    except:
        ptext += "<br/>Encaminhado por: "

    Story.append(Paragraph(ptext, styles["Justify"]))

    today = datetime.date.today()

    ptext = "Barra do Garças-MT, " + today.strftime("%d/%m/%Y")+".<br/><br/><br/> <br/><br/><br/>"





    Story.append(Paragraph(ptext, styles["Right"]))


    ptext="_____________________________________________"
    ptext+="<br/>Responsável pelo acolhimento<br /><br />"

    Story.append(Paragraph(ptext, styles["Center"]))

    Story.append(Paragraph("", styles["Left"]))
    steps=[]

    if p.entregadedocumentos:
        steps.append("X")
    else:
        steps.append("")

    if p.avaliacaopsiquiatrica:
        steps.append("X")
    else:
        steps.append("")
    #
    if p.enfermagem:
        steps.append("X")
    else:
        steps.append("")

    if p.psicologa:
        steps.append("X")
    else:
        steps.append("")


    # if p.psicoterapeuta:
    #     steps.append("X")
    # else:
    #     steps.append("")

    if p.assistentesocial:
        steps.append("X")
    else:
        steps.append("")

    if p.fisioterapeuta:
        steps.append("X")
    else:
        steps.append("")

    # if p.terapeutaocupacional:
    #     steps.append("X")
    # else:
    #     steps.append("")

    # Passos cumpridos
    data = [[steps[0], 'Entrega de documentos'],
            [steps[1], 'Avaliação psiquiátrica'],
            [steps[2], 'Enfermagem'],
            [steps[3], 'Psicóloga'],
            # [steps[4], 'Psicoterapeuta'],
            [steps[4], 'Assistente social'],
            [steps[5], 'Fisioterapeuta'],
            # [steps[7], 'Terapeuta ocupacional'],
            ]


    t = Table(data, hAlign='LEFT')
    t.setStyle(TableStyle([
                            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),]))


    Story.append(t)
    Story.append(Paragraph("<br/><br/>", styles["Center"]))
    Story.extend([Spacer(0, 0.1*cm), HRFlowable(width="100%", thickness=0.5, color=colors.black), Spacer(0,0.1*cm)])
    ptext = "Rua Francisco Lira, 1470, Sena marques. CEP 78.600-000 - Barra do Garças-MT<br/>"
    ptext += "Tel.: (66) 3401-7805"

    Story.append(Paragraph(ptext, styles["Center"]))


    doc.build(Story)

    response.write(buff.getvalue())
    buff.close()
    return response



@login_required
def gerarRelatorio(request):

    # Se for informado algo será considerado
    pcr="t"
    try:
        pcr = request.GET['pcr']
        pcrq = paciente.objects.get(pk=int(pcr))
    except:
        pcr="t"


    Story = []

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
    styles.add(ParagraphStyle(name='Left', alignment=TA_LEFT))

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    nomearquivo="relatorio"+datetime.date.today().strftime("%d/%m/%Y")+".pdf"
    response['Content-Disposition'] = 'filename="'+nomearquivo+'"' # attachment; filename=
    buff = BytesIO()


    styleN = styles['Normal']
    def footer(canvas, doc):
        canvas.saveState()
        P = Paragraph("<hr/><br/>Rua Francisco Lira, 1470, Sena marques. CEP 78.600-000 - Barra do Garças-MT <br/>Tel.: (66) 3401-7805  " ,
                      styles["Center"])
        w, h = P.wrap(doc.width, doc.bottomMargin)
        P.drawOn(canvas, doc.leftMargin, h)

        canvas.line(doc.leftMargin, 62, doc.width+67, 62)


        logo = os.path.join(BASE_DIR, "logopref.png")

        im = Image(logo, 0.7 * inch, 0.7 * inch)
        h = im.imageHeight
        w = im.imageWidth
        c = w/2
        ch = h/2




        print("Width: ", w)
        print("Height: ", h)
        print("c: ", c)
        print("ch: ", ch)

        print("Doc width: ", doc.width)
        print("LeftM width: ", doc.leftMargin)
        print("Centro: ", (doc.width/2)+c-37)

        im.drawOn(canvas, (doc.width/2)+c-(doc.leftMargin/2), doc.height + doc.topMargin-5)


        #
        # header = Paragraph(im, styles['Center'])
        # w, h = header.wrap(doc.width, doc.topMargin)
        # header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h)
        #
        ptext = "<br/>PREFEITURA DE BARRA DO GARÇAS<br/>"
        ptext += "SECRETARIA MUNICIPAL DE SAÚDE<br/>"
        ptext += "Centro de Atenção Psicossoail CAPS II TM<br/><br/>"

        header = Paragraph(ptext, styles['Center'])
        w, h = header.wrap(doc.width, doc.topMargin)
        header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h)



        canvas.restoreState()



    doc = SimpleDocTemplate(buff, pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=135, bottomMargin=72, )

    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height,
                  id='normal')

    template = PageTemplate(id='test', frames=frame, onPage=footer)
    doc.addPageTemplates([template])


    ptext = "<b>RELATÓRIO</b><br/> <br/>"

    if pcr == "t":
        datainicialr = request.GET['datainicialr']
        datafinalr = request.GET['datafinalr']

        datainicialrt = datetime.datetime.strptime(datainicialr, '%Y-%m-%d')
        datafinalrt = datetime.datetime.strptime(datafinalr, '%Y-%m-%d')

    Story.append(Paragraph(ptext, styles["Center"]))

    ptext = "<b>Relatório gerado no dia </b> "+datetime.date.today().strftime("%d/%m/%Y")+"<br/>"

    if pcr == "t":
        ptext += "<b>Data inicial: </b> "+datainicialrt.strftime("%d/%m/%Y")+"<br/>"
    else:

        ptext +="<b>Paciente: </b> "+pcrq.nome+"<br/><br/>"

    l = ""
    tadd=""

    try:
        l = request.GET['lista']

        if l == 't':
            tadd = ""
        else:
            profl = Profissional.objects.get(pk=int(l))
            tadd = " <br/><b>Profissional:</b>  " + profl.user.get_full_name()
            tadd += " <br/><b>Especialidade:</b>  " + profl.get_especialidade_display()

    except:
        print("Erro lista : ", tadd)
        # tadd = ""

    if pcr == "t":
        ptext += " <b>Data final:</b>  "+datafinalrt.strftime("%d/%m/%Y") +tadd+" <br/><br/>"



    Story.append(Paragraph(ptext, styles["Left"]))





    datatable = []

    evolucao = []

    # consultasInt = Consulta.objects.filter(data__gte=datafinalr).filter(data__lte=datainicialr)
    if pcr == "t":
        consultasInt = Consulta.objects.filter(data__lte=datafinalr).filter(data__gte=datainicialr).filter(status='conc').order_by("data")

        # em = Horario.objects.filter(profissional_id__exact=hora.profissional.id).filter(
        #     validadefim__gte=hora.validadeinicio).filter(
        #     validadeinicio__lte=hora.validadeinicio).exclude(id=hora.id)

        try:
            l = request.GET['lista']

            if l != 't':
                profl = Profissional.objects.get(pk=int(l))
                consultasInt = consultasInt.filter(profissional=profl)
        except:
            pass

        print('quantidade de consultasInt:', len(consultasInt))
    else:

        consultasInt = Consulta.objects.filter(paciente=pcrq).filter(status='conc').order_by("data")



    cont=1

    if l == 't':
        datatable.append(['Num','Data', 'Hora', 'Nome', 'Especialidade','Paciente'])
    else:
        if pcr == 't':
            datatable.append(['Num', 'Data', 'Hora',  'Paciente']) # Relatório de um profissional
        else:
            datatable.append(['Num', 'Data', 'Hora', 'Nome', 'Especialidade']) # De um paciente em específico
            evolucao.append(['Profissional', 'Anotações'])






    for con in consultasInt:
        if l == 't':
            datatable.append([cont, con.data.strftime("%d/%m/%Y"), con.hora, Paragraph(con.profissional.user.get_full_name(),styles["Left"]) , con.profissional.get_especialidade_display(), Paragraph(con.paciente.nome,styles["Left"])])
        else:
            if pcr == 't':
                datatable.append([cont, con.data.strftime("%d/%m/%Y"), con.hora,  Paragraph(con.paciente.nome, styles["Left"])])
            else:
                datatable.append([cont, con.data.strftime("%d/%m/%Y"), con.hora, Paragraph(con.profissional.user.get_full_name(), styles["Left"]), con.profissional.get_especialidade_display() ])

        cont += 1



    from reportlab.lib.units import mm

    if(len(consultasInt) >= 1):
        if l == 't':
            t = Table(datatable, colWidths=(10*mm, 22*mm, 20*mm, 50*mm, 50*mm, 50*mm))
        else:
            if pcr == "t":
                t = Table(datatable, colWidths=(10 * mm, 22 * mm, 20 * mm,  100 * mm))
            else:
                t = Table(datatable, colWidths=(10 * mm, 22 * mm, 20 * mm, 50 * mm, 53 * mm))
        #
        t.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                                ]))

        Story.append(t)
    else:
        print("Não há registros de consulta")


    try:
        pc = paciente.objects.get(pk=pcr)
        print("Oi4", pc.nome)
        evData = Evolucao.objects.all().filter(paciente=pc)
        print("Oi1")

        # evolucao.append(['Profissional', 'Anotações'])

        for ev in evData:
            text =  Paragraph(ev.anotacoes.replace("\n", "<br/>"), styles["Justify"])
            esp = Paragraph(ev.profissional.get_especialidade_display()+": "+ev.profissional.user.get_full_name()+" -- dia: "+ev.ultimaatualizacao.strftime("%d/%m/%Y"), styles["Left"])
            evolucao.append([esp, text ])
        print("Oi2 ", len(evData))

        t2 = Table(evolucao, colWidths=((10+22+20) * mm, (50+53) * mm))
        print('oi3333')
        #
        t2.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                               ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                               ]))

        Story.append(Paragraph("<br/><br/>", styles['Left']))
        Story.append(t2)
    except:
        print('Não há registros de evolução')




    doc.build(Story)

    response.write(buff.getvalue())
    buff.close()

    return response



def viewFotos(request):



    return HttpResponse("Olamundo")




def home(request):
    return render(request, 'base2.html')


def loginform(request):
    return render(request, "login/login.html")





def sair(request):
    logout(request)

    return redirect("/login/")



from django.core import serializers

@staff_member_required
@login_required
def pacientecad(request):
    return render(request, "paciente.html")



from .formularios import *

@staff_member_required
@login_required
def cadastrapaciente(request):

    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        form = PacientForm(data)

        if form.is_valid():
            form.save()

            return JsonResponse({'resp': 1})


    return JsonResponse({'resp': -1})



@login_required
def home2(request):
    return render(request, "base2.html")



@staff_member_required
@login_required
def pacienteman(request):
    form = PacientForm()
    pc = paciente()
    er = None
    id = ""

    if request.method == "POST":

        form = PacientForm(request.POST or None, request.FILES or None)

        if form.is_valid():


            id = request.POST['id']

            print("Id passado: ", id)

            if id == "":
                form.save()

            else:
                pc = form.save(commit=False)
                pc.id = int(id)
                pcOld = paciente.objects.get(pk=int(pc.id))

                try:
                    foto = request.FILES['foto']
                    pc.foto = foto
                except:
                    pc.foto = pcOld.foto


                print("ID: ", pc.id)
                pc.save()

            print("formulario salvo")

            return redirect("/pacientelist?page=0")
        else:
            er = 1
            print("Form: ", form.errors)
    else:
        pacienteid = request.GET['pacienteid']


        if int(pacienteid) != 0:
            pc = paciente.objects.get(pk=int(pacienteid))
            id = pc.id
            form = PacientForm(instance=pc)

        else:
            form = PacientForm()

        print("Ok form")


    return render(request, "pacienteman.html", { 'formulario': form,
                                                 'foto': pc.foto,
                                                 'er': er, 'id': id})



@staff_member_required
@login_required
def pacienterem(request):

    idr = request.GET['idr']
    pc = paciente.objects.get(pk=idr)
    pc.delete()

    return redirect("/pacientelist?page=0")


@login_required
def pacientelist(request):

    novaconsulta = 0
    try:
        # novaconsulta = request.GET['novaconsulta']
        profid = request.GET['profid']
        periodo = request.GET['periodo']
        data = request.GET['data']
    except:
        novaconsulta = 0
        profid = 0
        periodo = 0
        data=0

    pesquisa = 0


    if request.method == "POST":
        pesquisa = request.POST['pesquisa']
        pacientes = paciente.objects.filter(nome__contains=pesquisa)
    else:
        pacientes = paciente.objects.all()


    paginator = Paginator(pacientes, 8)

    numpages = list(range(1, paginator.num_pages+1))

    page = request.GET['page']

    print("Página: ", page)

    atual = 1

    try:
        pcientes = paginator.page(page)
        atual = int(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pcientes = paginator.page(1)
        # data = serializers.serialize('json', pcientes)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pcientes = paginator.page(paginator.num_pages)

        # data = serializers.serialize('json', pcientes)


    return render(request, "page.html",
                  {
                   'pacientes': pcientes,
                   'numpages': numpages,
                   'atual': atual, 'fim': paginator.num_pages,
                   'novaconsulta': novaconsulta, # Só aparece se for para agendar uma nova consulta
                   'profid': profid, # idem anterior
                   'periodo': periodo,
                   'data': data,
                   })
    # return JsonResponse(data)

# @
@login_required
def evolucaopacientes(request):

    if request.POST:
        id = request.POST['id']

        anotacoes = request.POST['anotacoes']
        pc = request.POST['paciente']
        anotacaoconsulta = request.POST['anotacaoconsulta']

        try:
            anot = Evolucao.objects.get(pk=id)
        except:
            anot = Evolucao()

        prof = Profissional.objects.get(user=request.user)

        anot.profissional = prof
        anot.anotacoes = anotacoes
        anot.paciente = paciente.objects.get(pk=pc)
        anot.anotacaoconsulta = Consulta.objects.get(pk=anotacaoconsulta)
        anot.ultimaatualizacao = datetime.datetime.now()

        anot.save()

    evolucaoPage = Evolucao.objects.all().order_by('-ultimaatualizacao')

    try:
        pacienteid = request.GET['pacienteid']
        pc = paciente.objects.get(pk=pacienteid)
        evolucaoPage = evolucaoPage.filter(paciente=pc)
    except:
        print('Sem paciente id ')


    paginator = Paginator(evolucaoPage, 8)

    numpages = list(range(1, paginator.num_pages+1))

    # Se nada for fornecido
    try:
        page = request.GET['page']
    except:
        page=0

    atual = 1

    try:
        evolucaoPage = paginator.page(page)
        atual = int(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        evolucaoPage = paginator.page(1)
        # data = serializers.serialize('json', pcientes)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        evolucaoPage = paginator.page(paginator.num_pages)





    return render(request, "evolucaopacientes.html", {'evolucaoanot': evolucaoPage,
                                                      'atual': atual,
                                                      'fim': paginator.num_pages})

def getAnotacao(consulta):

    try:
        evolucao = Evolucao.objects.get(anotacaoconsulta=consulta.id)
        print('Evoluação: ', evolucao.id)

    except:
        # Novo
        evolucao = {'id': -1,
                    'profissional': consulta.profissional.id,
                    'anotacoes':'',
                    'paciente': consulta.paciente.id,
                    'anotacaoconsulta': consulta.id,
                    'ultimaatualizacao': datetime.datetime.now() }


    return evolucao


@login_required
def minhasconsultas(request):
    # configuração e instalação de computadores

    prof = None

    # print("Usuário: ", request.user)

    user = User.objects.get(username=str(request.user))

    if not user.is_staff:
        prof = Profissional.objects.get(user=request.user)

    if request.POST:
        id = request.POST['id']

        anotacoes = request.POST['anotacoes']
        pc = request.POST['paciente']
        anotacaoconsulta = request.POST['anotacaoconsulta']



        try:
            anot = Evolucao.objects.get(pk=id)
        except:
            anot = Evolucao()

        anot.profissional = prof
        anot.anotacoes = anotacoes
        anot.paciente = paciente.objects.get(pk=pc)
        anot.anotacaoconsulta = Consulta.objects.get(pk=anotacaoconsulta)
        anot.ultimaatualizacao = datetime.datetime.now()

        anot.save()




    print("Profissional: ", prof.user.get_full_name())
    #
    data = datetime.date.today()
    #
    # # Pega todos os gets args e monta o form
    idpaciente = 0
    pacientenome = ""
    profissional = ""
    datacad = ""
    periodo = ""
    lastid = ""

    trab = []


    # Tenta pegar de uma só data
    try:
        datacon = request.GET['data']

        try:
            lastid = request.GET['lastid']
        except:
            lastid = ""  # às vezes o algoritmo pode ser ser referenciado sem o ID

        try:
            datacadpy = datetime.datetime.strptime(datacon, '%d/%m/%Y')
        except:
            datacadpy = datetime.datetime.strptime(datacon, '%Y-%m-%d')

        consultasList = Consulta.objects.filter(data=datacadpy, profissional=prof)
        data = datacadpy

        print("Data: ", datacon)

    except Exception as e:
        print("Erro: ", e)
        consultasList = Consulta.objects.filter(data=data, profissional=prof)

        print("Quantidade: ", len(consultasList))

    p = []

    # Verifica se o profissional tem horario na data especificada
    horario = Horario.objects.filter(profissional=prof).filter(
        validadeinicio__lte=data).filter(validadefim__gte=data)

    if (len(horario) > 0):
        # Pega somente o primeiro
        hr = horario[0]

        print("Dia da semana: ", data.isoweekday())

        # Segunda
        manha = 0
        tarde = 0

        if (data.isoweekday() == 1):
            if (hr.segundaM == True):
                manha = 1
            if (hr.segundaT == True):
                tarde = 1
        elif (data.isoweekday() == 2):
            if (hr.tercaM == True):
                manha = 1
            if (hr.tercaT == True):
                tarde = 1
        elif (data.isoweekday() == 3):
            if (hr.quartaM == True):
                manha = 1
            if (hr.quartaT == True):
                tarde = 1
        elif (data.isoweekday() == 4):
            if (hr.quintaM == True):
                manha = 1
            if (hr.quintaT == True):
                tarde = 1
        elif (data.isoweekday() == 5):
            if (hr.sextaM == True):
                manha = 1
            if (hr.sextaT == True):
                tarde = 1


        trab.append(
            [prof.id, manha, tarde])  # zero não tem espediente e 1 tem  -- primeiro é cedo e o outro é de tarde

        p.append(prof)
        print("prof nome: ", prof.user.get_full_name())

    # Fica so quem tem horario
    profs = p

    dictConsultas = []

    for c in consultasList:
        dc = {}
        dc['cs'] = c
        # print("Nome: ", c.paciente.nome )
        dc['anot'] = getAnotacao(c)
        dictConsultas.append(dc)


    print("Tam: ", len(dictConsultas))


    return render(request, "minhasconsultas.html", {'profs': profs,
                                                 'data': data,
                                                 'trab': trab,
                                                 # Dadoslastid do formulário de cadastro
                                                 'idpaciente': idpaciente,
                                                 'pacientenome': pacientenome,
                                                 'profissional': profissional,
                                                 'datacad': datacad,
                                                 # 'cad': cad,
                                                 'consultasList': dictConsultas,
                                                 'lastid': lastid,
                                                 'periodo': periodo})

    # return render(request, "minhasconsultas.html")


def logar(request):
    form = UsuarioForm()
    erro=""

    if request.method == "POST":
        usuario = request.POST['usuario']
        senha = request.POST['senha']

        user = authenticate(username=usuario, password=senha)

        if user is not None:
            login(request, user)

            return redirect("/")
        else:
            erro = "Usuário ou senha estão incorretos"


    return render(request, "logar.html", { 'form': form, 'erro': erro })

#
# @login_required
# def userMan(request):
#
#     form = UserForm()
#
#     return render(request, 'criarusuario.html', {'form': form})




# Horário de cada profissional do caps
@staff_member_required
@login_required
def horarioMaker(request):

    if request.method == "GET":
        idprof = request.GET['profid']
        prof = Profissional.objects.get(pk=int(idprof))


    return render(request, "horario.html", {'prof': prof})







# Horário de cada profissional do caps
@staff_member_required
@login_required
def profissionais(request):
    form = ProfissionalForm()
    er=""
    id=0
    action=""
    if request.method == "POST":
        form = ProfissionalForm(request.POST)

        if form.is_valid():

            id = int(request.POST['id'])

            if id == 0:
                print("Opção 1")
                pc = form.save(commit=False)
                pc.id = None
                pc.save()
            else:
                pc = form.save(commit=False)
                pc.id = id
                print("Opção 2")
                print("ID: ", pc.id)
                pc.save()

            return redirect("/cadprofissionais")
        else:
            er = 1
            print("Form: ", form.errors)
    else:
        try:
            id = int(request.GET['profid'])

            if id != 0:
                prof = Profissional.objects.get(pk=int(id))
                action="editar"
                print("Encontrei o professor: ", prof.nome)
                form = ProfissionalForm(instance=prof)
        except:
            pass


    return render(request, "profissionais.html", {"form": form, 'er': er, 'id': id, 'action': action })



@staff_member_required
@login_required
def profissionaislist(request):

    if request.method =="POST":
        pesq = request.POST['pesquisa']
        profs = Profissional.objects.filter(nome__contains=pesq)
    else:
        profs = Profissional.objects.all()



    return render(request, "profissionaislist.html", {"profs": profs})


@staff_member_required
@login_required
def remConsulta(request):
    try:
        id = request.POST['id']
        resp = {}

        consulta = Consulta.objects.get(pk=int(id))
        resp['lastid'] = consulta.profissional_id
        consulta.delete()



        return JsonResponse(resp)
    except:
        return HttpResponse(-1)

@staff_member_required
@login_required
def newhorario(request):
    form = HorarioForm()
    erro = ""
    prof = "Horário de "
    hora = Horario()

    try:
        idhorario = int(request.GET['idhorario'])
    except:
        idhorario=0

    try:
        idprof = int(request.GET['idprof'])
        p = Profissional.objects.get(pk=idprof)
        hora.profissional = p
    except:
        return HttpResponse("Forneça os parâmetros de maneira correta!!!!<br />")


    if request.method == "POST":
        form = HorarioForm(request.POST)

        if form.is_valid():

            #Id do horario
            id = request.POST['id']

            if id is not None and id != "None":
                hora = form.save(commit=False)
                validadeinicio = request.POST['validadeinicio']
                validadefim = request.POST['validadefim']

                validadeinicio = datetime.datetime.strptime(validadeinicio, '%d/%m/%Y')
                validadefim = datetime.datetime.strptime(validadefim, '%d/%m/%Y')

                hora.validadeinicio = validadeinicio.date()
                hora.validadefim = validadefim.date()

                # print("Data inicio: ", validadeinicio)
                # print("Data fim: ", validadefim)
                # print("ID: ", id)
                hora.id = int(id)
                # print("Opção 2")
                # print("ID: ", pc.id)

                # Valida o salvamento dos itens
                # Caso jatem retorn uma lista maior que 0, o funcionário já tem um paciente
                jatem = Horario.objects.filter(profissional_id__exact=hora.profissional.id).filter(
                    validadefim__gte=hora.validadeinicio).filter(
                    validadeinicio__lte=hora.validadeinicio).exclude(id=hora.id)

                # Não pode estar no intervalo: hora.validadefim <=validadefim and  hora.validadeinicio>=validadeinicio>=
                jatem2 = Horario.objects.filter(profissional_id__exact=hora.profissional.id).filter(
                    validadefim__gte=hora.validadefim).filter(
                    validadeinicio__lte=hora.validadefim).exclude(id=hora.id)

                # print("Hora fim: ", hora.validadefim)
                # print("Hora inicio query: ", jatem2[0].validadeinicio)


                print("jatem1: ", len(jatem))
                print("jatem2: ", len(jatem2))


                if len(jatem) == 0  and len(jatem2) == 0 and hora.validadefim >= hora.validadeinicio:
                    hora.save()
                else:
                    erro = "Atenção, já um horário no período especificado. "

                if hora.validadefim < hora.validadeinicio:
                    erro += " A data de fim deve ser superior ao do início. "


            else:
                hora = form.save(commit=False)
                validadeinicio = request.POST['validadeinicio']
                validadefim = request.POST['validadefim']
                hora.id = None
                #
                # print("Data inicio Passado: ", validadeinicio)
                # print("Data inicio Passado: ", validadefim)

                hora.validadeinicio = datetime.datetime.strptime(validadeinicio, '%d/%m/%Y').date()
                hora.validadefim = datetime.datetime.strptime(validadefim, '%d/%m/%Y').date()

                # print("Data inicio Passado2: ", pc.validadeinicio)
                # print("Data inicio Passado2: ", pc.validadefim)


                # Não pode estar no intervalo: hora.validadeinicio <=validadefim and validadeinicio>=hora.validadeinicio
                jatem = Horario.objects.filter(profissional_id__exact=hora.profissional.id).filter(
                    validadefim__gte=hora.validadeinicio).filter(
                    validadeinicio__lte=hora.validadeinicio).exclude(id=hora.id)

                # Não pode estar no intervalo: hora.validadefim <=validadefim and  hora.validadeinicio>=validadeinicio>=
                jatem2 = Horario.objects.filter(profissional_id__exact=hora.profissional.id).filter(
                    validadefim__gte=hora.validadefim).filter(
                    validadeinicio__lte=hora.validadefim).exclude(id=hora.id)

                # print("Hora fim: ", hora.validadefim)
                # print("Hora inicio query: ", jatem2[0].validadeinicio)


                print("jatem1: ", len(jatem))
                print("jatem2: ", len(jatem2))



                if len(jatem) == 0 and len(jatem2) == 0 and hora.validadefim >= hora.validadeinicio:
                    hora.save()
                else:
                    erro = "Atenção, já um horário no período especificado."


                if hora.validadefim <= hora.validadeinicio:
                    erro += " A data de fim deve ser superior ao do início."

                # if hora.horainicioM > hora.horafimM:
                #     erro += " Hora início matutino é maior que a hora fim."
                #
                # if hora.horainicioT > hora.horafimT:
                #     erro += " Hora início da tarde é maior que a hora fim."
                #


        else:
            erro="Erro diversos"
            print("Dados não válidos", form.errors)

        if erro == "":
            print("idprof: ", idprof)


            return redirect("/horariolist?idprof="+str(idprof))
        else:
            prof += hora.profissional.user.get_full_name()

            if idhorario ==0:
                prof += " - Novo"


    if idhorario > 0 and erro == "":
        hora = Horario.objects.get(pk=idhorario)
        form = HorarioForm(instance=hora)
        prof += hora.profissional.user.get_full_name()

    if idhorario==0 and erro == "":
        p = Profissional.objects.get(pk=idprof)
        p.nome = ""
        prof += p.user.get_full_name() + " - Novo"

    return render(request, "newhorario.html", {'form': form, 'hora': hora, 'prof': prof, 'profid': idprof, 'erro': erro } )
    # return render(request, 'testeform.html', {'form': form})

@staff_member_required
@login_required
def horariolist(request):
    try:
        idprof = int(request.GET['idprof'])
        p = Profissional.objects.get(pk=idprof)
        horarios = Horario.objects.filter(profissional=p).order_by("-validadefim")
    except: # todos os profissionais
        return HttpResponse("Forneça idprof como parâmetro")


    return render(request, "horariolist.html", {'horarios': horarios, 'idprof': idprof, 'prof': p})


@staff_member_required
def teste(request):
    form = HorarioForm()

    return render(request, "teste.html", {'form': form })

@staff_member_required
@login_required
def jsont(request):
    import random
    data = datetime.datetime.today()

    inf = {}
    inf['data'] = data
    inf['id'] = random.randint(0, 1000)

    return JsonResponse(inf)

@staff_member_required
@login_required
def consultas(request):
    # configuração e instalação de computadores

    profs = Profissional.objects.all()

    data = datetime.date.today()

    # Pega todos os gets args e monta o form
    idpaciente = 0
    pacientenome = ""
    profissional = ""
    datacad = ""
    periodo = ""
    lastid = ""

    trab = []

    # Tenta pegar os argumentos acima
    try:
        idpaciente = request.GET['pacienteid']
        pacientenome = paciente.objects.get(pk=idpaciente)

        periodo = request.GET['periodo']
        datacad = request.GET['data']

        profid = request.GET['profid']
        profissional = Profissional.objects.get(pk=profid)
        cad = '1'
    except:
        print("Ocorreu um erro!!!")
        cad='0'

    try:
        datacon = request.GET['data']

        try:
            lastid = request.GET['lastid']
        except:
            lastid = "" # às vezes o algoritmo pode ser ser referenciado sem o ID

        try:
            datacadpy = datetime.datetime.strptime(datacon, '%d/%m/%Y')
        except:
            datacadpy = datetime.datetime.strptime(datacon, '%Y-%m-%d')


        consultasList = Consulta.objects.filter(data=datacadpy)
        data = datacadpy

        print("Data: ", datacon)

    except Exception as e:
        print("Erro: ", e)
        consultasList = Consulta.objects.filter(data=data)

    p = []
    for pf in profs:
        # Verifica se o profissional tem horario na data especificada
        horario = Horario.objects.filter(profissional=pf).filter(
            validadeinicio__lte=data).filter(validadefim__gte=data)


        if ( len(horario)>0 ):
            # Pega somente o primeiro
            hr = horario[0]

            print("Dia da semana: ", data.isoweekday())

            # Segunda
            manha = 0
            tarde = 0
            if (data.isoweekday() == 1):
                if (hr.segundaM == True):
                    manha = 1
                if (hr.segundaT == True):
                    tarde = 1
            elif (data.isoweekday() == 2):
                if (hr.tercaM== True):
                    manha = 1
                if (hr.tercaT == True):
                    tarde = 1
            elif (data.isoweekday() == 3):
                if (hr.quartaM == True):
                    manha = 1
                if (hr.quartaT == True):
                    tarde = 1
            elif (data.isoweekday() == 4):
                if (hr.quintaM == True):
                    manha = 1
                if (hr.quintaT == True):
                    tarde = 1
            elif (data.isoweekday() == 5):
                if (hr.sextaM == True):
                    manha = 1
                if (hr.sextaT == True):
                    tarde = 1
            else:
                # não se trabalha no sábado e no domingo
                break

            trab.append( [pf.id, manha, tarde]) # zero não tem espediente e 1 tem  -- primeiro é cedo e o outro é de tarde




            p.append(pf)
            print("prof nome: ", pf.nome)

    # Fica so quem tem horario
    profs = p

    return render(request, "consultalist.html", {'profs': profs,
                                                 'data': data,
                                                 'trab': trab,
                                                  # Dadoslastid do formulário de cadastro
                                                 'idpaciente': idpaciente,
                                                 'pacientenome': pacientenome,
                                                 'profissional': profissional,
                                                 'datacad': datacad,
                                                 'cad': cad,
                                                 'consultasList': consultasList,
                                                 'lastid': lastid,
                                                 'periodo': periodo})

@staff_member_required
@login_required
def marcarconsulta(request):
    # Recebe um submit do formulário em aJax

    # Caso esteja Ok o sistema atualiza a página
    # Caso contrário, o sistema irá mostrar o erro

    try:
        datacad = request.POST['datacad']
        idprofissional = request.POST['idprofissional']
        idpaciente = request.POST['idpaciente']
        horariocad = request.POST['horariocad']
        periodo = request.POST['periodo']

        # Parse datacad do formato dd/mm/YY

        datacadpy = datetime.datetime.strptime(datacad, '%d/%m/%Y')

        consulta = Consulta()
        consulta.data = datacadpy
        consulta.hora = horariocad
        consulta.profissional = Profissional.objects.get(pk=int(idprofissional))
        consulta.paciente = paciente.objects.get(pk=int(idpaciente))
        consulta.periodo = periodo
        consulta.status = "pend" # Situação da atividade



        # Associar um horário a consulta
        # Fica mais fácil de identificar

        try:
            horario = Horario.objects.filter(profissional=consulta.profissional).order_by("-validadefim").filter(
                validadeinicio__lte=consulta.data).filter(validadefim__gte=consulta.data)

            print("Eu encontrei um horário para esta consulta?")
            print("Tam: ", len(horario) )

            horario = horario[0]
            consulta.horario = horario


            # Avalia de acordo com a quantidade máxima configurada no banco de dados
            consultasPeriodo = Consulta.objects.filter(profissional=consulta.profissional)\
                .filter(data=consulta.data)\
                .filter(periodo=consulta.periodo).exclude(status='des').exclude(status='falt').exclude(status='rem')


            if (len(consultasPeriodo)>= consulta.profissional.quantmaxconsulta):
                return HttpResponse(-2) # quantidade máxima excedida


        except:
            print("Erro do pesquisar por horarios")

            # Não pode marcar uma consulta para alguém que não tem uma
            return HttpResponse(-1)


        consulta.save()

        print("Salvo com sucesso!!!!")


        resp = {}
        resp['lastid'] = consulta.profissional.id
        resp['data'] = datacad

        return JsonResponse(resp)

    except Exception as e:

        print("Erro:")
        print(e)
        # Erro
        return HttpResponse(-1)

@staff_member_required
@login_required
def changeStatus(request):


    if request.method=="POST":

        try:
            id = request.POST['idconsulta']
            status = request.POST['status']
            anotacao = request.POST['anotacao']

            con = Consulta.objects.get(pk=int(id))
            con.status = status
            con.anotacoes = anotacao
            con.save()

            print("Salvo com sucesso!!!")
            return HttpResponse(1)
        except:
            print("Erro")

            return HttpResponse(-1)


    else:
        return HttpResponse(-1)

@staff_member_required
@login_required
def disponibilidade(request):

    if request.method == "GET":
        idprof = request.GET['idprof']
        prof = Profissional.objects.get(pk=int(idprof))

        print("Idprof: ", idprof)
        print("Idprof: ", prof.nome)


    return HttpResponse("Executei a bagaça!!!!!!!!!")

# @staff_member_required
@login_required
def diasDisponiveis(request):
    data = datetime.date.today()
    nome=""

    dias = []
    horario=""

    try:
        # Quem usa isto é o staff
        idprof = request.GET['idprof']
        prof = Profissional.objects.get(pk=int(idprof))
    except:
        prof = Profissional.objects.get(user=request.user)

    nome = prof.user.get_full_name()

    consultasprof = Consulta.objects.filter(profissional=prof).order_by('-data')


    data = datetime.date.today()

    horario = Horario.objects.filter(profissional=prof).filter(
        validadeinicio__lte=data).filter(validadefim__gte=data)


    try:
        horario = horario[0]
    except:
        return HttpResponse("<h1>Defina um horário para este profissional</h1>")

    diff = horario.validadefim - data

    # DIAS QUE TRABALHA
    diastrab = []
    if horario.segundaM or horario.segundaT:
        diastrab.append(1)

    if horario.tercaM or horario.tercaT:
        diastrab.append(2)

    if horario.quartaM or horario.quartaT:
        diastrab.append(3)

    if horario.quintaM or horario.quintaT:
        diastrab.append(4)

    if horario.sextaM or horario.sextaT:
        diastrab.append(5)


    # DIAS MATUTINO
    diasmat = []
    if horario.segundaM:
        diasmat.append(1)

    if horario.tercaM:
        diasmat.append(2)

    if horario.quartaM:
        diasmat.append(3)

    if horario.quintaM:
        diasmat.append(4)

    if horario.sextaM:
        diasmat.append(5)

    # DIAS VESPERTINO
    # DIAS QUE TRABALHA
    diasvesp = []
    if horario.segundaT:
        diasvesp.append(1)

    if horario.tercaT:
        diasvesp.append(2)

    if horario.quartaT:
        diasvesp.append(3)

    if horario.quintaT:
        diasvesp.append(4)

    if horario.sextaT:
        diasvesp.append(5)


    for i in range(diff.days + 1):
        dia = data + timedelta(days=i)

        # Tira o sábado e o domingo
        if dia.isoweekday() > 5 :
            continue

        # Se tiver um dia que o profissional não trabalha ... então este dia não estará nos dias disponíveis
        if dia.isoweekday() not in diastrab:
            continue
        qmat = []
        qvesp = []

        # Contar somente os concluídos e pendentes


        # CONSULTA = (
        #     ('pend', 'Pendente'),
        #     ('des', 'Desistir'),
        #     ('rem', 'Remarcar'),
        #     ('falt', 'Faltou'),
        #     ('conc', 'Concluído'),
        # )
        if dia.isoweekday() in diasmat:
            qmat = Consulta.objects.filter(profissional=prof).order_by('-data').filter(data=dia).filter(periodo='mat').filter(Q(status='conc')| Q(status='pend'))

        if dia.isoweekday() in diasvesp:
            qvesp = Consulta.objects.filter(profissional=prof).order_by('-data').filter(data=dia).filter(
                periodo='ves').filter(Q(status='conc')| Q(status='pend'))

        consultasprof = Consulta.objects.filter(profissional=prof).order_by('-data').filter(data=dia).filter(Q(status='conc')| Q(status='pend'))

        d = {}
        d['dia'] = dia
        d['quant'] = len(consultasprof)


        try:
            quant=prof.quantmaxconsulta+1
        except:
            prof.quantmaxconsulta=0

        if dia.isoweekday() in diasmat:
            d['quantm'] = len(qmat)
            d['dispm'] = prof.quantmaxconsulta - len(qmat)
        else:
            d['dispm'] = ''
            d['quantm'] = ''

        if dia.isoweekday() in diasvesp:
            d['quantv'] = len(qvesp)
            d['dispv'] = prof.quantmaxconsulta - len(qvesp)
        else:
            d['dispv'] = ''
            d['quantv'] = ''

        d['profid'] = prof.id

        print("Quantidade: ", d['quant'])



        dias.append(d)
        # Para cada dia, pesquisa-se



    return render(request, "diaslivres.html", {'profissional': "profissional",
                                               'datainicial': data,
                                               'datafinal': horario.validadefim,
                                               'nome': nome,
                                               'dias': dias})

@staff_member_required
@login_required
def cadconsulta(request):

    form = ConsultaForm()

    return render(request, "consultacad.html", {'form': form})

@staff_member_required
@login_required
def teste2(request):
    form = ConsultaForm()
    # t = input("Digite um valor")
    
    return render(request, "logar.html", {'form': form})

@staff_member_required
@login_required
def paci(request):
    paci = PacientForm()

    return render(request, {'form': paci})

