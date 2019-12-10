import re
from datetime import datetime,timedelta
import pandas as pd
with open(r'C:\git\kodekalendere\knowit\dag10\logg.txt','r') as f:
    t = f.read()


d = {}
c = 0
for i in t.splitlines():
    if ':' in i:
        s = datetime.strptime(i,'%b %d:')
        d[s] = {}
        c = s
    else:
        g = re.match( '.*\* ([0-9]*) .* (.*)',i)
        if g:
            g= g.groups()
            d[c][g[1]] = int(g[0])
df = pd.DataFrame(d).transpose()

df.index = pd.to_datetime(df.index)
df.index = df.index + pd.DateOffset(years=118)

sj_sun = df[df.index.weekday_name == 'Sunday'].sum()['sjampo']
to_ons = df[df.index.weekday_name == 'Wednesday'].sum()['toalettpapir']
tann = df.sum()['tannkrem'] // 125
sjampo = df.sum()['sjampo'] // 300
papir = df.sum()['toalettpapir'] // 25

print(to_ons*tann*sjampo*papir*sj_sun)