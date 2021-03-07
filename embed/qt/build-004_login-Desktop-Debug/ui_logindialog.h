/********************************************************************************
** Form generated from reading UI file 'logindialog.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LOGINDIALOG_H
#define UI_LOGINDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_LoginDialog
{
public:
    QLabel *usernamelabel;
    QLabel *pwdlabel;
    QLineEdit *usr_lineEdit;
    QLineEdit *pwd_lineEdit;
    QPushButton *login_pushButton;
    QPushButton *exit_pushButton;
    QLabel *label;

    void setupUi(QDialog *LoginDialog)
    {
        if (LoginDialog->objectName().isEmpty())
            LoginDialog->setObjectName(QString::fromUtf8("LoginDialog"));
        LoginDialog->resize(400, 300);
        usernamelabel = new QLabel(LoginDialog);
        usernamelabel->setObjectName(QString::fromUtf8("usernamelabel"));
        usernamelabel->setGeometry(QRect(40, 80, 79, 25));
        pwdlabel = new QLabel(LoginDialog);
        pwdlabel->setObjectName(QString::fromUtf8("pwdlabel"));
        pwdlabel->setGeometry(QRect(40, 130, 79, 25));
        usr_lineEdit = new QLineEdit(LoginDialog);
        usr_lineEdit->setObjectName(QString::fromUtf8("usr_lineEdit"));
        usr_lineEdit->setGeometry(QRect(130, 80, 131, 33));
        pwd_lineEdit = new QLineEdit(LoginDialog);
        pwd_lineEdit->setObjectName(QString::fromUtf8("pwd_lineEdit"));
        pwd_lineEdit->setGeometry(QRect(130, 120, 131, 33));
        login_pushButton = new QPushButton(LoginDialog);
        login_pushButton->setObjectName(QString::fromUtf8("login_pushButton"));
        login_pushButton->setGeometry(QRect(100, 180, 104, 33));
        exit_pushButton = new QPushButton(LoginDialog);
        exit_pushButton->setObjectName(QString::fromUtf8("exit_pushButton"));
        exit_pushButton->setGeometry(QRect(240, 180, 104, 33));
        label = new QLabel(LoginDialog);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(30, 30, 211, 25));

        retranslateUi(LoginDialog);
        QObject::connect(exit_pushButton, SIGNAL(clicked()), LoginDialog, SLOT(close()));

        QMetaObject::connectSlotsByName(LoginDialog);
    } // setupUi

    void retranslateUi(QDialog *LoginDialog)
    {
        LoginDialog->setWindowTitle(QCoreApplication::translate("LoginDialog", "Dialog", nullptr));
        usernamelabel->setText(QCoreApplication::translate("LoginDialog", "\347\224\250\346\210\267\345\220\215\357\274\232", nullptr));
        pwdlabel->setText(QCoreApplication::translate("LoginDialog", "\345\257\206\347\240\201\357\274\232", nullptr));
        usr_lineEdit->setPlaceholderText(QCoreApplication::translate("LoginDialog", "\350\257\267\350\276\223\345\205\245\347\224\250\346\210\267\345\220\215", nullptr));
        pwd_lineEdit->setPlaceholderText(QCoreApplication::translate("LoginDialog", "\350\257\267\350\276\223\345\205\245\345\257\206\347\240\201", nullptr));
        login_pushButton->setText(QCoreApplication::translate("LoginDialog", "\347\231\273\345\275\225", nullptr));
        exit_pushButton->setText(QCoreApplication::translate("LoginDialog", "\351\200\200\345\207\272", nullptr));
        label->setText(QCoreApplication::translate("LoginDialog", "\346\254\242\350\277\216\346\235\245\345\210\260\345\265\214\345\205\245\345\274\217\350\256\241\347\256\227\346\234\272", nullptr));
    } // retranslateUi

};

namespace Ui {
    class LoginDialog: public Ui_LoginDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LOGINDIALOG_H
