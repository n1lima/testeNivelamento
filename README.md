# Teste de Nivelamento - Estágio

Este repositório contém a solução para o teste de nivelamento para estágio, com foco em **Web Scraping** e outras tarefas relacionadas ao processamento de dados e desenvolvimento de APIs. A solução foi desenvolvida utilizando **Python**, com o objetivo de aplicar e aprender novas bibliotecas e técnicas.

## Objetivo do Teste

O teste de nivelamento foi projetado para avaliar habilidades em diversas áreas, sendo:

1. **Web Scraping**: Acesso a site, download de arquivos em formato PDF e compactação.
2. **Transformação de Dados**: Extração de dados de um PDF e conversão para um formato estruturado (CSV).
3. **Banco de Dados**: Manipulação de dados utilizando SQL, incluindo a criação de queries e importação de dados.
4. **API e Web Interface**: Desenvolvimento de uma interface web que interage com um servidor Python.

## Descrição das Etapas Realizadas

### 1. Web Scraping

**Objetivo**: Acessar a página da ANS, fazer o download dos Anexos I e II em formato PDF e compactá-los em um arquivo ZIP.

**Tarefas Realizadas**:
- Utilização da biblioteca `requests` para fazer a requisição e obter o conteúdo da página.
- Uso de `BeautifulSoup` para realizar o parsing do HTML e localizar os links dos arquivos PDF.
- Implementação de lógica para verificar e baixar apenas os PDFs desejados.
- Compactação dos arquivos baixados em um único arquivo ZIP utilizando a biblioteca `zipfile`.

**Resultado**:
- Os arquivos PDF desejados foram baixados com sucesso e compactados em um arquivo ZIP denominado `anexos.zip`.

**Código**: [webScraping.py](https://github.com/n1lima/testeNivelamento/blob/master/exercicio1/webScraping.py)

### 2. Transformação de Dados

**Objetivo**: Extrair os dados da tabela "Rol de Procedimentos e Eventos em Saúde" do PDF do Anexo I, salvar os dados em formato CSV e realizar a compactação do arquivo.

**Progresso**:
- Embora essa parte não tenha sido concluída dentro do prazo, dediquei um bom tempo para aprender sobre a extração de dados de PDFs, explorando bibliotecas como `PyPDF2` e `pdfplumber`. Essas bibliotecas são essenciais para processar o conteúdo do PDF de forma estruturada.
- O aprendizado continua e tenho o plano de completar esta tarefa em breve, aplicando as ferramentas adquiridas durante este processo.

### 3. Banco de Dados

**Objetivo**: Baixar os arquivos necessários e criar queries SQL para estruturar tabelas e importar dados de arquivos CSV.

**Progresso**:
- Não consegui avançar nessa parte ainda, principalmente devido à dependência da extração de dados do PDF. No entanto, estou planejando seguir com as queries de importação de dados assim que a extração for concluída. Isso inclui aprendizado contínuo em SQL para melhorar a estruturação e importação.

### 4. API e Web Interface

**Objetivo**: Desenvolver uma interface web utilizando Vue.js que interage com um servidor Python, realizando buscas nos cadastros de operadoras de planos de saúde.

**Progresso**:
- Esta parte envolve o aprendizado de novas ferramentas e ainda não foi possível completá-la no tempo disponível. 

## Considerações Finais

Este teste foi uma excelente oportunidade para aprender novas bibliotecas e ferramentas, como o **BeautifulSoup**, **requests**, **zipfile**, entre outras relacionadas ao processamento de dados. Embora não tenha sido possível concluir todas as tarefas dentro do prazo estipulado, me empenhei bastante em cada etapa, buscando aprender e aplicar novas ferramentas ao longo do caminho. O aprendizado é contínuo, e estou dedicado a finalizar as tarefas restantes assim que possível.

Agradeço pela oportunidade de participar deste processo seletivo e estou à disposição para mais esclarecimentos.
