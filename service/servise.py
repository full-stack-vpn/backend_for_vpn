from repository.repository import work_with_bd
class work_with_vpn:
    @staticmethod
    def get_comfig(name_country,user_name):
        if user_name in work_with_bd.bd_read():
            pass
        else:
            work_with_bd.bd_create("test")