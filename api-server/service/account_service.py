from model.account_model import AccountModel


class AccountService:

    @staticmethod
    def get_all_account():
        return AccountModel.all_account()

    @staticmethod
    def get_account_by_uid(uid):
        pass

    @staticmethod
    def list_account(name, phone, email, sex, arch_group):
        pass

    @staticmethod
    def create_account(uid, name, job_number, group, phone, email, sex, arch_group, create_time, update_time):
        empty_ok = [uid, name, job_number, group, phone, email, sex, arch_group, create_time, update_time]

        for OK in empty_ok:
            if OK is None:
                return False

        return AccountModel.create_account(uid, name, job_number, group, phone, email, sex, arch_group, create_time,
                                           update_time)

    @staticmethod
    def delete_account_by_job_number(delete_by_job_number):
        return AccountModel.delete_account_by_job_number(delete_by_job_number)

    @staticmethod
    def batch_delete_account(uid_list):
        return AccountModel.batch_delete_account(uid_list)

    @staticmethod
    def update_account(uid, name, job_number, group, phone, email, sex, arch_group, update_time):
        if uid is None:
            return {}
        else:
            return AccountModel.update_account_by_uid(uid, name, job_number, group, phone, email, sex, arch_group, update_time)
