# Databricks notebook source
dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets/')

display(files)

# COMMAND ----------


