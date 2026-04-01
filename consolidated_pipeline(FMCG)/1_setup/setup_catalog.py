# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE  CATALOG IF NOT EXISTS fmcg;
# MAGIC USE CATALOG fmcg;

# COMMAND ----------

# MAGIC  %sql
# MAGIC  CREATE SCHEMA IF NOT EXISTS fmcg.gold;
# MAGIC  CREATE SCHEMA IF NOT EXISTS fmcg.silver;
# MAGIC  CREATE SCHEMA IF NOT EXISTS fmcg.bronze;
# MAGIC
# MAGIC --Create a view to access the data in the DataFrame
# MAGIC --This is a temporary view that will be dropped when the session ends
# MAGIC --This is a global temporary view that will

# COMMAND ----------

