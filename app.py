import plotly.express as px
import pandas as pd

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

df['ca'] = df.prix * df.qte

figure = px.pie(df, values='qte', names='region', title='quantité vendue par région')
figure.write_html('ventes-par-region.html')

grouped = df.groupby('produit', as_index=False, sort=True).agg({ 'qte': ['sum', 'std', 'var'], 'ca': ['sum', 'mean', 'median'] })

grouped.columns = ['produit', 'qte_sum', 'qte_std','qte_var', 'ca_sum', 'ca_mean', 'ca_median']
print(grouped)

vpp = px.pie(grouped, values='qte_sum', names='produit', title='quantité vendue par produit')
vpp.write_html('ventes-par-produit.html')

cpp = px.pie(grouped, values='ca_sum', names='produit', title='ca par produit')
cpp.write_html('ca-par-produit.html')
