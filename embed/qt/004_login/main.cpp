#include "mainwidget.h"

#include <QApplication>
#include "logindialog.h"
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWidget w;
    w.setWindowTitle("Embedded Technology DXZDH2017");
    LoginDialog login;
    if(login.exec()==QDialog::Accepted)
    {
    w.show();
    return a.exec();
    }
    else
        return 0;
}
