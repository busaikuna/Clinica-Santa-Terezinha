# appClinica/models.py

from django.db import models

class Paciente(models.Model):
    nome_do_paciente = models.CharField(max_length=100, blank=True, null=True)
    n_registro = models.CharField(max_length=15, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    data_nascimento = models.DateField(blank=True, null=True)
    nome_do_pai = models.CharField(max_length=100, blank=True, null=True)
    nome_da_mae = models.CharField(max_length=100, blank=True, null=True)
    responsavel = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    tipo_saida = models.CharField(max_length=100, blank=True, null=True)
    data_saida = models.DateField(blank=True, null=True)
    data_entrada = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Internaçao(models.Model):
    # Identificação do Estabelecimento de Saúde
    nome_estabelecimento_solicitante = models.CharField(max_length=255)
    cnes_solicitante = models.CharField(max_length=7)
    nome_estabelecimento_executante = models.CharField(max_length=255)
    cnes_executante = models.CharField(max_length=7)
    
    # Identificação do Paciente
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    cartao_nacional_saude = models.CharField(max_length=15)
    raca = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    numero_prontuario = models.CharField(max_length=20, blank=True, null=True)
    nome_mae = models.CharField(max_length=255)
    documento_identificacao = models.CharField(max_length=50)
    endereco = models.CharField(max_length=255)
    municipio_residencia = models.CharField(max_length=100)
    cod_ibge_municipio = models.CharField(max_length=7)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    telefone = models.CharField(max_length=15)
    
    # Justificativa da Internação
    principais_sinais_sintomas_clinicos = models.TextField(blank=True, null=True)
    condicoes_justificam_internacao = models.TextField(blank=True, null=True)
    principais_resultados_exames = models.TextField(blank=True, null=True)
    diagnostico_inicial = models.TextField(blank=True, null=True)
    cid10_principal = models.CharField(max_length=10)
    cid10_secundario = models.CharField(max_length=10, blank=True, null=True)
    cid10_associadas = models.CharField(max_length=10, blank=True, null=True)
    
    # Procedimento Solicitado
    descricao_procedimento = models.TextField()
    codigo_procedimento = models.CharField(max_length=10)
    clinica = models.CharField(max_length=255)
    carater_internacao = models.CharField(max_length=255)
    documento_prof_solicitante = models.CharField(max_length=20)
    cns_prof_solicitante = models.CharField(max_length=15)
    cpf_prof_solicitante = models.CharField(max_length=11)
    nome_profissional_solicitante = models.CharField(max_length=255)
    data_solicitacao = models.DateField()
    assinatura_medico = models.CharField(max_length=255)
    
    # Preenchimento em Caso de Causa Externas
    acidente_transito = models.BooleanField(default=False)
    acidente_trabalho_tipico = models.BooleanField(default=False)
    acidente_trabalho_trajeto = models.BooleanField(default=False)
    cnpj_seguradora = models.CharField(max_length=14, blank=True, null=True)
    numero_bilhete = models.CharField(max_length=20, blank=True, null=True)
    serie = models.CharField(max_length=20, blank=True, null=True)
    cnpj_empresa = models.CharField(max_length=14, blank=True, null=True)
    numero_bilhete_empresa = models.CharField(max_length=20, blank=True, null=True)
    serie_empresa = models.CharField(max_length=20, blank=True, null=True)
    
    # Vínculo com a Previdência
    emprego = models.BooleanField(default=False)
    autonomo = models.BooleanField(default=False)
    desempregado = models.BooleanField(default=False)
    aposentado = models.BooleanField(default=False)
    nao_segurado = models.BooleanField(default=False)
    
    # Autorização
    nome_profissional_autorizador = models.CharField(max_length=255)
    cod_crm = models.CharField(max_length=20)
    numero_autorizacao_internacao = models.CharField(max_length=20)
    cns_autorizador = models.CharField(max_length=15)
    cpf_autorizador = models.CharField(max_length=11)
    data_autorizacao = models.DateField()
    assinatura_carimbo = models.CharField(max_length=255)
    assinatura_paciente_responsavel = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Internações"

    def __str__(self):
        return f'Internação de {self.nome_paciente} - {self.data_solicitacao}'
