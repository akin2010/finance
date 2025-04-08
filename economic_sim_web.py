# economic_sim_web.py
import os
from io import BytesIO
import pandas as pd
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Union,Iterable
from enum import Enum
from datetime import datetime, timedelta
import base64
from copy import deepcopy
from flask import send_file,flash,url_for,Flask, request, render_template_string, redirect,session

try:
    import openpyxl
    from openpyxl.styles import Alignment, Border, Side
    from openpyxl.utils import get_column_letter
    EXCEL_AVAILABLE = True
except ImportError:
    print("Warning: openpyxl package not found. Excel export functionality will be disabled.")
    print("To enable Excel export, please install openpyxl using: pip install openpyxl")
    EXCEL_AVAILABLE = False

# ... [rest of the code from 1.4EconomicSimulationWebUI.py] ...

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24).hex()
system = EconomicSystem()

# ... [rest of the routes and application code] ... 