# challenge-jsm

# Objetivo
O objetivo desse case é criar um desenho de solução, com passo a passo para orientar um engenheiro de dados desenvolver uma solução de dados real time para a squad de pedidos. 
O resultado desse desenho deverá orientar as pessoas de dados e da squad com a solução. Esses documentos servirão como insumo para iniciar o desenvolvimento.
A squad de produtos hoje conta com um(a) PM e pessoas de engenharia de software. 
Esse time fará parte da solução, criando o transacional da nossa solução de dados, portanto é necessário desenharmos a solução que contemple eles. 
Aqui é necessário sugerir uma arquitetura e ferramentas para a Squad, contextualizando tecnicamente e funcionalmente o time. 
A stack do lado de dados conta com um Databricks na Azure, mas ainda não tem uma solução para dados real time.

Os dados que receberemos estão nesse modelo (https://www.kaggle.com/datasets/gabrielramos87/an-online-shop-business)
É necessário também desenvolver um trecho de código para servir de exemplo para os engenheiros de software e de dados. 
Aqui, deixamos a sua escolha qual parte do código deseja construir para servir de exemplo. Podemos utilizar, Python, Pyspark, Sql e/ou Scala. 
Precisamos também explicar os motivadores para a escolha de tecnologia.
Para documentar essa solução utilize uma ferramenta como Draw.io, Miro ou excalidraw e para o código, utilize o github.

## Arquitetura Sugerida
Para realizar a captura de dados real, precisamos levar como principais premissas:
- Alta escalabilidade;
- Baixa latência.
Pensando nessas principais premissas, podemos utilizar uma arquitetura baseada em eventos.
Utilizando os recursos da Azure, integrando times como o de engenharia de software para o
desenvolvimento do transacional e de uma solução escalável e segura.

## Componentes da Arquitetura
Foi sugerido no desenho disponível na pasta: system_design, 

1) API e microserviços: o desenvolvimento de uma API e microserviços para 
capturar os eventos de pedidos (CRUD) e enviar para a ferramenta Azure Event Hub.

2) Azure Event Hub: será utilizado para fazer a captação de eventos dos pedidos em tempo real.

3) Azure Databricks: utilizar o recurso já disponível para processar/transformar os dados em tempo real.

4) Delta Lake: ferramenta que será usada para armazenar os dados já processados, será responsável por 
manter o histórico dos pedidos e pode oferecer suporte à futuras consultas analíticas em tempo real.

5) Azure Monitor: ferramenta utilizada para monitorar e alertar erros nos processos envolvidos no fluxo.

## Entendendo a Utilização das Ferramentas
1) API e microserviços: nível de conhecimento e maturidade do time de engenharia de software.
2) Azure Event Hub: capacidade de escalabilidade e transmissão de grande volume de dados.
3) Azure Databricks: capacidade de utilizar a ferramenta com Apache Spark, para processar quantidades massivas de dados 
em tempo real e com baixa latência. Além da utilização do pySpark que facilita o desenvolvimento de código utilizando
a linguagem Python.
4) Delta Lake: mantém a qualidade dos dados através das transações ACID (manipulação dos dados estruturados em larga escala), 
além de ser altamente escalável no armazenamento de dados de grandes volumes e permitir consultas de baixa latência.

## Conclusão
Além de garantir a captura de eventos e disponibilidade de dados, ainda sim é possível utilizar a estrutura para evolução
de projetos de para dados analíticos, já que as ferramentas suportam e integram com outras soluções de análises da oferecidas
pela Azure.



