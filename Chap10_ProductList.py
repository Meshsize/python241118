import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sqlite3
import os


def initialize_database():
    """데이터베이스 초기화 및 연결"""
    db_path = "ProductList.db"
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    if not os.path.exists(db_path):
        cur.execute(
            """
            CREATE TABLE Products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT,
                Price INTEGER
            );
            """
        )
    return con, cur


# DB 초기화
con, cur = initialize_database()

# 디자인 파일 로딩
form_class = uic.loadUiType("ProductList.ui")[0]


class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.initialize_ui()

        # 초기값 설정
        self.id = 0
        self.name = ""
        self.price = 0

    def initialize_ui(self):
        """UI 초기 설정"""
        self.setup_table()
        self.connect_signals()

    def setup_table(self):
        """테이블 위젯 초기 설정"""
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)

    def connect_signals(self):
        """UI 시그널 연결"""
        self.prodID.returnPressed.connect(self.focusNextChild)
        self.prodName.returnPressed.connect(self.focusNextChild)
        self.prodPrice.returnPressed.connect(self.focusNextChild)
        self.tableWidget.doubleClicked.connect(self.handle_double_click)

    def add_product(self):
        """제품 추가"""
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (self.name, self.price))
        self.refresh_table()
        con.commit()

    def update_product(self):
        """제품 수정"""
        self.id = self.prodID.text()
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        cur.execute("UPDATE Products SET Name = ?, Price = ? WHERE id = ?;", (self.name, self.price, self.id))
        self.refresh_table()
        con.commit()

    def remove_product(self):
        """제품 삭제"""
        self.id = self.prodID.text()
        cur.execute("DELETE FROM Products WHERE id = ?;", (self.id,))
        self.refresh_table()
        con.commit()

    def refresh_table(self):
        """테이블 새로고침"""
        self.tableWidget.clearContents()
        cur.execute("SELECT * FROM Products;")
        for row, item in enumerate(cur.fetchall()):
            self.add_table_row(row, item)

    def add_table_row(self, row, item):
        """테이블에 행 추가"""
        item_id = QTableWidgetItem(str(item[0]))
        item_id.setTextAlignment(Qt.AlignRight)
        self.tableWidget.setItem(row, 0, item_id)

        self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))

        item_price = QTableWidgetItem(str(item[2]))
        item_price.setTextAlignment(Qt.AlignRight)
        self.tableWidget.setItem(row, 2, item_price)

    def handle_double_click(self):
        """더블 클릭 이벤트 처리"""
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo_form = DemoForm()
    demo_form.show()
    sys.exit(app.exec_())
