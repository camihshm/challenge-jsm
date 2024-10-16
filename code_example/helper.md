# Resumo
A sugestão proposta no desenho utiliza as ferramentas Azure Event Hub e Azure Databricks. Logo,
utilizaremos a integração do Azure Event Hub com o Spark Structured Streaming no Azure
Databricks, para consumir e fazer a leitura dos eventos em tempo real.

Utilizaremos a biblioteca nativa para a utilização do Spark no Databricks.

# Dependências
Antes de iniciar, é necessário garantir a instalação da biblioteca do Azure Event Hub para Spark 
no Databricks. Para isso, siga o passo abaixo:

1) Na seção "Biblioteca" ou "Libraries" do Databricks adicione o pacote: Maven.

> *com.microsoft.azure:azure-eventhubs-spark_2.12:2.3.18*

Além disso, é necessário à configuração da conexão com Event Hub, os parâmetros são:
- Event Hub Connection String.
- Event Hub Name.
- Consumer Group.

---

Explicação do Passo a Passo Executado pelo Código.

1) Conexão do Event Hub:
- O código utilizará os parâmetros: connectionString e eventHubName, para configurar a conexão.
- A configuração é passada para o Spark Structured Streaming, para fazer a leitura
contínua dos eventos.

2) Leitura dos Eventos:
- A função: spark.readStream.format("eventhubs"), faz a leitura dos eventos do Event Hub em tempo real e retorna um dataframe.

3) Definindo o Schema:
- Definimos um schema específico para os dados que chegam no Event Hub.

4) Capturando os Dados JSON:
- Dentro da coluna "body", é aonde estão os dados dos eventos em formato binário,
e então é convertido para string para ser transfor o JSON em um dataframe estruturado, com base do schema definido no passo 3.

5) Escreve no Console:
- Esse trecho permitirá que você escreva os dados no console, para fins de testes, mas deve ser adaptado para fazer a escrita/gravação no delta lake.





