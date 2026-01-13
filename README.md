# AdaptaNote - Gerador de Atividades Acessíveis

AdaptaNote é uma plataforma pensada para educadores que precisam adaptar conteúdos curriculares para estudantes com deficiência intelectual, TEA, TDAH ou outras dificuldades de aprendizagem. A aplicação combina geração automática de conteúdo pedagógico com controles de acessibilidade, simplificando a produção de atividades e avaliações em questão de minutos.

## Persona
- **Quem usa:** Professores de sala regular, docentes de Atendimento Educacional Especializado (AEE) e terapeutas educacionais.
- **Necessidade:** Criar rapidamente materiais adaptados com diferentes níveis de complexidade, mantendo alinhamento com o currículo.

## Problema
Educadores gastam horas procurando imagens, simplificando textos e formatando atividades acessíveis. O processo manual é exaustivo e dificulta a oferta de materiais personalizados para cada aluno.

## Objetivo do Produto
Permitir que o usuário informe um tema e receba um documento adaptado automaticamente, pronto para impressão ou uso digital, reduzindo drasticamente o tempo de preparação de atividades.

## Funcionalidades Essenciais

### 1. Geração de Conteúdo por Tema
- **Entrada:** tema central (ex.: "Ciclo da Água", "Verbos no passado").
- **Saída:** texto explicativo conciso + conjunto de questões base.
- **Detalhes técnicos:**
  - Motor de geração textual baseado em LLM com prompt ajustado para linguagem pedagógica.
  - Controles de temperatura para manter consistência terminológica.

### 2. Níveis de Adaptação
- **Seleção do usuário:** Nível 1, 2 ou 3.
- **Processamento:** pipeline de transformação que reescreve textos, ajusta tipos de questões e sugere recursos de apoio visual conforme o nível escolhido.
- **Especificações de nível:**
  - **Nível 1 – Simplificação leve:** textos curtos, questões objetivas, múltipla escolha com até 3 alternativas.
  - **Nível 2 – Suporte visual amplo:** frases de 1-2 linhas, atividades de associação (ligar, circular), pareamento imagem-palavra.
  - **Nível 3 – Adaptação profunda:** foco em imagens e vocabulário mínimo, respostas "sim/não" ou apontar figuras.

### 3. Banco de Imagens Inteligente
- **Automação:** seleção de pictogramas ou ilustrações simples para conceitos-chave.
- **Fontes:** integração com bibliotecas livres (ex.: OpenMoji, TheNounProject) com filtros por estilo e direitos de uso.
- **Entrega:** cada questão/alternativa relevante recebe imagem correspondente.

### 4. Instruções Claras
- **Opção do usuário:** checkbox "Incluir Instruções".
- **Geração:**
  - **Aluno:** comandos diretos ("Pinte a resposta certa.").
  - **Aplicador/Professor:** orientações de mediação ("Leia a pergunta em voz alta, aponte para as imagens...").

### 5. Exportação
- **Formatos:** `.docx` e Google Docs.
- **Implementação sugerida:**
  - Uso de `python-docx` ou `docx-compose` para gerar arquivo local.
  - Integração com Google Drive API para criar cópia editável.
  - Garantia de preservação de layout (texto + imagens + instruções).

## Arquitetura Proposta

```text
frontend/ (Next.js ou React + Tailwind)
└─ components/ActivityPreview
backend/ (FastAPI ou Django)
└─ services/
   ├─ content_generator.py   # prompts e pós-processamento
   ├─ adaptation_engine.py   # aplica níveis de adaptação
   ├─ image_retriever.py     # busca e seleciona imagens
   ├─ export_service.py      # gera .docx ou Google Docs
   └─ instructions_builder.py
infra/
└─ pipelines/llm_prompts.yaml
```

### Fluxo de dados
1. Usuário envia tema + preferências.
2. Backend chama `content_generator` para criar base textual.
3. `adaptation_engine` ajusta o conteúdo conforme nível.
4. `image_retriever` associa pictogramas.
5. `instructions_builder` gera instruções opcionais.
6. `export_service` compila tudo e entrega o documento.

## Roadmap Inicial
1. Prototipar interface de entrada de tema e visualização de prévia.
2. Implementar prompts e regras de adaptação para os três níveis.
3. Integrar banco de imagens livre com cache local.
4. Construir exportação `.docx` + integração Google Docs.
5. Testar com educadores e iterar com base no feedback.

## Métricas de Sucesso
- Tempo médio de criação de atividade < 5 minutos.
- Taxa de reutilização de atividades > 60%.
- Satisfação do usuário (NPS) >= 8.

## Como testar rapidamente
O repositório inclui um protótipo em linha de comando que permite gerar atividades fictícias de maneira
rápida. Para instalar as dependências (apenas Python padrão) e executar:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .  # opcional, apenas para uso em outros projetos
python main.py "Ciclo da Água" --level 2
```

Também há testes automatizados básicos executáveis com `pytest`:

```bash
pip install pytest
pytest
```

## Licença
Projeto em desenvolvimento. Definir licença conforme diretrizes da organização.
