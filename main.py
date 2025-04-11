import pandas as pd
from src.extractTransform import requestApiBcb
from src.load import salvarCsv, salvarSQlite

dadosBcb = requestApiBcb("20191")
# salvarCsv(dadosBcb, "etlBCB/src/datasets/meiosPagamentosTri.csv", ";", ".")

salvarSQlite(dadosBcb, "src/datasets/dadosbcb.db", "meiosPagamentosTri")

# salvarMySQL(dadosBcb, "root", "root", "localhost", "etlbcb", "meiosPagamentostri")