#include "logindialog.h"
#include "ui_logindialog.h"
#include <QMessageBox>

LoginDialog::LoginDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::LoginDialog)
{
    ui->setupUi(this);
}

LoginDialog::~LoginDialog()
{
    delete ui;
}

void LoginDialog::on_login_pushButton_clicked()
{
    if(ui->usr_lineEdit->text()==tr("Telecom") && ui->pwd_lineEdit->text()==tr("iloveyou"))
        QDialog::accept();
    else {
        QMessageBox::warning(this,tr("警告"),tr("用户名密码输入有误"));
        ui->usr_lineEdit->clear();
        ui->pwd_lineEdit->clear();
        ui->usr_lineEdit->setFocus();
    }
}
