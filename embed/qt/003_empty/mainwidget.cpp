#include "mainwidget.h"
#include <QPushButton>
MainWidget::MainWidget(QWidget *parent) : QWidget(parent)
{
    b1.setParent(this);
    b1.setText("Telecom");
    b1.move(100,100);

    b2 = new QPushButton(this);
    b2->setText("Automation");
    b2->move(200,100);
    connect(&b1,&QPushButton::pressed,this,&MainWidget::close);
    connect(b2,&QPushButton::released,this,&MainWidget::myslot);
}
void MainWidget::myslot()
{
    b1.setText("i love you");
}
MainWidget::~MainWidget()
{

}
