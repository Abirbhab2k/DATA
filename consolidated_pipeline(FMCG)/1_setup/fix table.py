# Databricks notebook source
spark.sql("""
DELETE FROM fmcg.bronze.orders
WHERE order_placement_date = 'Wednesday, December 31, 2025'
""")