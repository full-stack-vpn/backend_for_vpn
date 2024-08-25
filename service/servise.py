from repository.repository import work_with_bd
class work_with_vpn:
    @staticmethod
    def get_comfig(name_country,user_name):
        if user_name in work_with_bd.bd_read():
            pass
        else:
            data ={
                "user_name":name_country,
                "paid_or_free":"off",
                "over_day":"0",
            }
            work_with_bd.bd_create(data)