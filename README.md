# Projeto de Desenvolvimento - Ciência de Dados

### Integrantes

Ana Carolina Fernandes - 5094

João Roberto Melo dos Santo - 3883

Dalmo Nolasco Dantas Rainer - 5361

Guilherme Guimarães Pianetti - 5360

Renan Grassi - 3987

### Dataset

Dados demográficos dos municípios brasileiros (BrStats)

# Perguntas a serem respondidas

## 🔴 Crise

1. A partir da análise do PIB, quais municípios se recuperaram da recessão de 2014-2016? 
2. Como os indicadores socias e econômicos foram afetados durante a pandemia?

# Preparação dos dados

## 🔴 Dados sobre a crise

### A partir da análise do PIB, quais municípios se recuperaram da recessão de 2014-2016?

  Entre os anos de 2014 a 2016 o Brasil passou por uma recessão que resultou em uma queda considerável do PIB, a seguir apresentamos fontes consistentes
sobre a recessão:

  - [Recessão brasileira acabou no fim de 2016, diz comitê da FGV que estuda ciclos econômicos - G1](https://g1.globo.com/economia/noticia/recessao-brasileira-acabou-no-fim-de-2016-diz-comite-da-fgv-que-estuda-ciclos-economicos.ghtml)
  - [Década cada vez mais perdida na economia brasileira e comparações internacionais - FGV](https://portal.fgv.br/artigos/decada-cada-vez-mais-perdida-economia-brasileira-e-comparacoes-internacionais)
  - [Como o Brasil entrou, sozinho, na pior crise da história - Epoca](https://epoca.globo.com/ideias/noticia/2016/04/como-o-brasil-entrou-sozinho-na-pior-crise-da-historia.html)

  Entretanto, os dados disponíveis no dataset BrStats não seriam o suficiente para fazer a análise que essa pergunta propõe, uma vez que o PIB de cada município está registrado apenas a partir do ano de 
  2016, e a recessão começou em 2014 e terminou em 2016, por esse motivo houve a necessidade de incluir os dados dos anos anteriores.

  Para realizar essa busca utilizamos a mesma fonte apresentada no artigo "Dados demográficos dos municípios brasileiros (BrStats)", o [Sidra](https://sidra.ibge.gov.br/pesquisa/censo-demografico/series-temporais/series-temporais/). O Sidra é um banco de tabelas que armazena os dados de pesquisas realizadas pelo Instituto Brasileiro de Geografia e Estatística (IBGE), tais tabelas possuem diversos filtros que permitem acessar determinadas informações, como nomes dos municípios, UF e o PIB registrado de cada um deles. Essas informações nos levaram a uma [tabela](https://sidra.ibge.gov.br/tabela/5938#resultado) específica, que foi utilizada para enriquecer o dataset original.
