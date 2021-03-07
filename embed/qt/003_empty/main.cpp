#include <QApplication>
#include "mainwidget.h"
int main(int argc, char *argv[])
{
    QApplication app(argc,argv);
    MainWidget w;
    w.setWindowTitle("Embedded Technology 2017");
    w.show();
    return app.exec();
/*
    QWidget w;
    w.setWindowTitle("Embedded Technolgy 2017");

    QPushButton b1(&w), *b2;
    b1.setText("Telecom");
    b1.move(100,100);

    b2 = new QPushButton;
    b2->setText("Automation");
    b2->setParent(&w);
    b2->move(200,100);

    w.show();
*/

}
