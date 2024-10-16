from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StringType, StructType, StructField

# Create a session Spark
spark = SparkSession.builder.appName("EventHubStream").getOrCreate()

# Configuration Event Hub
connectionString = "Endpoint=sb://<NAMESPACE>.servicebus.windows.net/;SharedAccessKeyName=<SAS_KEY_NAME>;SharedAccessKey=<SAS_KEY>"
eventHubName = "<EVENT_HUB_NAME>"
ehConf = {
    'eventhubs.connectionString': connectionString,
    'eventhubs.eventHubName': eventHubName,
    'eventhubs.consumerGroup': '$Default',  # pode usar seu consumer group
}

# Read events from Event Hub
eventHubDF = (
    spark.readStream.format("eventhubs")
    .options(**ehConf)
    .load()
)

# Define the schema of the events being read.
schema = StructType([
    StructField("order_id", StringType(), True),
    StructField("customer_id", StringType(), True),
    StructField("product_id", StringType(), True),
    StructField("status", StringType(), True),
    StructField("timestamp", StringType(), True)
])

# Parse of data JSON
parsedDF = (
    eventHubDF
    .withColumn("body", col("body").cast("string"))
    .select(from_json(col("body"), schema).alias("data"))
    .select("data.*")
)

# Show result into console - only for testing
query = (
    parsedDF.writeStream
    .outputMode("append")
    .format("console")
    .start()
)

query.awaitTermination()
