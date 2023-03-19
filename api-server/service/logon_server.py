from model.logon_model import LogonModel


class LogonServer:

    @staticmethod
    def logon(name, password):
        return LogonModel.check_username_and_password(name, password)
