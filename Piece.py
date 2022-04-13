def Piece(Base, Delimitador, nPos):
  # Base (Texto ao qual será selecionado o pedaço)
  # Delimitador (Caractere [ou texto] que compreende o pedaço de texto)
  # nPos (Posição do pedaço que se pretende)
  #
  # Exemplo: Piece("alunos.livre^utfpr^software^^trabalho^desenvolvimento", "^", 2)   ===> 'utfpr'
  #          Piece("alunos.livre^utfpr^software^^trabalho^desenvolvimento", "^", 4)   ===> ''
  #          Piece("alunos.livre^utfpr^software^^trabalho^desenvolvimento", "^", 5)   ===> 'trabalho'
  #          Piece("alunos.livre^utfpr^software^^trabalho^desenvolvimento", ".", 1)   ===> 'alunos'
  #          Piece("alunos.livre^utfpr^software^^trabalho^desenvolvimento", ".", 2)   ===> 'livre^utfpr^software^^trabalho^desenvolvimento'
  #
  if Base == "" or nPos == 0:
    return
  xEnd = Base.find(Delimitador)
  if xEnd == 0 and nPos == 1:
    return Base
  if xEnd == -1:
    exit
  if nPos == 1: 
    return Base[0:xEnd]
  yBeg = 1
  iCount = 2
  while iCount <= nPos:
     yBeg = Base.find(Delimitador,yBeg + 1)
     if yBeg == -1:
       break
     yBeg += len(Delimitador)
     xEnd = Base.find(Delimitador,yBeg + 1)
     iCount += 1
  if xEnd == -1 and yBeg == -1:
    return
  if xEnd == -1:
    xEnd = len(Base) + 1 + len(Delimitador)     
  return Base[yBeg:xEnd]