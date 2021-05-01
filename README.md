# Sentiment Analyzer for Crypto news

Tested with python 3.8, 3.9 doesn't work because BASC-py4chan is broken atm with that version 

## Collect Data from 4chan
**No ORM provided**

### Setup
- provide mariadb || use docker-compose
- setup db + connection
- import seed.sql to mysql
### Usage
Run
```
python3 collect-4chan-biz-data.py
```
every hour
## Analyze
### count-coins
Just counts the coins foreach thread. 
Generates a top5 when possible and stores results.




## Work in progress 
1. Fix todos
2. Caching
3. Better Analyzers
4. Benchmarking (log results with rates to Google Sheets)
5. More sources
6. Use TT RSS
