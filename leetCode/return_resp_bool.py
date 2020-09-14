class ReturnRespBool(object):
    def cmp_resp(self, resp1, resp2, list):
        is_same = True
        for key in resp1:
            if key not in list:
                # print(resp2[key])
                # print(resp1[key])
                print(key in resp2.keys())
                if key in resp2.keys():
                    if type(resp1[key]) == dict:
                        is_same = self.cmp_resp(resp1[key], resp2[key],list)
                        if is_same == False:
                            break
                    else:
                        if resp1[key] != resp2[key]:
                            is_same = False
                            break
                        else:
                            is_same = True
                else:
                    is_same = False
                    break
        return is_same


if __name__ == "__main__":
    # ÓÃÀı1£º
    xx = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["3333", "4444", "111"]}}
    yy = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["111", "3333", "4444"]}}
    list = ["22222"]

    ReturnRespBool().cmp_resp(xx, yy, list)
