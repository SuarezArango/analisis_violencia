# Tarea 3 - Procesamiento de Datos Masivos (Batch y Streaming)

Este repositorio contiene la implementación práctica para la Tarea 3, enfocada en arquitecturas Big Data con Apache Spark y Apache Kafka sobre un entorno de clúster Hadoop.

## 🛠️ Tecnologías Utilizadas
* **Apache Spark / PySpark** (Batch Processing & Structured Streaming)
* **Apache Kafka** (Procesamiento y flujo de eventos en tiempo real)
* **Hadoop / HDFS** (Infraestructura de clúster)
* **Python 3**

## 📁 Estructura del Repositorio
* `analisis_violencia.py`: Script de procesamiento en lote (*batch*) con PySpark para el análisis exploratorio del dataset "Reporte de Delito Violencia Intrafamiliar - Policía Nacional" (~477k registros).
* `kafka_producer.py`: Productor en Python que simula el envío de mensajes/eventos hacia un tópico de Kafka.
* `spark_streaming_consumer.py`: Consumidor en PySpark Structured Streaming para el procesamiento y agregación de datos en tiempo real recibidos desde Kafka.

## 🚀 Ejecución de los Scripts
1. **Análisis Batch:**
   ```bash
   python3 analisis_violencia.py
