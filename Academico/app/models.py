from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Instituicao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da instituição")
    site = models.CharField(max_length=100, verbose_name="Site")
    telefone = models.CharField(max_length=11, verbose_name="Telefone")
    cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE, verbose_name="Cidade")

    
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Área do saber")

    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Área do saber"
        verbose_name_plural = "Áreas do saber"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupação")

    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

class Pessoas(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da pessoa")
    pai = models.CharField(max_length=100, verbose_name="Nome do pai")
    mae = models.CharField(max_length=100, verbose_name="Nome da mãe")
    cpf = models.CharField(max_length=11, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.CharField(max_length=100, verbose_name="Email")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupaçao")

    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Cursos(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do curso")
    carga_horaria_total = models.CharField(max_length=4, verbose_name="Carga horaria total")
    duracao_meses = models.CharField(max_length=2, verbose_name="Duração meses")
    area_saber = models.ForeignKey(AreaSaber,on_delete=models.CASCADE, verbose_name="Área do saber")
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name ="Nome da instituição")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"


class PeriodoCurso(models.Model):
    numero = models.IntegerField(verbose_name="Numero periodo")

    def __str__(self):
        return f"{self.numero}"
    class Meta:
        verbose_name = "Periodo do curso"
        verbose_name_plural = "Periodos do curso"


class Disciplinas(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da disciplina")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do saber")

    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituição")
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Cursos")
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE, verbose_name="Pessoa")
    data_inicio = models.DateField( verbose_name="Data de inicio")
    data_prev_termino = models.DateField( verbose_name = "Data previsão termino")
    def __str__(self):
        return f"{self.instituicao}, {self.curso}, {self.pessoa},{self.data_inicio}, {self.data_prev_termino}"
    class Meta:
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"


class Avaliacoes(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Cursos")
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE, verbose_name="Disciplinas")
    def __str__(self):
        return f"{self.descricao}, {self.curso}, {self.disciplina}"
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

class Frequencia(models.Model):
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE, verbose_name="Pessoa")
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Cursos")
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE, verbose_name="Disciplinas")
    numero_faltas = models.CharField(max_length=100, verbose_name="Faltas")

    def __str__(self):
        return f"{self.pessoa}, {self.curso}, {self.disciplina}, {self.numero_faltas}"
    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"


class Turmas(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da turma")
    periodo = models.CharField(max_length=100, verbose_name="Periodo")

    def __str__(self):
        return f"{self.nome}, {self.periodo}"
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

class Ocorrencias(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    data = models.DateField(verbose_name = "Data")
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE, verbose_name="Pessoa")
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Cursos")
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE, verbose_name="Disciplinas")

    def __str__(self):
        return f"{self.descricao},{self.data},{self.pessoa}, {self.curso}, {self.disciplina}"
    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"

class DiciplinaCurso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da disciplina do curso")
    carga_horaria = models.CharField(max_length=100, verbose_name="Carga horaria")
    periodo = models.ForeignKey(PeriodoCurso, on_delete=models.CASCADE, verbose_name="Periodo")
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Cursos")
    def __str__(self):
        return f"{self.nome},{self.carga_horaria},{self.periodo}, {self.curso}"
    class Meta:
        verbose_name = "Diciplina curso"
        verbose_name_plural = "Disciplinas curso"

class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo de avalição")

    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Tipo avaliação"
        verbose_name_plural = "Tipos avaliações"