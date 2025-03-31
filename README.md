Projeto de Desenvolvimento - Dados demográficos dos municípios brasileiros (BrStats)

Para o trabalho prático da disciplina de Introdução à Ciência dos Dados será desenvolvido um processamento dos dados demográficos dos municípios brasileiros (BrStats), além disso, os dados serão analisados em relação aos temas Economia, Agropecuária e situações de Crise envolvendo o Brasil. A base de dados foi fornecida pelo professor, com algumas adições retiradas da fonte utilizada no levantamento do BrStats, o Sidra - Sistema IBGE de Recuperação Automática.
Integrantes

Ana Carolina Fernandes - 5094

João Roberto Melo dos Santos - 3883

Dalmo Nolasco Dantas Rainer - 5361

Guilherme Guimarães Pianetti - 5360

Renan Grassi - 3987
Dataset

Dados demográficos dos municípios brasileiros (BrStats)
Tarefas

🔵 QUESTÕES A SEREM VALIDADAS

🔴 DEFINIÇÃO DO CONJUNTO DE DADOS
🔵 QUESTÕES A SEREM VALIDADAS

Ao selecionar as questões que utilizaríamos como base para nosso projeto optamos por separá-las em tópicos específicos, de maneira que direcionariamos o projeto para os temas Economia, Agropecuária e Crise. Os temas foram decididos em uma reunião na qual cada integrante do grupo levou algumas perguntas, e decidimos que a melhor abordagem seria a divisão em temas, selecionando as melhores perguntas que se encaixavam em cada um.

Em seguida dividimos os temas entre os integrantes conforme mostrado abaixo:

    📈 Economia: Dalmo Nolasco Dantas Rainer - 5361 e Guilherme Guimarães Pianetti - 5360;
    🌱 Agropecuária: Renan Grassi - 3987;
    📉 Crise: Ana Carolina Fernandes - 5094 e João Roberto Melo dos Santo - 3883.

📈 Economia

    Existe uma correlação entre a quantidade de empresas (QtEmpresas) e indicadores sociais (População, NrNascimento, NrObitosInfantis)?
    Existe alguma relação entre o Produto Interno Bruto (PIB) e a taxa de exportação (Exportacoes_US$) dos municípios?
    Os municípios que recebem mais receita proveniente do governo federal brasileiro são capazes de utilizar e investir esse recurso em desenvolvimento social e econômico (PessoalOcupado, PessoalAssalariado, PIB, Receitas_R$)?
    As transferências correntes (Transferencias_correntes_R$) e as transferências capitais (Transferencias_capital_R$) tem grande influencia nas Receitas (Receitas_R$) dos municípios? Se sim, a taxa da receita (Receitas_R$) que é utilizada com esses recursos é alta ou baixa?

🌱 Agropecuária

    Quais os efeitos da discrepância entre a área plantada e colhida? Há relações de deficit aparentes, neutro(ou balança 0) e aparente superavit que devemos estudar para as proximas etapas do projeto.
    Há relação entre povoamento e área plantada? Aparentemente sim!, quanto mais densamente povoado o local, menor sua produção agricola, sedo deixada para o interior.
    Mecanização da produção agrícola afeta a empregabilidade? Dados ainda precisam ser melhor trabalhados, estão muito confusos.
    Há uma relação entre o valor da produção agrícola e pecuária? Assim como a questão anterior ainda precisamos organizar melhor estes dados...

📉 Crise

    A partir da análise do PIB, quais municípios se recuperaram da recessão de 2014-2016?
    Como os indicadores socias e econômicos foram afetados durante a pandemia?

🔴 DEFINIÇÃO DO CONJUNTO DE DADOS
📉 Crise
9. A partir da análise do PIB, quais municípios se recuperaram da recessão de 2014-2016?

Entre os anos de 2014 a 2016 o Brasil passou por uma recessão que resultou em uma queda considerável do PIB, a seguir apresentamos fontes consistentes sobre a recessão:

    Recessão brasileira acabou no fim de 2016, diz comitê da FGV que estuda ciclos econômicos - G1
    Década cada vez mais perdida na economia brasileira e comparações internacionais - FGV
    Como o Brasil entrou, sozinho, na pior crise da história - Epoca

Entretanto, os dados disponíveis no dataset BrStats não seriam o suficiente para fazer a análise que essa pergunta propõe, uma vez que o PIB de cada município está registrado apenas a partir do ano de 2016, e a recessão começou em 2014 e terminou em 2016, por esse motivo houve a necessidade de incluir os dados dos anos anteriores.

Para realizar essa busca utilizamos a mesma fonte apresentada no artigo "Dados demográficos dos municípios brasileiros (BrStats)", o Sidra. O Sidra é um banco de tabelas que armazena os dados de pesquisas realizadas pelo Instituto Brasileiro de Geografia e Estatística (IBGE), tais tabelas possuem diversos filtros que permitem acessar determinadas informações, como nomes dos municípios, UF e o PIB registrado de cada um deles. Essas informações nos levaram a uma tabela específica, que foi utilizada para enriquecer o dataset original.
10. Como a taxa de desemprego e o PIB foram afetadas durante a pandemia

Em 11 de março de 2020, a Organização Mundial da Saúde (OMS) caracterizou a Covid-19 como uma pandemia, essa informação foi retirada do site da CNN Brasil, 5 anos após o fim da pandemia, em uma notícia publicada em 31 de dezembro de 2024, disponível abaixo:

    5 anos da Covid-19: lembre o histórico desde 1º caso até fim da emergência

A pandemia da Covid-19 foi uma tragédia mundial, que marcou não só as vidas dos brasileiros como também a economia do Brasil, o comércio e trabalho tiveram que ser adaptados pela nova realidade imposta, e cinco anos depois ainda sofremos com os impactos causados pela doença que parou o planeta como um todo.

Por esse motivo, decidimos utilizar o Dataset BrStats, que conta com dados relacionados e economia e qualidade de vida, para fazer uma análise do quanto a pandemia do Covid-19 afetou os indicadores sociais e econômicos disponíveis no Dataset durante o seu período de ocorrência.
