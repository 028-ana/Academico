from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html') 
    

class PessoasView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoas.objects.all()
        return render(request, 'pessoas.html', {'pesssoas' : pessoas})

class AreaSaberView(View):
    def get(self, request, *args, **kwargs):
        area_saber = AreaSaber.objects.all()
        return render(request, 'area_saber.html', {'area_saber' : area_saber})

class AvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        avaliacao = Avaliacoes.objects.all()
        return render(request, 'avaliacoes.html', {'avaliacao' : avaliacao})

class CidadeView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidades.html', {'cidades' : cidades})

class CursosView(View):
    def get(self, request, *args, **kwargs):
        curso = Cursos.objects.all()
        return render(request, 'cursos.html', {'curso' : curso})
    
class DisciplinaCursoView(View):
    def get(self, request, *args, **kwargs):
        disciplina_curso = DiciplinaCurso.objects.all()
        return render(request, 'disciplina_curso.html', {'disciplina_curso' : disciplina_curso})
    
class DisciplinaView(View):
    def get(self, request, *args, **kwargs):
        disciplina = Disciplinas.objects.all()
        return render(request, 'disciplinas.html', {'disciplina' : disciplina})    
    

class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        frequencia = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencia' : frequencia})    
    

class InstituicaoView(View):
    def get(self, request, *args, **kwargs):
        instituicao = Instituicao.objects.all()
        return render(request, 'instituicao.html', {'instituicao' : instituicao})    
    

class MatriculaView(View):
    def get(self, request, *args, **kwargs):
        matricula = Matricula.objects.all()
        return render(request, 'matricula.html', {'matricula' : matricula})        
    

class OcorrenciaView(View):
    def get(self, request, *args, **kwargs):
        ocorrencia = Ocorrencias.objects.all()
        return render(request, 'ocorrencias.html', {'ocorrencia' : ocorrencia})    
    

class OcupacaoView(View):
    def get(self, request, *args, **kwargs):
        ocupacao = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacao' : ocupacao})    
    

class PeriodoCursoView(View):
    def get(self, request, *args, **kwargs):
        periodo_curso = PeriodoCurso.objects.all()
        return render(request, 'periodo_cursos.html', {'periodo_curso' : periodo_curso})    

class PessoasView(View):
    def get(self, request, *args, **kwargs):
        pessoa = Pessoas.objects.all()
        return render(request, 'pessoas.html', {'pessoa' : pessoa})    

class TipoAvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        tipo_avaliacao = TipoAvaliacao.objects.all()
        return render(request, 'tipo_avaliacao.html', {'tipo_avaliacao' : tipo_avaliacao})    


class TurmaView(View):
    def get(self, request, *args, **kwargs):
        turma = Turmas.objects.all()
        return render(request, 'turmas.html', {'turma' : turma})