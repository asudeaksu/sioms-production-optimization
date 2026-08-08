# SIOMS — Smart Inventory & Operations Management System

## Overview

SIOMS (Smart Inventory & Operations Management System) is a Python-based inventory and operations management project developed as part of my Industrial Engineering learning journey at Bilkent University.

The project focuses on managing inventory data, performing basic inventory analysis, and building a foundation for future production optimization and data visualization workflows.

## Current Features

### Inventory Management
- Add new products
- Display all products
- Search products by name
- Update product quantity and price
- Delete products

### Data Management
- Store inventory data in CSV format
- Load inventory data automatically when the application starts
- Save changes after adding, updating, or deleting products
- Maintain persistent inventory data between program sessions

### Inventory Analysis
- Calculate total number of products
- Calculate total items in stock
- Calculate total inventory value

## Technologies

- Python
- CSV
- Pandas
- NumPy

## Project Structure

```text
SIOMS/
│
├── main.py
├── production_optimizer.py
├── products.csv
├── requirements.txt
├── data/
├── outputs/
├── docs/
└── README.md