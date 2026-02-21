# Auto Savings Retirement System

Production-grade API for automated retirement savings using expense round-up
and investment projections.

## Features
- Expense rounding & micro-savings
- q / p / k temporal rules
- Index fund & NPS-ready design
- Inflation-adjusted returns
- Dockerized deployment

## Run with Docker
```bash
docker build -t auto-savings-retirement-system .
docker run -p 5477:5477 auto-savings-retirement-system