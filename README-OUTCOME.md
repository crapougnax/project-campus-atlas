# Compte Rendu


## Export SQL

### CA Total

```sql
SELECT SUM(qte * prix) as ca FROM ventes
```

### Ventes par produit

```sql
SELECT produit, SUM(qte) total_qte, SUM(qte * prix) total_ca FROM ventes GROUP BY produit
```

### Ventes par région

```sql
SELECT region, SUM(qte*prix) total_ca FROM ventes GROUP BY region
```

## Synthèse des résultats obtenus

### 3.a

44 825 

### 3.b

```json
[
  { "produit": "Produit A", "total_qte": 1750, "total_ca": 17500 },
  { "produit": "Produit B", "total_qte": 1055, "total_ca": 15825 },
  { "produit": "Produit C", "total_qte": 575, "total_ca": 11500 }
]
```

### 3.c

```json
[
  { "region": "Nord", "total_ca": 20725 },
  { "region": "Sud", "total_ca": 24100 }
]
```

### 6

voir fichier `native.py`

### 7

### 8

https://github.com/crapougnax/project-campus-atlas
