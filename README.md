# **Projeto de Desenvolvimento - Dados demográficos dos municípios brasileiros (BrStats)**

Para o trabalho prático da disciplina de Introdução à Ciência dos Dados será desenvolvido um processamento dos dados demográficos dos municípios brasileiros (BrStats), além disso, os dados serão analisados em relação aos temas **Economia**, **Agropecuária** e situações de **Crise** envolvendo o Brasil. A base de dados foi fornecida pelo professor, com algumas adições retiradas da fonte utilizada no levantamento do BrStats, o [Sidra - Sistema IBGE de Recuperação Automática](https://sidra.ibge.gov.br/pesquisa/censo-demografico/series-temporais/series-temporais/) e do [Finbra - Finanças do Brasil](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjUifHUwNmNAxU0s5UCHXsLD1UQFnoECBkQAQ&url=https%3A%2F%2Fsiconfi.tesouro.gov.br%2Fsiconfi%2Fpages%2Fpublic%2Fconteudo%2Fconteudo.jsf%3Fid%3D20303&usg=AOvVaw1FzxDElDFlYavY0tFIKZCN&opi=89978449).

É importante citar, para um melhor entendimento do trabalho, a maneira como os notebooks estão estruturados, optamos por dividir cada tema em um notebook. De maneira a auxiliar o leitor em sua navegação, colocaremos o notebook utilizado em cada seção.


### Integrantes

Ana Carolina Fernandes - 5094

João Roberto Melo dos Santos - 3883

Dalmo Nolasco Dantas Rainer - 5361

Guilherme Guimarães Pianetti - 5360

Renan Grassi - 3987

## **Dataset**

Dados demográficos dos municípios brasileiros (BrStats)

O dataset utilizado é um conjunto de dados unificados que reúne informações socioeconômicas de todos os municípios brasileiros. Ele integra dados de diversas áreas, como população, economia, emprego, educação e saúde, jo qual serão feitas análises nas três principais vertentes: Economia, Agropecuária e Crises.

### **Características principais:**
**Abrangência:** Dados de 5.570 municípios brasileiros, cobrindo o período de 2016 a 2021.

**Variáveis:** Inclui 21 colunas com informações como população, PIB, número de empresas, produção agrícola e pecuária, salários, importações/exportações, receitas municipais e indicadores de saúde (nascimento e óbitos infantis).

**Fontes:** Dados extraídos de APIs públicas (IBGE e IPEA).

## **Tarefas**

[🔵 QUESTÕES A SEREM VALIDADAS](https://github.com/anaC-Fernandes/ProjetoDados#-questões-a-serem-validadas)

[🔴 DEFINIÇÃO DO CONJUNTO DE DADOS](https://github.com/anaC-Fernandes/ProjetoDados#-definição-do-conjunto-de-dados)

[🟡 ORGANIZAÇÃO DAS ENTREGAS](https://github.com/anaC-Fernandes/ProjetoDados#-organizacao-das-entregas)

## **🔵 QUESTÕES A SEREM VALIDADAS**

Ao selecionar as questões que utilizaríamos como base para nosso projeto optamos por separá-las em tópicos específicos, de maneira que direcionariamos o projeto para os temas **Economia**, **Agropecuária** e **Crise**. Os temas foram decididos em uma reunião na qual cada integrante do grupo levou algumas perguntas, e decidimos que a melhor abordagem seria a divisão em temas, selecionando as melhores perguntas que se encaixavam em cada um. 

É importante citar que, inicialmente, haviam 10 questões, porém a medida que se foi avançando no desenvolvimento do trabalho vimos a necessidade de remover ou remodelar algumas questões. Isso resultou na remoção de um notebook que havia sido utilizado anteriormente (Dataset-covid), mas que pode ser encontrado a partir das tags criadas para as entregas anteriores.

Em seguida dividimos os temas entre os integrantes conforme mostrado abaixo:

- **📈 Economia**: Dalmo Nolasco Dantas Rainer - 5361 e Guilherme Guimarães Pianetti - 5360;
- **🌱 Agropecuária**: Renan Grassi - 3987;
- **📉 Crise**: Ana Carolina Fernandes - 5094 e João Roberto Melo dos Santos - 3883.

### **📈 Economia**
1. Existe uma correlação entre a quantidade de empresas (QtEmpresas) e indicadores sociais (População, NrNascimento, NrObitosInfantis)?
2. Existe alguma relação entre o Produto Interno Bruto (PIB) e a taxa de exportação (Exportacoes_US$) dos municípios?
3. Os municípios que recebem mais receita proveniente do governo federal brasileiro são capazes de utilizar e investir esse recurso em desenvolvimento social e econômico (PessoalOcupado, PessoalAssalariado, PIB, Receitas_R$)?
4. As transferências correntes (Transferencias_correntes_R$) e as transferências capitais (Transferencias_capital_R$) tem influencia nas Receitas (Receitas_R$) dos municípios?

### **🌱 Agropecuária**
5.  Como está distribuída a produção agrícola entre os 10 maiores produtores agricolas do Dataset?
6.  Estabelecendo uma relação entre Pessoal Ocupado e Produção Agrícola?

### **📉 Crise**

9. A partir da análise do PIB, quais regiões se recuperaram da recessão de 2014-2016? 

## **🔴 DEFINIÇÃO DO CONJUNTO DE DADOS**

### **📈 Economia**

### **📚Notebook**: [Dataset_Economia](https://github.com/anaC-Fernandes/ProjetoDados/blob/c984c0f9a998e76d35b183980d1b8cc1c00f251c/Notebooks/Dataset_Economia.ipynb)

#### **3. Os municípios que recebem mais receita proveniente do governo federal brasileiro são capazes de utilizar e investir esse recurso em desenvolvimento social e econômico (PessoalOcupado, PessoalAssalariado, PIB, Receitas_R$)?**

O principal objetivo desta pergunta é avaliar se os municípios que recebem grandes quantias de dinheiro, provenientes do governo, conseguem aplicá-lo de maneira eficaz em benefício da população. Para isso, utilizaremos bases de dados, como o Portal da Transparência, para coletar e analisar informações sobre os repasses. Esses dados serão incorporados às nossas tabelas como novas colunas, enriquecendo a pesquisa e tornando-a mais precisa e fundamentada.

  - [Portal da Transparência](https://portaldatransparencia.gov.br/transferencias/consulta?ordenarPor=mesAno&direcao=desc)

### **🌱 Agropecuária**

### **📚 Notebook**: [Dataset_Agro](https://github.com/anaC-Fernandes/ProjetoDados/blob/c984c0f9a998e76d35b183980d1b8cc1c00f251c/Notebooks/Dataset_Agro.ipynb)

### **📉 Crise**

### **📚 Notebook**: [Dataset_Crise](https://github.com/anaC-Fernandes/ProjetoDados/blob/739fde131c64e203584947a9971e4e7f68be4dbf/Notebooks/Dataset_Crise.ipynb)

#### **9. A partir da análise do PIB, quais municípios se recuperaram da recessão de 2014-2016?**

Entre os anos de 2014 a 2016 o Brasil passou por uma recessão que resultou em uma queda considerável do PIB, a seguir apresentamos fontes consistentes
sobre a recessão:

  - [Recessão brasileira acabou no fim de 2016, diz comitê da FGV que estuda ciclos econômicos - G1](https://g1.globo.com/economia/noticia/recessao-brasileira-acabou-no-fim-de-2016-diz-comite-da-fgv-que-estuda-ciclos-economicos.ghtml)
  - [Década cada vez mais perdida na economia brasileira e comparações internacionais - FGV](https://portal.fgv.br/artigos/decada-cada-vez-mais-perdida-economia-brasileira-e-comparacoes-internacionais)
  - [Como o Brasil entrou, sozinho, na pior crise da história - Epoca](https://epoca.globo.com/ideias/noticia/2016/04/como-o-brasil-entrou-sozinho-na-pior-crise-da-historia.html)

  Entretanto, os dados disponíveis no dataset BrStats não seriam o suficiente para fazer a análise que essa pergunta propõe, uma vez que o PIB de cada município está registrado apenas a partir do ano de 
  2016, e a recessão começou em 2014 e terminou em 2016, por esse motivo houve a necessidade de incluir os dados dos anos anteriores.
  
  Para realizar essa busca utilizamos a mesma fonte apresentada no artigo "Dados demográficos dos municípios brasileiros (BrStats)", o [Sidra](https://sidra.ibge.gov.br/pesquisa/censo-demografico/series-temporais/series-temporais/). O Sidra é um banco de tabelas que armazena os dados de pesquisas realizadas pelo Instituto Brasileiro de Geografia e Estatística (IBGE), tais tabelas possuem diversos filtros que permitem acessar determinadas informações, como nomes dos municípios, UF e o PIB registrado de cada um deles. Essas informações nos levaram a uma [tabela](https://sidra.ibge.gov.br/tabela/5938#resultado) específica, que foi utilizada para enriquecer o dataset original.

## **🟡 ORGANIZAÇÃO DAS ENTREGAS**

Para uma melhor organização do repositório as etapas do projeto foram divididas em tags/releases no GitHub, para melhor orientar a visualização do que foi feito dispinibilizamos abaixo as entregas e suas respectivas tags e commits.

### **Entrega 1 - Entendimento inicial dos dados e preparação**
  - [Tag](https://github.com/anaC-Fernandes/ProjetoDados/releases/tag/entrega-etapa-1)
  - [Commit referente](https://github.com/anaC-Fernandes/ProjetoDados/tree/cedd5b68115c414878effa417b99a6bcd75ac9ce)

### **Entrega 2 - Análise exploratória dos dados**
  - [Tag](https://github.com/anaC-Fernandes/ProjetoDados/releases/tag/entrega-etapa-2)
  - [Commit referente](https://github.com/anaC-Fernandes/ProjetoDados/tree/9b8815eb7151d9e490fa1071e05789e770b47eca)

### **Entrega 3 - Inferência Estatística e Regras de Associação**
  - [Tag](https://github.com/anaC-Fernandes/ProjetoDados/releases/tag/entrega-etapa-3)
  - [Commit referente](https://github.com/anaC-Fernandes/ProjetoDados/tree/444ffded54695389c0ccc438982deb98cd579ff1)

### **Entrega 4 - Regressão**
  - [Tag](https://github.com/anaC-Fernandes/ProjetoDados/releases/tag/entrega-etapa-4)
  - [Commit referente](https://github.com/anaC-Fernandes/ProjetoDados/tree/a614a9a7a604526e952140b32aca6d1346cf33e0)

  É importante ressaltar que nesta etapa o Analise-Covid foi descontinuado, a decisão foi tomada ao encontrar dificuldade em fazer a regressão relacionada ao tema. Por esse motivo o integrante responsável pela pergunta do Analise-Covid trabalhou no Dataset_Crise nesta entrega.

### **Entrega 5 - Aprendizado Supervisionado e Não-Supervisionado**
  - [Tag](https://github.com/anaC-Fernandes/ProjetoDados/releases/tag/entrega-etapa-4)
  - [Commit referente](https://github.com/anaC-Fernandes/ProjetoDados/tree/a614a9a7a604526e952140b32aca6d1346cf33e0)

