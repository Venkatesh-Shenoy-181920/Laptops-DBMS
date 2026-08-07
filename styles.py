# The main style sheet
style = """
/*Main Window BAckground*/
QMainWindow, QWidget#CentralWidget{
    background-color:#0F172A;
    color:#F8FAFc;
    font-family:'Segoe UI', Arial, sans-serif;
}

/*SideBar Styling*/
QFrameSidebar {
    background-color: #1E293B;
    border-right: 1px solid #334155;
    min-width: 180px;
}

QPushButton.NavBtn{
    background-color: transparent;
    color: #94A3B8;
    text-align: left;
    padding: 10px 16px;
    font-size: 14px;
    border: none;
    border-radius: 8px;
}

QPushButton.NavBtn:hover {
    background-color: #334155;
    color: #FFFFFF;
}

QPushButton.NavBtn:checked {
    background-color: #1D4ED8;
    color: #FFFFFF;
    font-weight: bold;
}

/* Top Search Field*/
QLineEdit#Searchbar {
    backgroud-color: #1E293B;
    color: #FFFFFF;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 8px 14px;
    font-size: 13px;
}

/* Primary Blue Action Button */
QPushButton#PrimaryBtn{
    background-color: #1D4ED8;
    color: #FFFFFF;
    font-weight: bold;
    border: none;
    border-radius: 8px;
    padding: 8px 16px;
}

QPushButton#PrimaryBtn:hover{
    background-color: #2563EB;
}

/* Table Styling*/
QTableWidget{
    background-color: #0F172A;
    border: none;
    outline: none;
    border-radius: 12px;
    gridline-color: transparent;
    color: #F8FAFC;
    selection-background-color: #1D4ED8;
    selection-color: #FFFFFF;    
}

QHeaderView::section{
    background-color:#0F172A;
    color:#94A3B8;
    font-weight: bold;
    font-size: 12px;
    padding: 8px;
    border:none;
    border-bottom: 1px solid #334155;    
}

QTableWidget::viewport{
    background-color:#0F172A;
}

QTableWidget::item{
    padding: 8px;
    border-bottom: 1px solid #334155;
}

/* Right Side Details Card*/
QFrame#DetailsPanel{
    background-color: #1E293B;
    border: 1px solid #334155;
    border-radius: 12px;
}

/*Action Buttons*/
QPushButton#EditBtn{
    background-color: #334155;
    color: #FFFFFF;
    border-radius: 6px;
    padding: 8px;
    font-weight: bold;
}

QPushButton#DeleteBtn{
    background-color:#DC2626;
    color: #FFFFFF;
    border-radius: 6px;
    padding: 8px;
    font-weight: bold;
}

QDialog{
    background-color: #0F0C1B;
}

QLabel#title{
    color: #FFFFFF;
    font-size: 22px;
    font-weight: bold;
}

QLabel#name_label{
    color: #FFFFFF;
    font-weight: bold;
    border: 1px solid #6366F1;
    border-radius: 12px;
    padding: 4px 12px;
}

QLabel#role_label{
    color: #94A3B8;
    font-size: 12px;
    font-weight: bold;
}

QLabel#email{
    color: #94A3B8;
    font-size: 12px;
    font-weight: bold;
}
"""