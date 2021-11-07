# -*- coding: utf-8 -*-
"""upstream.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jrTYZ03FV_SYVPVdvW9qNyZGVSYTzpBV
"""

# upstream.py

import pandas as pd
import quandl

from connect import DATAPATH

quandl.ApiConfig.api_key = os.environ.get("QUANDL_API_KEY")

def put_fred_data():
  """Store FRED data to the DB."""

  data = quandl.get('FRED/GDP', start_date="2001-12-31", end_date="2005-12-31")

  filename = DATAPATH + "fred_data.ftr"

  data.to_feather(filename)