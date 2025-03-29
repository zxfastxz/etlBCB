import pandas as pd
from src.extractTransform import requestApiBcb
from src.load import salvarCsv

dadosBcb = requestApiBcb('20191')
salvarCsv(dadosBcb, "etlBCB/src/datasets/meiosPagamentosTri.csv", ";",".")

