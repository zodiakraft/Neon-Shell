#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <math.h>
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    ui->lineEdit_point->setReadOnly(true);
    ui->pushButton_Clean->click();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_Clean_clicked()
{
    ui->lineEdit_Name->clear();
    ui->lineEdit_Strenght->clear();
    ui->lineEdit_Agility->clear();
    ui->lineEdit_Luck->clear();
    ui->lineEdit_intellegence->clear();

    ui->label_Attack->clear();
    ui->label_Mana->clear();
    ui->label_Health->clear();
    ui->label_Defense->clear();
    ui->label_Class->clear();

    ui->radioButton_sex_m->setChecked(true);

    ui->lineEdit_point->setText("20");
    ui->label_intellegence->setStyleSheet("color:black");
    ui->label_strenght->setStyleSheet("color:black");
    ui->label_luck->setStyleSheet("color:black");
    ui->label_agility->setStyleSheet("color:black");
}



void MainWindow::on_pushButton_Create_clicked()
{
    QString name;
    int dlina_stroki;
    bool flag;
    bool inter1;
    bool inter2;
    bool inter3;
    bool inter4;

    int strength, agility, intellegence, luck;

    name = ui->lineEdit_Name->text();
    dlina_stroki=name.length();
    if((dlina_stroki<3)||(dlina_stroki>20))
        {
            flag = false;
            QMessageBox::information(this, "Ошибка", "Некорректная длина имени", QMessageBox::Ok);
        }

        else{
               flag = true;
    }

    //сила
    strength = 0;
    if(flag){
        if (ui->radioButton_sex_m->isChecked()){
            {
                strength = ui->lineEdit_Strenght->text().toInt(&inter1);
                if(flag and inter1)
                {
                    if((strength<1)||(strength>12))
                        {
                        flag = false;
                        QMessageBox::information(this, "Ошибка", "\"Сила\" должна быть от 1 до 12", QMessageBox::Ok);
                                              }
                    }
                    else if(!inter1){
                        QMessageBox::information(this, "Ошибка", "некорректное значение параметра силы", QMessageBox::Ok);
                    }
                }
            }
        else if (ui->radioButton_sex_f->isChecked()) {

                strength = ui->lineEdit_Strenght->text().toInt(&inter1);
                if(flag and inter1)
                {
                    if((strength<1)||(strength>8))
                    {
                    flag = false;
                    QMessageBox::information(this, "Ошибка", "\"Сила\" должна быть от 1 до 8", QMessageBox::Ok);
                    }
                else if(!inter1){
                    QMessageBox::information(this, "Ошибка", "некорректное значение параметра силы", QMessageBox::Ok);
                    }
                }
            }
        }

    else {
        QMessageBox::information(this, "Ошибка", "Неправильное значение параметра силы", QMessageBox::Ok);
         }



    //ловкость
    agility = 0;
    if(flag){
        if (ui->radioButton_sex_m->isChecked()){
            {
                agility = ui->lineEdit_Agility->text().toInt(&inter2);
                if(flag and inter2)
                {
                    if((agility<1)||(agility>8))
                    {
                    flag = false;
                    QMessageBox::information(this, "Ошибка", "\"ловкость\" должна быть от 1 до 8", QMessageBox::Ok);
                    }
                }
                else if(!inter2){
                    QMessageBox::information(this, "Ошибка", "некорректное значение параметра ловкости", QMessageBox::Ok);
                }
            }
        }
        else if (ui->radioButton_sex_f->isChecked()) {

                agility = ui->lineEdit_Agility->text().toInt(&inter2);
                if(flag and inter2)
                {
                    if((agility<1)||(agility>12))
                    {
                    flag = false;
                    QMessageBox::information(this, "Ошибка", "\"Ловкость\" должна быть от 1 до 12", QMessageBox::Ok);
                    }
                else if(!inter2){
                    QMessageBox::information(this, "Ошибка", "некорректное значение параметра ловкости", QMessageBox::Ok);
                    }
                }
            }
        }

    else {
        QMessageBox::information(this, "Ошибка", "Неправильное значение параметра ловкости", QMessageBox::Ok);
         }



    //интеллект
    intellegence = 0;
    if(flag){
        if (ui->radioButton_sex_m->isChecked()){
            {
                intellegence = ui->lineEdit_intellegence->text().toInt(&inter3);
                if(flag and inter3)
                {
                    if((intellegence<1)||(intellegence>12))
                    {
                    flag = false;
                    QMessageBox::information(this, "Ошибка", "\"Интеллект\" должен быть от 1 до 12", QMessageBox::Ok);
                    }
                }
                else if(!inter3){
                    QMessageBox::information(this, "Ошибка", "некорректное значение параметра интеллекта", QMessageBox::Ok);
                }
            }
        }
        else if (ui->radioButton_sex_f->isChecked()) {

                intellegence = ui->lineEdit_intellegence->text().toInt(&inter3);
                if(flag and inter3)
                {
                    if((intellegence<1)||(intellegence>8))
                    {
                    flag = false;
                    QMessageBox::information(this, "Ошибка", "\"Интеллект\" должен быть от 1 до 8", QMessageBox::Ok);
                    }