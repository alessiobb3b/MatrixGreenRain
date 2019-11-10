#! /usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import print_function
from random import randint
from time import sleep
def Randomz():
 Chars =   ['0','1','2','3','4','5','6','7','8','9','｡','｢','｣','､','･','ｦ','ｧ','ｨ','ｩ','ｪ','ｫ','ｬ','ｭ','ｮ','ｯ','ｰ','ｱ','ｲ','ｳ','ｴ','ｵ','ｶ','ｷ','ｸ','ｹ','ｺ','ｻ','ｼ','ｽ','ｾ','ｿ','ﾀ','ﾁ','ﾂ','ﾃ','ﾄ','ﾅ','ﾆ','ﾇ','ﾈ','ﾉ','ﾊ','ﾋ','ﾌ','ﾍ','ﾎ','ﾏ','ﾐ','ﾑ','ﾒ','ﾓ','ﾔ','ﾕ','ﾖ','ﾗ','ﾘ','ﾙ','ﾚ','ﾛ','ﾜ','ﾝﾞﾟ', ' ']
 i = (randint(0,len(Chars)-1))
 return i
def Calcu():
 m = (randint(0,3))
 return m

def Color():
 j = (randint(0,100))
 if ( j <= 98):
   j = 0
 elif (j == 99):
   j = 1
 elif (j == 100):
   j = 2 
 return j

def Function():
 intro = ["\033[1;32m","","\033[1;42m"]
 outro = "\033[1;m"
 Chars =   ['0','1','2','3','4','5','6','7','8','9','｡','｢','｣','､','･','ｦ','ｧ','ｨ','ｩ','ｪ','ｫ','ｬ','ｭ','ｮ','ｯ','ｰ','ｱ','ｲ','ｳ','ｴ','ｵ','ｶ','ｷ','ｸ','ｹ','ｺ','ｻ','ｼ','ｽ','ｾ','ｿ','ﾀ','ﾁ','ﾂ','ﾃ','ﾄ','ﾅ','ﾆ','ﾇ','ﾈ','ﾉ','ﾊ','ﾋ','ﾌ','ﾍ','ﾎ','ﾏ','ﾐ','ﾑ','ﾒ','ﾓ','ﾔ','ﾕ','ﾖ','ﾗ','ﾘ','ﾙ','ﾚ','ﾛ','ﾜ','ﾝﾞﾟ', ' ']
 k = 0
 l = 0
 while (k < 68 and l <= 30):
  A = int(Randomz())
  sleep(0.1)
  j = int(Color())
  q = int(Color())
  w = int(Color())
  e = int(Color())
  if (intro == ""):
   outro = ""
  Z = (intro[j] + Chars[A]  + outro + " ")
  B = int(Randomz())
  X = (intro[q] + Chars[B]  + outro + " ")
  C = int(Randomz())
  V = (intro[w] + Chars[C]  + outro + " ")
  D = int(Randomz())
  N = (intro[e] + Chars[D]  + outro + " ")
  M = int(Randomz())
  lista = [Z,X,V,N]
  m = int(Calcu())
  n = int(Calcu())
  o = int(Calcu())
  p = int(Calcu())
  NZ = lista[m] + lista[n] + lista[o] + lista[p]
  print NZ *10
  k = k+1
  if (k == 67):
   k = 0
   l = l+1

Function()

