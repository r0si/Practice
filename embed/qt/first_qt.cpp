#include <QApplication>
#include <QPushButton>
#include <QWidget>

int main(int argc, char *argv[]) {
  QApplication app(argc, argv);
  QWidget w;
  w.setWindowTitle("Embedded Technology 2017");

  QPushButton b1;
  b1.setText("Telecom");
  b1.setParent(&w);
  b1.move(100, 100);

  w.show();

  app.exec();
  return 0;
}
