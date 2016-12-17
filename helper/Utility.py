from PySide import QtGui
from helper.Encrypt import Encrypt


class Utility:
    @staticmethod
    def show_message(title, message, type_icon):
        message_box = QtGui.QMessageBox()
        message_box.setIcon(type_icon)
        message_box.setText(message)
        message_box.setWindowTitle(title)
        message_box.setWindowIcon(QtGui.QIcon("images/logo.ico"))
        message_box.exec_()

    @staticmethod
    def dict_to_object(dictionary, obj, decrypt=True) -> object:
        encrypt = Encrypt()
        obj_result = type(obj.__class__.__name__, obj.__bases__, getattr(obj(), '__dict__'))
        for key in dictionary:
            if "id" not in key:
                value = dictionary[key]
                if decrypt and not (not value):
                    value = encrypt.decrypt(eval(value))
                setattr(obj_result, key, value)
        return obj_result

    @staticmethod
    def organize_result_mongo(dictionary, decrypt=True):
        encrypt = Encrypt()
        obj_result = {}
        for key in dictionary:
            if "id" not in key:
                value = dictionary[key]
                if decrypt and not (not value):
                    value = encrypt.decrypt(eval(value))
                obj_result[key] = value
        return obj_result
