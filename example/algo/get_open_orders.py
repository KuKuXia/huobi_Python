from huobi.client.algo import AlgoClient
from huobi.constant import *
from huobi.privateconfig import *
from huobi.utils import *

symbol_test = "adausdt"
account_id = g_account_id

algo_client = AlgoClient(api_key=p_api_key, secret_key=p_secret_key)
result = algo_client.get_open_orders()
print(result)
LogInfo.output_list(result)
