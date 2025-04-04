import pandas as pd
from src.extractTransform import requestApiBcb
from src.load import salvarCsv, salvarSQlite, salvarMySQL

dadosBcb = requestApiBcb("20191")
salvarCsv(dadosBcb, "src/datasets/meiospagamentosTri.csv", ";", ".")

salvarSQlite(dadosBcb, "src/datasets/dadosbcb.db", "meiospagamentosTri")

salvarMySQL(dadosBcb, "root", "teste", "localhost", "etlbcb", "meiospagamentostri")