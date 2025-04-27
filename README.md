# **Projeto de Desenvolvimento - Dados demográficos dos municípios brasileiros (BrStats)**

Para o trabalho prático da disciplina de Introdução à Ciência dos Dados será desenvolvido um processamento dos dados demográficos dos municípios brasileiros (BrStats), além disso, os dados serão analisados em relação aos temas **Economia**, **Agropecuária** e situações de **Crise** envolvendo o Brasil. A base de dados foi fornecida pelo professor, com algumas adições retiradas da fonte utilizada no levantamento do BrStats, o [Sidra - Sistema IBGE de Recuperação Automática](https://sidra.ibge.gov.br/pesquisa/censo-demografico/series-temporais/series-temporais/).

É importante citar, para um melhor entendimento do trabalho, a maneira como os notebooks estão estruturados, optamos por dividir cada tema em um notebook, com exceção do tema **Crise**, onde existem dois notebooks, um para a questão 9 e outro para a 10. De maneira a auxiliar o leitor em sua navegação, colocaremos o notebook utilizado em cada seção.


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

## **🔵 QUESTÕES A SEREM VALIDADAS**

Ao selecionar as questões que utilizaríamos como base para nosso projeto optamos por separá-las em tópicos específicos, de maneira que direcionariamos o projeto para os temas **Economia**, **Agropecuária** e **Crise**. Os temas foram decididos em uma reunião na qual cada integrante do grupo levou algumas perguntas, e decidimos que a melhor abordagem seria a divisão em temas, selecionando as melhores perguntas que se encaixavam em cada um. 

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
5. Existe uma correlação entre a área plantada e a área colhida?
6. Municípios mais densamente povoados tendem a ter menor área agrícola?
7. A produção agrícola gera mais empregos nos municípios?
8. Municípios com maior produção agropecuária têm maior PIB?
### **📉 Crise**

9. A partir da análise do PIB, quais municípios se recuperaram da recessão de 2014-2016? 
10. Como os indicadores socias e econômicos foram afetados durante a pandemia?

## **🔴 DEFINIÇÃO DO CONJUNTO DE DADOS**

### **📈 Economia**

### **📚Notebook**: [Dataset_Economia](https://github.com/anaC-Fernandes/ProjetoDados/blob/292a5f31c338f9156d05305fa3d1e98a96b6ae9a/Notebooks/Dataset_Economia.ipynb)

#### **3. Os municípios que recebem mais receita proveniente do governo federal brasileiro são capazes de utilizar e investir esse recurso em desenvolvimento social e econômico (PessoalOcupado, PessoalAssalariado, PIB, Receitas_R$)?**

O principal objetivo desta pergunta é avaliar se os municípios que recebem grandes quantias de dinheiro, provenientes do governo, conseguem aplicá-lo de maneira eficaz em benefício da população. Para isso, utilizaremos bases de dados, como o Portal da Transparência, para coletar e analisar informações sobre os repasses. Esses dados serão incorporados às nossas tabelas como novas colunas, enriquecendo a pesquisa e tornando-a mais precisa e fundamentada.

  - [Portal da Transparência](https://portaldatransparencia.gov.br/transferencias/consulta?ordenarPor=mesAno&direcao=desc)

### **🌱 Agropecuária**

### **📚 Notebook**: [Dataset_Agro](https://github.com/anaC-Fernandes/ProjetoDados/blob/292a5f31c338f9156d05305fa3d1e98a96b6ae9a/Notebooks/Dataset_Agro.ipynb)

### **📉 Crise**

### **📚 Notebook Questão 9**: [Dataset_Crise](https://github.com/anaC-Fernandes/ProjetoDados/blob/292a5f31c338f9156d05305fa3d1e98a96b6ae9a/Notebooks/Dataset_Crise.ipynb)
### **📚 Notebook Questão 10**: [Dataset_Covid](https://github.com/anaC-Fernandes/ProjetoDados/blob/292a5f31c338f9156d05305fa3d1e98a96b6ae9a/Notebooks/Analise-Covid.ipynb)

#### **9. A partir da análise do PIB, quais municípios se recuperaram da recessão de 2014-2016?**

Entre os anos de 2014 a 2016 o Brasil passou por uma recessão que resultou em uma queda considerável do PIB, a seguir apresentamos fontes consistentes
sobre a recessão:

  - [Recessão brasileira acabou no fim de 2016, diz comitê da FGV que estuda ciclos econômicos - G1](https://g1.globo.com/economia/noticia/recessao-brasileira-acabou-no-fim-de-2016-diz-comite-da-fgv-que-estuda-ciclos-economicos.ghtml)
  - [Década cada vez mais perdida na economia brasileira e comparações internacionais - FGV](https://portal.fgv.br/artigos/decada-cada-vez-mais-perdida-economia-brasileira-e-comparacoes-internacionais)
  - [Como o Brasil entrou, sozinho, na pior crise da história - Epoca](https://epoca.globo.com/ideias/noticia/2016/04/como-o-brasil-entrou-sozinho-na-pior-crise-da-historia.html)

  Entretanto, os dados disponíveis no dataset BrStats não seriam o suficiente para fazer a análise que essa pergunta propõe, uma vez que o PIB de cada município está registrado apenas a partir do ano de 
  2016, e a recessão começou em 2014 e terminou em 2016, por esse motivo houve a necessidade de incluir os dados dos anos anteriores.
  
  Para realizar essa busca utilizamos a mesma fonte apresentada no artigo "Dados demográficos dos municípios brasileiros (BrStats)", o [Sidra](https://sidra.ibge.gov.br/pesquisa/censo-demografico/series-temporais/series-temporais/). O Sidra é um banco de tabelas que armazena os dados de pesquisas realizadas pelo Instituto Brasileiro de Geografia e Estatística (IBGE), tais tabelas possuem diversos filtros que permitem acessar determinadas informações, como nomes dos municípios, UF e o PIB registrado de cada um deles. Essas informações nos levaram a uma [tabela](https://sidra.ibge.gov.br/tabela/5938#resultado) específica, que foi utilizada para enriquecer o dataset original.

#### **10. Como a taxa de desemprego e o PIB foram afetadas durante a pandemia**

Em 11 de março de 2020, a Organização Mundial da Saúde (OMS) caracterizou a Covid-19 como uma pandemia, essa informação foi retirada do site da CNN Brasil, 5 anos após o fim da pandemia, em uma notícia publicada em 31 de dezembro de 2024, disponível abaixo:

- [5 anos da Covid-19: lembre o histórico desde 1º caso até fim da emergência](https://www.cnnbrasil.com.br/saude/5-anos-da-covid-19-relembre-o-historico-desde-1o-caso-ate-fim-da-emergencia/)

A pandemia da Covid-19 foi uma tragédia mundial, que marcou não só as vidas dos brasileiros como também a economia do Brasil, o comércio e trabalho tiveram que ser adaptados pela nova realidade imposta, e cinco anos depois ainda sofremos com os impactos causados pela doença que parou o planeta como um todo. 

Por esse motivo, decidimos utilizar o Dataset BrStats, que conta com dados relacionados e economia e qualidade de vida, para fazer uma análise do quanto a pandemia do Covid-19 afetou os indicadores sociais e econômicos disponíveis no Dataset durante o seu período de ocorrência.
