from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from cfgi_ui import Ui_MainWindow
import re
from copy import deepcopy, copy
from ContextFreeGrammar import CFG
import sys

rules = set()
nonterminals = set()
terminals = set()

class CFGI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lhs_input = ""
        self.rhs_input = ""
        self.input_all_rules = ""     
        self.lhs_edit.textChanged[str].connect(self.get_input_grammar)
        self.rhs_edit.textChanged[str].connect(self.get_input_grammar)
        self.cfg = None                    
        self.input_pushButton.clicked.connect(self.verify_grammar)
        self.Confirm_Button.clicked.connect(self.set_grammar)
        self.test_TextEdit.textChanged.connect(self.get_test_input)
        self.test_input = ""
        self.test_pushButton.clicked.connect(self.test_string)

    def get_input_grammar(self):
        self.lhs_input = self.lhs_edit.text()
        self.rhs_input = self.rhs_edit.text()
        
    def verify_grammar(self):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QMessageBox.Question)
                reply = msg.question(self, 'Verification Step', '{0} -> {1} is the rule you want to add?'.format(self.lhs_input, self.rhs_input), QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                if reply == QtWidgets.QMessageBox.Yes:
                    self.rules_textBrowser.append('{0} -> {1}\n'.format(self.lhs_input, self.rhs_input))
                    nonterminals.add(self.lhs_input)

                    for i in range(len(self.rhs_input)):
                        s_part = str(self.rhs_input[i]).strip()

                        for char in s_part:
                            if re.compile("[A-Z]").fullmatch(char):
                                nonterminals.add(char)
                            elif char == '|':
                                continue
                            else:            
                                terminals.add(char)
                    
                    self.input_all_rules += self.lhs_input + '->' +self.rhs_input + "\n"                            
                                        
    def set_grammar(self):

        try:
            start_symbol = "S"
            nonterminals.add(start_symbol) 
            null_character = "ε"
            terminals.add(null_character)  

            for line in self.input_all_rules.strip().split('\n'):
                
                line = line.strip()

                if not line:
                    continue

                line_parts = line.split('->')
                if len(line_parts) != 2:
                    raise ValueError("Rule syntax error : {}".format(line))

                line_parts = [line_part.strip() for line_part in line_parts]

                if line_parts[1].count('|') != 0:
                    second_parts = line_parts[1].split('|')
                    for second_part in second_parts:
                        second_part = second_part.strip()
                        if not second_part:
                            raise ValueError("Rule syntax error : {}".format(line))

                        rules.add((line_parts[0], second_part))

                else:
                    rules.add((line_parts[0], line_parts[1]))
            
            cfg_grammar = CFG(nonterminals, terminals, rules, start_symbol, null_character)
            cfg = copy(cfg_grammar)
            cfg.cnf()
            
            self.cfg = cfg

        except ValueError as e:
            messagebox.showerror("Input CFG Error", e.args[0])
            self.cfg = None 
            return

    def get_test_input(self):
        self.test_input = self.test_TextEdit.toPlainText()

    def test_string(self):
        test_input = str(self.test_input).splitlines()
        
        for i in range(len(test_input)):

            if self.cfg.cyk(str(test_input[i])):
                self.result_textBrowser.append("Yes! The string is accepted by the grammar") 
            else:
                self.result_textBrowser.append("No! The string is not accepted by the grammar")   
   
if __name__ == "__main__":
  
    app = QtWidgets.QApplication(sys.argv)
    cfgi_gui = CFGI()
    cfgi_gui.show()
    app.exec_()

