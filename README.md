# Brazilian E-Commerce Data Challenge

This repository contains the solution to the **Brazilian E-Commerce Data Challenge** using the Brazilian E-Commerce Public Dataset by Olist. The project focuses on cleaning, analyzing, and visualizing e-commerce data to uncover insights into customer behavior, sales performance, and delivery metrics. The workflow includes data preparation, reconciliation of financial metrics, and the creation of an interactive monthly financial dashboard using Power BI.

---

## Project Structure

The repository is organized into numbered directories representing the sequence of steps in the project:

```
.
├── 0.DataSet
│   ├── DataSet.zip
│   ├── olist_customers_dataset.csv
│   ├── olist_geolocation_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_order_payments_dataset.csv
│   ├── olist_order_reviews_dataset.csv
│   ├── olist_orders_dataset.csv
│   ├── olist_products_dataset.csv
│   ├── olist_sellers_dataset.csv
│   └── product_category_name_translation.csv
├── 1.Data_Clean
│   ├── customers_dataset_clean.ipynb
│   ├── Data_Cleaned
│   │   ├── cleaned_olist_customers_dataset.csv
│   │   ├── cleaned_olist_geolocation_dataset.csv
│   │   ├── cleaned_olist_order_items_dataset.csv
│   │   ├── cleaned_olist_order_payments_dataset.csv
│   │   ├── cleaned_olist_order_reviews_dataset.csv
│   │   ├── cleaned_olist_orders_dataset.csv
│   │   ├── cleaned_product_category_name_translation.csv
│   │   ├── cleaned_products_dataset.csv
│   │   ├── cleaned_sellers_dataset.csv
│   │   └── merged_olist_dataset.csv
│   ├── geolocation_dataset_clean.ipynb
│   ├── main.ipynb
│   ├── Merging_Datasets_Cleaned.ipynb
│   ├── order_items_dataset_clean.ipynb
│   ├── order_payments_dataset_clean.ipynb
│   ├── order_reviews_dataset_clean.ipynb
│   ├── orders_dataset_clean.ipynb
│   ├── product_category_name_translation_clean.ipynb
│   ├── products_dataset_clean.ipynb
│   ├── Report.pdf
│   ├── sellers_clean.ipynb
│   └── temp
│       ├── clean.ipynb
│       └── clean.py
├── 2.Data_Analysis
│   ├── analysis.ipynb
│   ├── detailed_olist_data.csv
│   ├── monthly_olist_data.csv
│   └── Report.pdf
├── 3.visualization
│   ├── Report.pdf
│   ├── visualization.pbix
│   └── visualization.pdf
├── 4.Reports
│   ├── 1.Clean_Report.docx
│   ├── 1.Clean_Report.pdf
│   ├── 2.Analysis_Report.docx
│   ├── 2.Analysis_Report.pdf
│   ├── 3.visualization_Report.docx
│   └── 3.visualization_Report.pdf
├── Instructions
│   └── Google Data Analysis Tech challenge.pdf
├── README.md
└── requirements.txt
```

### Directory Breakdown
- **`0.DataSet`**: Contains the raw Olist datasets, available as individual CSV files or in `DataSet.zip`.
- **`1.Data_Clean`**: Includes notebooks for cleaning each dataset, a `Data_Cleaned` folder with cleaned CSV files, and a merged dataset (`merged_olist_dataset.csv`).
- **`2.Data_Analysis`**: Houses the analysis notebook, aggregated data files (`detailed_olist_data.csv` and `monthly_olist_data.csv`), and an analysis report.
- **`3.visualization`**: Contains the Power BI dashboard file (`visualization.pbix`), a static PDF version (`visualization.pdf`), and a report.
- **`4.Reports`**: Stores comprehensive reports for cleaning, analysis, and visualization in both DOCX and PDF formats.
- **`Instructions`**: Provides the challenge description.
- **`requirements.txt`**: Lists required Python libraries.

---

## Project Steps

### 1. Data Cleaning
Raw datasets from `0.DataSet` are cleaned to handle missing values, standardize formats, and remove duplicates. This step is managed in `1.Data_Clean`.

