# etlBCB

## Explicação de cada Função implementada no repositório

### 🔎 Coleta de Dados
~~~~ python
def requestApiBcb(data: str) -> pd.DataFrame:
    url = f'https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%27{data}%27&$format=json'

    req = requests.get(url)
    dados = req.json()

    df = pd.json_normalize(dados['value'])

    df['datatrimestre'] = pd.to_datetime(df['datatrimestre'])

    return df
~~~~
Esta função foi criada com o objetivo de automatizar a coleta de dados trimestrais sobre meios de pagamento disponibilizados pela API pública do Banco Central do Brasil.

O que ela faz:

* Monta a URL de requisição com base no parâmetro data, que representa o trimestre desejado (ex: "20191").
* Realiza uma requisição HTTP para a API do Banco Central.
* Converte a resposta JSON em um DataFrame do Pandas, facilitando a manipulação e análise dos dados.
* Converte a coluna datatrimestre para o tipo datetime, padronizando a formatação temporal e assim evitando problemas possíveis com o banco de dados por exemplo.

### 💱 Conversão de Formato
~~~~python
def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    df.to_csv(nome_arquivo, sep=separador, decimal=decimal)
    return
~~~~
Esta função foi criada para salvar qualquer DataFrame do Pandas em um arquivo .csv de forma personalizada.

O que ela faz:

* Recebe o DataFrame que deve ser salvo, o nome do arquivo de destino, o separador de colunas (sep) e o caractere usado para decimais (decimal).
* Utiliza o método to_csv() para exportar os dados com as configurações informadas.
* Ideal para garantir compatibilidade com ferramentas que exigem formatos específicos (por exemplo, Excel com ; e , em regiões como o Brasil).

# Dicionário de Dados do Repositório

