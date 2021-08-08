#include "zjfwidget.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    ZJFWidget w;
    w.show();
    return a.exec();
}
