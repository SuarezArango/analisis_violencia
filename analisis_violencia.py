from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, desc

# 1. Crear la sesión de Spark para Batch
spark = SparkSession.builder \
    .appName("AnalisisViolenciaIntrafamiliarBatch") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# 2. Cargar el dataset que subimos a la máquina virtual
file_path = "Reporte_Delito_Violencia_Intrafamiliar_Polic_a_Nacional.csv"

df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("delimiter", ",") \
    .csv(file_path)

print("--- Esquema del Dataset cargado ---")
df.printSchema()

print(f"Total de registros procesados: {df.count()}")

# 3. Análisis de ejemplo: Conteo por Departamento o zona (ajusta el nombre de la columna si es necesario)
print("--- Top registros agrupados ---")
# Nota: Imprimimos las primeras columnas o realizamos un agrupamiento seguro
df.groupBy(df.columns[0]) \
    .agg(count("*").alias("total_casos")) \
    .orderBy(desc("total_casos")) \
    .limit(10) \
    .show(truncate=False)

# 4. Análisis adicional por Género
print("--- Conteo de casos por Género ---")
df.groupBy("GENERO") \
    .agg(count("*").alias("total_casos")) \
    .orderBy(desc("total_casos")) \
    .show(truncate=False)

# 5. Análisis adicional por Armas o Medios utilizados
print("--- Top 5 Armas o Medios más frecuentes ---")
df.groupBy("ARMAS MEDIOS") \
    .agg(count("*").alias("total_casos")) \
    .orderBy(desc("total_casos")) \
    .limit(5) \
    .show(truncate=False)

# Detener la sesión de Spark
spark.stop()