| Nome                        | Tipo     | Título                              | Descrição |
|-----------------------------|----------|-------------------------------------|-----------|
| datatrimestre               | texto    | Trimestre                           | — |
| valorPix                    | decimal  | Valor Pix                           | Volume financeiro (R$ milhões) de transações Pix liquidadas trimestralmente no SPI e fora do SPI, considerando ordens de pagamento e devoluções no período. Dados referentes às transações liquidadas fora do SPI, estão sujeitas a alterações retroativas, pois dependem da prestação de informação pelos participantes. |
| valorTED                    | decimal  | Valor TED                           | Montante financeiro (R$ milhões) trimestral transferido por meio de TED. Transferência Eletrônica Direta (TED) - transferência financeira, em tempo real, entre diferentes bancos e demais instituições (financeiras ou de pagamentos) detentoras de conta no Banco Central. Pode ser utilizada para transferir valores entre correntistas de diferentes instituições, e entre as próprias instituições, envolvendo pagamento de obrigações ou não. |
| valorTEC                    | decimal  | Valor TEC                           | Montante financeiro (R$ milhões) trimestral transferido por meio de TEC. Transferência Especial de Crédito (TEC) - transferência financeira utilizada por empresas para pagamento de benefícios aos empregados. |
| valorCheque                 | decimal  | Valor Cheque                        | Montante financeiro (R$ milhões) de cheques interbancários e intrabancários compensados trimestralmente. |
| valorBoleto                 | decimal  | Valor Boleto                        | Montante financeiro (R$ milhões) de boletos interbancários e intrabancários compensados trimestralmente. |
| valorDOC                    | decimal  | Valor DOC                           | Montante financeiro (R$ milhões) trimestral transferido por meio de DOC. |
| valorCartaoCredito          | decimal  | Valor Cartão de Crédito             | Valor (R$ milhões) de transações realizadas com cartão de crédito. |
| valorCartaoDebito           | decimal  | Valor Cartão de Débito              | Valor (R$ milhões) de transações realizadas com cartão de débito trimestralmente. |
| valorCartaoPrePago          | decimal  | Valor Cartão Pré-pago               | Valor (R$ milhões) de transações realizadas com cartão pré-pago trimestralmente. |
| valorTransIntrabancaria     | decimal  | Valor Transferência Intrabancária   | Montante financeiro (R$ milhões) de transferências realizadas trimestralmente entre contas de clientes da Instituição, inclusive aquelas envolvendo movimentações referentes a aplicações e resgates em fundos de investimento. |
| valorConvenios              | decimal  | Valor Convênio                      | Montante financeiro (R$ milhões) referente a arrecadações trimestrais governamentais (arrecadação de tributos e encargos sociais em virtude de convênios firmados entre a instituição e as entidades governamentais) e não-governamentais (arrecadações referentes aos convênios firmados entre a instituição e entidades privadas). |
| valorDebitoDireto           | decimal  | Valor Débito Direto                 | Montante financeiro (R$ milhões) trimestral referente a débitos previamente autorizados pelo cliente em sua conta corrente/pagamento, referente ao pagamento de contas recorrentes e a débitos que a instituição efetua na conta dos clientes em virtude de cobrança de tarifas pelos serviços prestados. |
| valorSaques                 | decimal  | Valor Saque                         | Montante sacado (R$ milhões) nos caixas eletrônicos trimestralmente. |
| quantidadePix               | decimal  | Quantidade Pix                      | Quantidade (em milhares) de transações Pix liquidadas trimestralmente no SPI e fora do SPI, considerando ordens de pagamento e devoluções no período. |
| quantidadeTED               | decimal  | Quantidade TED                      | Quantidade (em milhares) de TED realizadas trimestralmente. Transferência Eletrônica Direta (TED) - transferência financeira, em tempo real, entre diferentes bancos e demais instituições (financeiras ou de pagamentos) detentoras de conta no Banco Central. Pode ser utilizada para transferir valores entre correntistas de diferentes instituições, e entre as próprias instituições, envolvendo pagamento de obrigações ou não. |
| quantidadeTEC               | decimal  | Quantidade TEC                      | Quantidade (em milhares) de TEC realizadas trimestralmente. Transferência Especial de Crédito (TEC) - transferência financeira utilizada por empresas para pagamento de benefícios aos empregados. |
| quantidadeCheque            | decimal  | Quantidade Cheque                   | Quantidade (em milhares) de cheques interbancários e de cheques intrabancários compensados trimestralmente. |
| quantidadeBoleto            | decimal  | Quantidade Boleto                   | Quantidade (em milhares) de cheques interbancários e intrabancários compensados trimestralmente. |
| quantidadeDOC               | decimal  | Quantidade DOC                      | Quantidade (em milhares) de DOC realizados trimestralmente. |
| quantidadeCartaoCredito     | decimal  | Quantidade Cartão de Crédito        | Quantidade (em milhares) de transações realizadas com cartão de crédito trimestralmente. |
| quantidadeCartaoDebito      | decimal  | Quantidade Cartão de Débito         | Quantidade (em milhares) de transações realizadas com cartão de débito trimestralmente. |
| quantidadeCartaoPrePago     | decimal  | Quantidade Cartão Pré-pago          | Quantidade (em milhares) de transações realizadas com cartão pré-pago trimestralmente. |
| quantidadeTransIntrabancaria| decimal  | Quantidade de Transferência Intrabancária | Quantidade (em milhares) de transferências realizadas trimestralmente entre contas de clientes da Instituição, inclusive aquelas envolvendo movimentações referentes a aplicações e resgates em fundos de investimento. |
| quantidadeConvenios         | decimal  | Quantidade Convênio                 | Quantidade (em milhares) de transações realizadas referentes a arrecadações trimestrais governamentais (arrecadação de tributos e encargos sociais em virtude de convênios firmados entre a instituição e as entidades governamentais) e não-governamentais (arrecadações referentes aos convênios firmados entre a instituição e entidades privadas). |
| quantidadeDebitoDireto      | decimal  | Quantidade Débito Direto            | Quantidade (em milhares) de transações trimestrais referente a débitos previamente autorizados pelo cliente em sua conta corrente/pagamento, referente ao pagamento de contas recorrentes e a débitos que a instituição efetua na conta dos clientes em virtude de cobrança de tarifas pelos serviços prestados. |
| quantidadeSaques            | decimal  | Quantidade de Saque                 | Quantidade (em milhares) de saques realizados nos caixas eletrônicos trimestralmente. |
