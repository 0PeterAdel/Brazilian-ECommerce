# Brazilian E-Commerce Data Challenge

This repository contains the solution to the **Brazilian E-Commerce Data Challenge** using the Brazilian E-Commerce Public Dataset by Olist. The project focuses on cleaning, analyzing, and visualizing e-commerce data to uncover insights into customer behavior, sales performance, and delivery metrics. The workflow includes data preparation, reconciliation of financial metrics, and the creation of a monthly financial dashboard.

---

## Project Structure

The repository is organized as follows:

```
.
├── Data_Analysis
│   ├── analysis.ipynb                # Notebook for data analysis and aggregation
│   ├── detailed_olist_data.csv       # Detailed dataset for visualization
│   ├── monthly_olist_data.csv        # Monthly aggregated data for dashboard
│   └── Report.docx                   # Analysis report in DOCX format
├── Data_Clean
│   ├── customers_dataset_clean.ipynb # Cleaning script for customers dataset
│   ├── Data_Cleaned                  # Folder with cleaned datasets
│   │   ├── cleaned_olist_customers_dataset.csv
│   │   ├── cleaned_olist_geolocation_dataset.csv
│   │   ├── cleaned_olist_order_items_dataset.csv
│   │   ├── cleaned_olist_order_payments_dataset.csv
│   │   ├── cleaned_olist_order_reviews_dataset.csv
│   │   ├── cleaned_olist_orders_dataset.csv
│   │   ├── cleaned_product_category_name_translation.csv
│   │   ├── cleaned_products_dataset.csv
│   │   ├── cleaned_sellers_dataset.csv
│   │   └── merged_olist_dataset.csv  # Merged cleaned dataset
│   ├── geolocation_dataset_clean.ipynb
│   ├── main.ipynb                    # Main script to orchestrate cleaning
│   ├── Merging_Datasets_Cleaned.ipynb # Merges all cleaned datasets
│   ├── order_items_dataset_clean.ipynb
│   ├── order_payments_dataset_clean.ipynb
│   ├── order_reviews_dataset_clean.ipynb
│   ├── orders_dataset_clean.ipynb
│   ├── product_category_name_translation_clean.ipynb
│   ├── products_dataset_clean.ipynb
│   ├── Report.pdf                    # Cleaning process report
│   └── sellers_clean.ipynb
├── DataSet
│   ├── olist_customers_dataset.csv   # Raw customers dataset
│   ├── olist_geolocation_dataset.csv # Raw geolocation dataset
│   ├── olist_order_items_dataset.csv # Raw order items dataset
│   ├── olist_order_payments_dataset.csv # Raw payments dataset
│   ├── olist_order_reviews_dataset.csv # Raw reviews dataset
│   ├── olist_orders_dataset.csv      # Raw orders dataset
│   ├── olist_products_dataset.csv    # Raw products dataset
│   ├── olist_sellers_dataset.csv     # Raw sellers dataset
│   └── product_category_name_translation.csv # Raw category translations
├── DataSet.zip                       # Zipped raw datasets
├── Instructions
│   └── Google Data Analysis Tech challenge.pdf # Challenge instructions
├── README.md                         # This file
├── Reports
│   ├── Clean_Report.docx             # Cleaning report in DOCX
│   ├── Clean_Report.pdf              # Cleaning report in PDF
│   ├── Analysis_Report.docx          # Analysis report in DOCX
│   └── Analysis_Report.pdf           # Analysis report in PDF
└── requirements.txt                  # Python dependencies
```

### Directory Breakdown
- **DataSet**: Raw datasets from Olist.
- **Data_Clean**: Scripts for cleaning each dataset and merging them into `merged_olist_dataset.csv`.
- **Data_Analysis**: Analysis notebook, aggregated data files, and report.
- **Reports**: Final cleaning and analysis reports in PDF and DOCX formats.
- **Instructions**: Challenge description.
- **requirements.txt**: Lists Python libraries needed.

---

## Project Steps

### 1. Data Cleaning
The raw datasets were cleaned to remove missing values, standardize formats, and eliminate duplicates. Each dataset has a dedicated cleaning notebook in the `Data_Clean` folder.

#### Cleaning Process
- **Datasets Cleaned**:
  - `customers_dataset_clean.ipynb`
  - `geolocation_dataset_clean.ipynb`
  - `order_items_dataset_clean.ipynb`
  - `order_payments_dataset_clean.ipynb`
  - `order_reviews_dataset_clean.ipynb`
  - `orders_dataset_clean.ipynb`
  - `product_category_name_translation_clean.ipynb`
  - `products_dataset_clean.ipynb`
  - `sellers_clean.ipynb`
- **Merged Output**: All cleaned datasets are combined into `merged_olist_dataset.csv` using `Merging_Datasets_Cleaned.ipynb`.
- **Documentation**: See `Report.pdf` in `Data_Clean` for details.

### 2. Data Analysis
The analysis was conducted in `analysis.ipynb` within the `Data_Analysis` folder, focusing on sales reconciliation and monthly trends.

#### Analysis Steps
- **Data Preparation**: Loaded `merged_olist_dataset.csv` and verified data integrity.
- **Reconciliation Metrics**:
  - **Total Revenue**: Sum of payments from delivered orders.
  - **Expected Revenue**: Sum of payments from approved orders.
  - **Canceled Orders**: Count of canceled orders.
  - **Late Deliveries**: Count of orders delivered after the estimated date.
- **Monthly Aggregation**: Aggregated data by month for financial metrics, order status, and delivery performance.
- **Output Files**:
  - `monthly_olist_data.csv`: Aggregated monthly data.
  - `detailed_olist_data.csv`: Detailed data for deeper insights.
- **Documentation**: See `Report.docx` in `Data_Analysis`.

### 3. Visualization and Reporting
- **Power BI Dashboard**: Used `monthly_olist_data.csv` and `detailed_olist_data.csv` to create an interactive dashboard with:
  - Financial summaries (revenue, payments).
  - Order status breakdowns (delivered, canceled, pending).
  - Delivery performance (late deliveries, delays).
- **Reports**:
  - `Clean_Report`: Details the cleaning process.
  - `Analysis_Report`: Summarizes analysis findings.

---

## How to Get Started

Follow these steps to set up and explore the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies**:
   Ensure Python 3.x is installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Data Cleaning**:
   - Go to `Data_Clean` and execute the cleaning notebooks (e.g., `customers_dataset_clean.ipynb`).
   - Merge the datasets with `Merging_Datasets_Cleaned.ipynb`.

4. **Perform Analysis**:
   - Open `analysis.ipynb` in `Data_Analysis` and run all cells.

5. **Build the Dashboard**:
   - Open Power BI Desktop.
   - Import `monthly_olist_data.csv` and `detailed_olist_data.csv`.
   - Create visualizations as outlined in the challenge.

6. **Explore Reports**:
   - Check the `Reports` folder for detailed documentation.

---

## Requirements

- **Python 3.x**
- **Jupyter Notebook**
- **Power BI Desktop**
- **Python Libraries** (see `requirements.txt`):
  - pandas
  - numpy
  - matplotlib
  - seaborn

---

## Encouragement to Start

Ready to dive into e-commerce analytics? Clone this repo, follow the steps above, and start exploring the Olist dataset! Whether you're improving the cleaning scripts, enhancing the analysis, or designing a stunning dashboard, this project is your playground. Contributions are welcome—fork the repo and submit a pull request with your ideas!

---

## License

This project is licensed under the MIT License. See the LICENSE file (or add one) for details.

---

## Contact

For questions or feedback, reach out via [Portfolio_Contact](https://peteradel.netlify.app/).

