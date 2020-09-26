import time
import sweetviz as sv
import pandas as pd
import sys

def analysis():
    output = pd.read_csv("C:\\xampp\\htdocs\\Pasckathon_Hack-o-holics\\static\\output.csv")
    report = sv.analyze(output)
    ts = time.time()
    ts = str(int(ts))
    report.show_html(ts+".html")
    sys.exit()
