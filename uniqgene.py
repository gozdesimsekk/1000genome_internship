import pandas as pd
import os


rs1815739 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1815739.csv')
rs4644994 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs4644994.csv')
rs4253778 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs4253778.csv')
rs1042713 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1042713.csv')
rs8192678 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs8192678.csv')
rs2070744 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs2070744.csv')
rs11549465 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs11549465.csv')
rs1800012 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1800012.csv')
rs12722 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs12722.csv')
rs1049434 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1049434.csv')
rs1800795 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1800795.csv')
rs6265 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs6265.csv')
rs4680 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs4680.csv')


rsler = [rs1815739, rs4644994, rs4253778, rs1042713, rs8192678, rs2070744, rs11549465, rs1800012, rs12722, rs1049434, rs1800795, rs6265, rs4680]
foldisim = ["rs1815739", "rs4644994", "rs4253778", "rs1042713", "rs8192678", "rs2070744", "rs11549465", "rs1800012", "rs12722", "rs1049434", "rs1800795", "rs6265", "rs4680"]

#population = list(i['Population(s)'])
def ethnicchang(df):
    for index,value in enumerate(population):
        for j in ["AFR", "AMR", "EAS", "EUR", "SAS"]:
            if j in value:
                population[index] = j
    df['Population(s)'] = population


for i in rsler:
    for j in foldisim:
        if os.path.isdir(f"/Users/gamze/PycharmProjects/pythonProject1/{j}") == False:
            os.mkdir(f"/Users/gamze/PycharmProjects/pythonProject1/{j}")

        population = list(i['Population(s)'])
        ethnicchang(i)

    data_grp = i.groupby('Population(s)')
    for c in ["AFR", "AMR", "EAS", "EUR", "SAS"]:
        df1 = data_grp.get_group(c)
        df1.head()

        for a in range(len(df1)):
            df1.iloc[:, 1:].to_csv("/Users/gamze/PycharmProjects/pythonProject1/{}/{}.csv".format(j, c))
