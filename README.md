# CFGI-Interpreter-GUI

The project is for a context-free grammar interpreter. The interpreter takes as input a context-free grammar and a string to parse and gives an output whether the test string is either accepted or rejected. The program is implemented in a GUI, using Python.

## Program

My program consists of three files. One is for setting context free grammar and parsing string and another is for setting up UI layout and last one is for setting button signal and slots to use context free grammar interpreter. The below code is developed in Python language.

## Demo

![image](https://user-images.githubusercontent.com/52568892/100826096-37d0e680-341f-11eb-92aa-b8d6cf691d08.png)

![image](https://user-images.githubusercontent.com/52568892/100826127-4a4b2000-341f-11eb-8cc0-f2ea453bcd37.png)

## Presentation on Youtube [![youtube](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Youtube2_colored_svg-256.png)](https://www.youtube.com/watch?v=u1nfMwuLPKw&feature=youtu.be)
[![Watch the video](https://user-images.githubusercontent.com/52568892/100825965-ef192d80-341e-11eb-973f-34c30d43d3d7.PNG)](https://www.youtube.com/watch?v=u1nfMwuLPKw&feature=youtu.be)

## Context Free Grammar
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

## Derivation Trees

Strings are accepted by grammar: 

## License
[MIT](https://github.com/minji-mia/CFGI-Interpreter-GUI/blob/main/LICENSE)
