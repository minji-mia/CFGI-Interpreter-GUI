# CFGI-Interpreter-GUI

The project is for a context-free grammar interpreter. The interpreter takes as input a context-free grammar and a string to parse and gives an output whether the test string is either accepted or rejected. The program is implemented in a GUI, using Python.

## Program Overview

It consists of three files. One is for setting context free grammar and parsing string and another is for setting up UI layout and last one is for setting button signal and slots to use context free grammar interpreter. The below code is developed in Python language.

## Demo

![image](https://user-images.githubusercontent.com/52568892/100826096-37d0e680-341f-11eb-92aa-b8d6cf691d08.png)

![image](https://user-images.githubusercontent.com/52568892/100826127-4a4b2000-341f-11eb-8cc0-f2ea453bcd37.png)

## Presentation on Youtube 

[![Watch the video](https://user-images.githubusercontent.com/52568892/100825965-ef192d80-341e-11eb-973f-34c30d43d3d7.PNG)](https://www.youtube.com/watch?v=u1nfMwuLPKw&feature=youtu.be)

## Example

### Context Free Grammar

- S → aaaaS|A|B|C  
- S → D|E|ɛ 
- A → m|AC  
- A → aB|c|D  
- A → aa 
- B → ae|BE|ɛ|azz  
- B → Cd  
- C → i|D   
- C →  u|ɛ|o   
- D → n|E|t|at   
- D → y|ɛ  
- E → j|r|D|F  
- E → CBF  
- F → lolF|h|g   
- F → d|kkk  

### Derivation Trees

#### Strings are accepted by grammar: 

-	minji

![image](https://user-images.githubusercontent.com/52568892/101060045-9186fd00-3554-11eb-885f-7f3c10f24fb2.png)
![image](https://user-images.githubusercontent.com/52568892/101060080-9cda2880-3554-11eb-8653-0473088e35f2.png)

#### Strings are not accepted by grammar: 

-	car: The grammar cannot produce ‘ar’

![image](https://user-images.githubusercontent.com/52568892/101060396-fe01fc00-3554-11eb-9091-4f84360ba358.png)


## Built with

- [Python 3.7](https://www.python.org/)

- [PyQt5](https://pypi.org/project/PyQt5/)

## License

This project is licensed under the [MIT](https://github.com/minji-mia/CFGI-Interpreter-GUI/blob/main/LICENSE) License
