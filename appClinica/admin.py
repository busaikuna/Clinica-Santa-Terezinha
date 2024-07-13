from django.contrib import admin
from .models import Paciente, Internaçao

class InternacaoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'data_solicitacao', 'diagnostico_inicial')
    search_fields = ('paciente__nome', 'diagnostico_inicial')
    list_filter = ('data_solicitacao',)
    fieldsets = (
        ('Informações do Paciente', {
            'fields': ('paciente', 'cartao_nacional_saude', 'raca', 'data_nascimento', 'sexo', 'numero_prontuario', 'nome_mae', 'documento_identificacao', 'endereco', 'municipio_residencia', 'telefone')
        }),
        ('Justificativa da Internação', {
            'fields': ('principais_sinais_sintomas_clinicos', 'condicoes_justificam_internacao', 'principais_resultados_exames', 'diagnostico_inicial', 'cid10_principal', 'cid10_secundario', 'cid10_associadas')
        }),
        ('Procedimento Solicitado', {
            'fields': ('descricao_procedimento', 'codigo_procedimento', 'clinica', 'carater_internacao', 'documento_prof_solicitante', 'cns_prof_solicitante', 'cpf_prof_solicitante', 'nome_profissional_solicitante', 'data_solicitacao', 'assinatura_medico')
        }),
        ('Preenchimento em Caso de Causa Externas', {
            'fields': ('acidente_transito', 'acidente_trabalho_tipico', 'acidente_trabalho_trajeto', 'cnpj_seguradora', 'numero_bilhete', 'serie', 'cnpj_empresa', 'numero_bilhete_empresa', 'serie_empresa')
        }),
        ('Vínculo com a Previdência', {
            'fields': ('emprego', 'autonomo', 'desempregado', 'aposentado', 'nao_segurado')
        }),
        ('Autorização', {
            'fields': ('nome_profissional_autorizador', 'cod_crm', 'numero_autorizacao_internacao', 'cns_autorizador', 'cpf_autorizador', 'data_autorizacao', 'assinatura_carimbo', 'assinatura_paciente_responsavel')
        }),
    )

class InternacaoInline(admin.StackedInline):
    model = Internaçao
    extra = 1

class PacienteAdmin(admin.ModelAdmin):
    search_fields = ('nome',)
    inlines = [InternacaoInline]

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Internaçao, InternacaoAdmin)
