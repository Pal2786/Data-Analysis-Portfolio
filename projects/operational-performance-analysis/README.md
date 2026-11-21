# Operational Performance Analysis Using Python

## Project Overview
This project uses fictional operational data to analyse workload, processing times and performance trends.

## Tools
- Python
- pandas
- matplotlib
- Jupyter Notebook

## Objectives
- Clean and validate data
- Identify trends and bottlenecks
- Create data visualisations
- Recommend improvements

## Status
Completed - Portfolio demonstration using fictional data

## Analysis Results

This project analyses 10 days of fictional operational data.

### Key Findings
- Total new cases: 546
- Total resolved cases: 483
- Net workload increase: 63 cases
- Throughput-to-intake ratio: 88.5%

The analysis identifies a net increase in workload over the reporting period. Further investigation into processing capacity and workflow bottlenecks would help explain the difference between incoming and resolved cases.

### Data Visualisations

#### Daily Net Case Movement
![Operational analysis chart 1](IMG_3289.png)

#### Cumulative Net Workload Change
![Operational analysis chart 2](IMG_3290.png)

#### Daily Out-of-SLA Case Count
![Operational analysis chart 3](IMG_3291.png)

### Limitations
The analysis uses fictional data covering only 10 days. Cumulative net movement is not the same as actual backlog. The sum of daily out-of-SLA counts does not necessarily represent unique cases.
