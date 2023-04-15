from PyQt5 import uic,QtWidgets

import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_produtos"
)

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria = ""

    if formulario.radioButton.isChecked() :
        print("Categoria do produto: Eletronicos")
        categoria = "Eletronicos"
    elif formulario.radioButton_2.isChecked() :
        print("Categoria do produto: Alimentos")
        categoria = "Alimentos"
    elif formulario.radioButton_3.isChecked() :
        print("Categoria do produto: Brinquedos")
        categoria = "Brinquedos"
    else :
        print ("Não selecionou categoria")

    print("Referencial ID ",linha1)
    print("Nome ",linha2)
    print("Valor ",linha3)
    
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo, descricao, preco, categoria) VALUES (%s, %s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")




app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)


formulario.show()
app.exec()
