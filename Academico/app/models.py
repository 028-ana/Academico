from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome completo")
    pai = models.CharField(max_length=100, verbose_name="Nome do pai")
    mae = models.CharField(max_length=100, verbose_name="Nome da mãe")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.EmailField(max_length=100, verbose_name="Email")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da instituição")
    site = models.CharField(max_length=100, verbose_name="Site da instituição")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE, verbose_name="Cidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de Ensino"

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da área do saber")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Área do Saber"
        verbose_name_plural = "Áreas do Saber"


class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do curso")
    carga_horaria_total = models.IntegerField(verbose_name="Carga horária total")
    duracao_meses = models.IntegerField(verbose_name="Duração em meses")
    area_saber = models.ForeignKey('AreaSaber', on_delete=models.CASCADE, verbose_name="Área do saber")
    instituicao = models.ForeignKey('InstituicaoEnsino', on_delete=models.CASCADE, verbose_name="Instituição de Ensino")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da turma")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")

    def __str__(self):
        return f"{self.nome} - {self.curso.nome}"

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da disciplina")
    area_saber = models.ForeignKey('AreaSaber', on_delete=models.CASCADE, verbose_name="Área do saber")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"


class Matricula(models.Model):
    instituicao = models.ForeignKey('InstituicaoEnsino', on_delete=models.CASCADE, verbose_name="Instituição de Ensino")
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, verbose_name="Curso")
    pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE, verbose_name="Pessoa")
    data_inicio = models.DateField(verbose_name="Data de início")
    data_previsao_termino = models.DateField(verbose_name="Data prevista de término")

    def __str__(self):
        return f"{self.pessoa.nome} - {self.curso.nome}"

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"


class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo de avaliação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Avaliação"
        verbose_name_plural = "Tipos de Avaliação"


class Avaliacao(models.Model):
    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE, verbose_name="Disciplina")
    tipo = models.ForeignKey('AvaliacaoTipo', on_delete=models.CASCADE, verbose_name="Tipo de Avaliação")

    def __str__(self):
        return f"{self.descricao} - {self.disciplina.nome}"

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"


class Frequencia(models.Model):
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE, verbose_name="Pessoa")
    numero_faltas = models.IntegerField(verbose_name="Número de faltas")

    def __str__(self):
        return f"{self.pessoa.nome} - {self.disciplina.nome}"

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"


class Turno(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do turno")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=200, verbose_name="Descrição da ocorrência")
    data = models.DateField(verbose_name="Data da ocorrência")
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE, verbose_name="Pessoa")

    def __str__(self):
        return f"{self.descricao[:30]} - {self.data}"

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"


class Periodo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do período")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Período"
        verbose_name_plural = "Períodos"


class CursoDisciplina(models.Model):
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE, verbose_name="Disciplina")
    carga_horaria = models.IntegerField(verbose_name="Carga horária")
    periodo = models.ForeignKey('Periodo', on_delete=models.CASCADE, verbose_name="Período")

    def __str__(self):
        return f"{self.curso.nome} - {self.disciplina.nome} - {self.periodo.nome}"

    class Meta:
        verbose_name = "Curso/Disciplina"
        verbose_name_plural = "Curso/Disciplinas"


class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo de avaliação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Avaliação"
        verbose_name_plural = "Tipos de Avaliação"
