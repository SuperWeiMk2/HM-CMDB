from core.server import Server
from bean.pojo.account import Account


class AccountModel:

    @staticmethod
    def all_account():
        result = Server.datasource["default"].db["account"].find()

        accounts = []

        for item in result:
            accounts.append(Account(uid=item["uid"],
                                    name=item["name"],
                                    job_number=item["job_number"],
                                    group=item["group"],
                                    phone=item["phone"],
                                    email=item["email"],
                                    sex=item["sex"],
                                    arch_group=item["arch_group"],
                                    create_time=item["create_time"],
                                    update_time=item["update_time"]))
        return accounts

    @staticmethod
    def create_account(uid, name, job_number, group, phone, email, sex, arch_group, create_time, update_time):
        result = Server.datasource["default"].db["account"] \
            .insert_one({"uid": uid, "name": name, "job_number": job_number, "group": group,
                         "phone": phone, "email": email, "sex": sex, "arch_group": arch_group,
                         "create_time": create_time, "update_time": update_time, "is_delete": False})

        return result

    # @staticmethod
    # def get_account_by_name(name):
    #     result = Server.datasource["default"].db["group"].find({'_id': {"$regex": name}})
    #
    #     accounts = []
    #
    #     for item in result:
    #         accounts.append(Account(name=item["name"],
    #                                 ))
    #     pass

    @staticmethod
    def get_account_by_job_number(job_number):
        pass

    @staticmethod
    def delete_account_by_job_number(delete_by_job_number):
        result = Server.datasource["default"].db["account"].delete_one({"job_number": delete_by_job_number})

        return result

    @staticmethod
    def update_account_by_uid(uid, name, job_number, group, phone, email, sex, arch_group, update_time):
        result = Server.datasource["default"].db["account"] \
            .update_one({"uid": uid}, {"$set": {"name": name, "job_number": job_number, "group": group,
                                                "phone": phone, "email": email, "sex": sex, "arch_group": arch_group,
                                                "update_time": update_time}})
        return result

    @staticmethod
    def update_account(uid, name, job_number, group, phone, email, sex, arch_group, update_time):

        if name and job_number and group and phone and email and sex and arch_group is None:
            """
            不更新。
            """
            return {}

        elif job_number and group and phone and email and sex and arch_group is None:
            """
            只更新 id
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"update_time": update_time})
            return result

        elif group and phone and email and sex and arch_group is None:
            """
            更新 id 和 工号
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number},
                            {"update_time": update_time})
            return result

        elif job_number and phone and email and sex and arch_group is None:
            """
            更新 id 和 组
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"group": group}, {"update_time": update_time})
            return result

        elif job_number and group and email and sex and arch_group is None:
            """
            更新 id 和 phone
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"phone": phone}, {"update_time": update_time})
            return result

        elif job_number and group and phone and sex and arch_group is None:
            """
            更新 id 和 email
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"email": email}, {"update_time": update_time})
            return result

        elif job_number and group and phone and email and arch_group is None:
            """
            更新 id 和 sex
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"sex": sex}, {"update_time": update_time})
            return result

        elif job_number and group and phone and email and sex is None:
            """
            更新 id 和 arch_group
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"arch_group": arch_group},
                            {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id 、job_number、group
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number},
                            {"group": group}, {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """"
            更新 id、job_number、phone
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number}, {"phone": phone},
                            {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、job_number、email
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number}, {"email": email},
                            {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、job_number、sex
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number},{"sex": sex},
                            {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、job_number、arch_group
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number},
                            {"arch_group": arch_group},{"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、group、phone
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"group": group},
                            {"phone": phone},{"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、group、email
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}},{"group": group},
                            {"email": email},{"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、group、sex
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"group": group},{"sex": sex},
                            {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、group、arch_group
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"group": group},{"arch_group": arch_group},
                            {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、phone、email
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"phone": phone}, {"email": email},
                            {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、phone、sex
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}},{"phone": phone},{"sex": sex},
                            {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、phone、arch_group
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}},{"phone": phone}, {"arch_group": arch_group},
                            {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、email、sex
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}},{"email": email}, {"sex": sex},
                            {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、email、arch_group
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}},  {"email": email}, {"arch_group": arch_group},
                            {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、sex、arch_group
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}},{"sex": sex}, {"arch_group": arch_group},
                            {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、job_number、group、phone
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number}, {"group": group},
                            {"phone": phone}, {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、job_number、group、email
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number}, {"group": group},
                            {"email": email},{"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、job_number、group、sex
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number}, {"group": group},
                             {"sex": sex}, {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、job_number、group、arch_group
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number}, {"group": group},
                             {"arch_group": arch_group},{"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、job_number、email、sex
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number}, {"email": email},
                            {"sex": sex},{"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、job_number、email、arch_group
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number},{"email": email},
                            {"arch_group": arch_group},{"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、job_number、sex、arch_group
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number}, {"sex": sex},
                            {"arch_group": arch_group},{"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、group、phone、email
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}},  {"group": group},{"phone": phone},
                            {"email": email},{"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、group、phone、sex
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}},{"group": group},{"phone": phone}, {"sex": sex},
                            {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、group、phone、arch_group
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"group": group},{"phone": phone},
                            {"arch_group": arch_group},{"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、phone、email、sex
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"phone": phone}, {"email": email}, {"sex": sex},
                            {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、phone、email、arch_group
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"phone": phone}, {"email": email},
                            {"arch_group": arch_group},{"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、email、sex、arch_group
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"email": email}, {"sex": sex},
                            {"arch_group": arch_group},{"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、job_number、group、phone、email
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number}, {"group": group},
                            {"phone": phone}, {"email": email}, {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、job_number、group、phone、sex
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number}, {"group": group},
                            {"phone": phone}, {"sex": sex},  {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、job_number、group、phone、arch_group
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number}, {"group": group},
                            {"phone": phone},  {"arch_group": arch_group},{"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、group、phone、email、sex
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"group": group},{"phone": phone},
                            {"email": email}, {"sex": sex}, {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、group、phone、email、arch_group
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}},  {"group": group}, {"phone": phone},
                            {"email": email}, {"arch_group": arch_group},{"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、phone、email、sex、arch_group
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"phone": phone}, {"email": email},
                            {"sex": sex}, {"arch_group": arch_group},{"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、job_number、group、phone、email、sex
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number}, {"group": group},
                            {"phone": phone}, {"email": email}, {"sex": sex},{"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、job_number、group、phone、email、arch_group
            """
            result = Server.datasource["default"].db["group"] \
                .update_one({"uid": uid}, {"$set": {"_id": name}}, {"job_number": job_number}, {"group": group},
                            {"phone": phone}, {"email": email},{"arch_group": arch_group},
                            {"update_time": update_time})
            return result

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 id、group、phone、email、sex、arch_group
            """
            pass

        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、phone
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、email
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、sex
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、group、phone
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、group、email
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、group、sex
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、group、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、phone、email
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、phone、email
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、phone、sex
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、phone、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、email、sex
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、email、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、sex、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、group、phone、email、sex
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、group、phone、email、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 job_number、group、phone、email、sex、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 group、phone
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 group、email
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 group、sex
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 group、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 group、phone、email
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 group、phone、sex
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 group、phone、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 group、email、sex
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 group、email、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 group、phone、email、sex
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 group、phone、email、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 group、email、sex、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 group、phone、email、sex、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 phone
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 phone、email
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 phone、sex
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 phone、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 phone、email、sex
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 phone、email、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 phone、email、sex、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 email
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 email、sex
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 email、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 email、sex、arch_group
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 sex
            """
            pass
        elif name and job_number and group and phone and email and sex and arch_group is None:
            """
            更新 sex、arch_group
            """
            pass
        else:
            """
            更新 arch_group
            """
            pass
