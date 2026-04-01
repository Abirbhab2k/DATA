
# FMCG Sales Analytics Dashboard

## 📊 Project Overview
An end-to-end **Sales Analytics Solution** built on **Databricks Lakeview** for analyzing FMCG (Fast-Moving Consumer Goods) business performance. This project demonstrates enterprise-grade data engineering practices including incremental data loading, dimensional modeling, and interactive business intelligence dashboards.

## 🎯 Business Objectives
- Track real-time sales performance across multiple channels and markets
- Analyze product profitability and revenue trends
- Monitor customer acquisition patterns by distribution channels
- Enable self-service analytics for business stakeholders
- Support data-driven decision making with KPI tracking

## ✨ Key Features
- **Incremental Data Pipeline**: Efficient ETL using Delta Lake's COPY INTO with schema enforcement
- **Dimensional Data Model**: Star schema with enriched fact and dimension tables
- **Interactive Dashboard**: 10+ dynamic visualizations with multi-dimensional filtering
- **Unity Catalog Integration**: Governed data access with catalog.schema.table structure
- **Real-time Insights**: Serverless compute for on-demand analytics
- **Self-Service BI**: Parameterized filters for year, quarter, month, and channel

## 🏗️ Architecture

### Data Layer Structure
```
fmcg (catalog)
├── gold (schema)
│   ├── fact_orders (managed table)
│   ├── dim_customer (dimension table)
│   ├── dim_product (dimension table)
│   ├── dim_date (dimension table)
│   └── vw_fact_orders_enriched (enriched view)
└── volumes
    └── parent_incrimental_update (volume for raw files)
```

### Data Flow
1. **Ingestion**: CSV files uploaded to Unity Catalog Volumes
2. **Loading**: COPY INTO statements with type casting for schema alignment
3. **Transformation**: Dimensional modeling with star schema design
4. **Enrichment**: Fact table joined with dimensions in view layer
5. **Visualization**: Lakeview dashboard consuming enriched views

## 🛠️ Technologies Used
- **Platform**: Databricks Lakehouse Platform
- **Storage**: Delta Lake (ACID transactions, time travel)
- **Catalog**: Unity Catalog (data governance)
- **Compute**: Serverless SQL Warehouses
- **Visualization**: Databricks Lakeview
- **Language**: SQL
- **Data Format**: CSV → Delta Tables

## 📐 Data Model

### Fact Table
- `fact_orders`: Transactional sales data
  - Grain: One row per product-customer-date combination
  - Key metrics: sold_quantity, total_amount_inr
  - Dimensions: date, product_code, customer_code

### Dimension Tables
- `dim_customer`: Customer master with market and channel information
- `dim_product`: Product hierarchy (division → category → product → variant)
- `dim_date`: Date dimension with calendar attributes (year, quarter, month)

### Enriched View
- `vw_fact_orders_enriched`: Denormalized view joining fact with all dimensions

## 📈 Dashboard Components

### KPIs & Metrics
- Total Revenue (INR)
- Total Quantity Sold
- Number of Transactions
- Average Order Value

### Visualizations
1. **Top 10 Products by Revenue** (Horizontal Bar Chart)
   - Revenue comparison across best-performing products
   - Formatted with compact number notation (8.7B INR)

2. **Revenue by Channel** (Pie Chart)
   - Channel distribution: Retailer vs Direct
   - Percentage breakdown of sales channels

3. **Customer Acquisition by Channel** (Pie Chart)
   - Unique customer count by channel
   - Acquisition pattern analysis

4. **Additional Charts** (Customizable)
   - Trend analysis over time periods
   - Regional performance comparisons
   - Category-wise revenue breakdown

### Interactive Filters
- **Year Selection**: Multi-year comparison
- **Quarter**: Q1, Q2, Q3, Q4 filtering
- **Month**: Granular monthly analysis
- **Channel**: Retailer/Direct segmentation

## 🚀 Implementation Highlights

### Incremental Data Loading
```sql
COPY INTO fmcg.gold.fact_orders
FROM (
  SELECT 
    CAST(date AS DATE) AS date,
    product_code,
    CAST(customer_code AS BIGINT) AS customer_code,
    CAST(sold_quantity AS BIGINT) AS sold_quantity
  FROM '/Volumes/fmcg/gold/parent_incrimental_update/fact_orders.csv'
)
FILEFORMAT = CSV
FORMAT_OPTIONS ('header' = 'true');
```

**Key Technical Decisions:**
- Explicit type casting to match target schema (INT → BIGINT)
- Schema enforcement for data quality
- Idempotent loading with duplicate handling

### Error Resolution
- **DELTA_FAILED_TO_MERGE_FIELDS**: Resolved type mismatch between CSV (INT) and Delta table (BIGINT)
- Solution: Added explicit CAST operations in SELECT clause

## 📊 Sample Insights

### Top Revenue Products
1. PX Grip Cricket Batting Gloves: ₹8.7B
2. WL Hex Dumbbell: ₹8.2B
3. NX Pro Cricket Leg Guards: ₹7.0B

### Channel Performance
- Retailer: 28.2B INR (80% of revenue) - 14 customers
- Direct: 6.8B INR (20% of revenue) - 4 customers

## 🔮 Future Enhancements
- [ ] Real-time streaming ingestion using Auto Loader
- [ ] Predictive analytics with ML models
- [ ] Customer segmentation and RFM analysis
- [ ] Automated alerting for threshold breaches
- [ ] Mobile-responsive dashboard layouts
- [ ] Advanced time-series forecasting
- [ ] Integration with external BI tools (Power BI, Tableau)

## 📝 Setup Instructions

### Prerequisites
- Databricks workspace with Unity Catalog enabled
- SQL Warehouse or serverless compute access
- Unity Catalog volume for file storage

### Installation Steps
1. **Create Catalog Structure**
   ```sql
   CREATE CATALOG IF NOT EXISTS fmcg;
   CREATE SCHEMA IF NOT EXISTS fmcg.gold;
   ```

2. **Upload Data Files**
   - Place CSV files in Unity Catalog Volumes
   - Ensure proper file permissions

3. **Create Tables**
   - Execute DDL scripts for fact and dimension tables
   - Set up table properties and constraints

4. **Load Data**
   - Run COPY INTO statements for incremental loads
   - Validate data quality and row counts

5. **Create Enriched View**
   - Join fact with dimensions
   - Test query performance

6. **Build Dashboard**
   - Create Lakeview dashboard
   - Configure datasets and visualizations
   - Set up filters and parameters

## 💡 Lessons Learned
- Type alignment is critical for Delta Lake schema enforcement
- Dimensional modeling simplifies complex business queries
- Unity Catalog provides strong governance without performance overhead
- Lakeview offers powerful self-service BI capabilities
- Proper data modeling reduces dashboard query complexity



## 📄 License
This project is available for educational and portfolio purposes.

---

**⭐ If you find this project useful, please consider giving it a star!**
EOF

