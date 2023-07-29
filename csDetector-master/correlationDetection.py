import pandas as pd

communitySmell1 = input("Inserisci il primo community smell (acronimo): ")
communitySmell2 = input("Inserisci il secondo community smell (acronimo): ")


dataframe = pd.read_excel('./communitySmellsDataset.xlsx', sheet_name="dataset")

pivot_table = pd.pivot_table(dataframe, index=communitySmell1, columns=communitySmell2, aggfunc='size')
contingency_table = pivot_table.iloc[::-1, ::-1]
print(contingency_table)
totals = contingency_table.sum(axis=1)
risk = contingency_table.div(totals, axis=0)
print(risk)

relative_risk = risk.loc[1, 1] / risk.loc[0, 1]
print(f'Relative risk: {relative_risk:3.1f}')
odds = contingency_table[1] / contingency_table[0]

odds_ratio = odds[1] / odds[0]

print(f'Odds ratio: {odds_ratio:3.1f}')