#### Cleaning Process
- **Datasets Cleaned**: Each dataset has a dedicated cleaning notebook:
  - `customers_dataset_clean.ipynb`
  - `geolocation_dataset_clean.ipynb`
  - `order_items_dataset_clean.ipynb`
  - `order_payments_dataset_clean.ipynb`
  - `order_reviews_dataset_clean.ipynb`
  - `orders_dataset_clean.ipynb`
  - `product_category_name_translation_clean.ipynb`
  - `products_dataset_clean.ipynb`
  - `sellers_clean.ipynb`
- **Merged Output**: Cleaned datasets are combined into `merged_olist_dataset.csv` using `Merging_Datasets_Cleaned.ipynb`.
- **Documentation**: See `Report.pdf` in `1.Data_Clean` for details.

### 2. Data Analysis
Analysis is performed in `2.Data_Analysis` using `analysis.ipynb`, focusing on sales reconciliation and monthly trends.

#### Analysis Steps
- **Data Preparation**: Load `merged_olist_dataset.csv` and verify its integrity.
- **Reconciliation Metrics**:
  - **Total Revenue**: Sum of payments from delivered orders.
  - **Expected Revenue**: Sum of payments from approved orders.
  - **Canceled Orders**: Count of canceled orders.
  - **Late Deliveries**: Count of orders delivered past the estimated date.
- **Monthly Aggregation**: Aggregate data by month for financial metrics, order status, and delivery performance.
- **Output Files**:
  - `monthly_olist_data.csv`: Monthly aggregated data.
  - `detailed_olist_data.csv`: Detailed dataset for further insights.
- **Documentation**: See `Report.pdf` in `2.Data_Analysis`.

### 3. Visualization
An interactive dashboard is built in Power BI using data from `2.Data_Analysis`. This step is detailed in `3.visualization`.

#### Visualization Components
- Financial summaries (revenue, payments).
- Order status breakdowns (delivered, canceled, pending).
- Delivery performance (late deliveries, delays).
- **Files**:
  - `visualization.pbix`: Power BI dashboard file.
  - `visualization.pdf`: Static dashboard snapshot.
  - `Report.pdf`: Visualization report.

### 4. Reporting
Final reports summarizing each phase are compiled in `4.Reports`.

- **Reports**:
  - `1.Clean_Report`: Cleaning process details (DOCX and PDF).
  - `2.Analysis_Report`: Analysis findings (DOCX and PDF).
  - `3.visualization_Report`: Visualization insights (DOCX and PDF).

---

## How to Get Started

Follow these steps to set up and explore the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/0PeterAdel/Brazilian-ECommerce.git
   cd Brazilian-ECommerce
   ```

2. **Install Dependencies**:
   Ensure Python 3.x is installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Data Cleaning**:
   - Navigate to `1.Data_Clean`.
   - Execute the cleaning notebooks (e.g., `customers_dataset_clean.ipynb`).
   - Merge datasets using `Merging_Datasets_Cleaned.ipynb`.

4. **Perform Analysis**:
   - Open `analysis.ipynb` in `2.Data_Analysis` and run all cells.

5. **Explore the Dashboard**:
   - Open `visualization.pbix` in `3.visualization` with Power BI Desktop to interact with the dashboard.
   - View `visualization.pdf` in `3.visualization` for a static version.
   - Refer to `3.visualization_Report.pdf` in `4.Reports` for details.

6. **Review Reports**:
   - Explore `4.Reports` for detailed documentation:
     - `1.Clean_Report.pdf`: Cleaning process.
     - `2.Analysis_Report.pdf`: Analysis findings.
     - `3.visualization_Report.pdf`: Visualization insights.

---

## Requirements

- **Python 3.x**
- **Jupyter Notebook**
- **Power BI Desktop** (for interacting with `visualization.pbix`)
- **Python Libraries** (listed in `requirements.txt`):
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`

---

## Encouragement to Start

Ready to dive into e-commerce analytics? Clone this repo, follow the steps above, and explore the Olist dataset! Whether you’re refining the cleaning scripts, deepening the analysis, or crafting a stunning dashboard, this project is your playground. Contributions are welcome—fork the repo and submit a pull request with your ideas!

---

## License

This project is licensed under the MIT License. See the LICENSE file (or add one) for details.

---

## Contact

For questions or feedback, reach out via [Portfolio_Contact](https://peteradel.netlify.app/).
