#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

class ZJFWidget : public QWidget
{
    Q_OBJECT

public:
    ZJFWidget(QWidget *parent = nullptr);
    ~ZJFWidget();
};
#endif // WIDGET_H
