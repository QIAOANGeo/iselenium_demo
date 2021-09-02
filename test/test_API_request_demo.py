import requests


def test_api_request():
    result = requests.get("https://www.baidu.com/sugrec?prod=pc_his&from=pc_web&json=1&sid=34438_34380_34496_31254_33848_34092_26350_34418_34474&hisdata=&_t=1630598027216&req=2&csor=0")
    res = result.content
    print(res)