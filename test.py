from utils import Chain
import os
import others as ot
from portfolio import Portfolio

links="https://jobs.lever.co/AIFund/29e4750a-61c1-4195-9a11-7889577e3d6f"
chain = Chain()
portfolio = Portfolio()
result=ot.get_email(links, chain, portfolio)
print(result)