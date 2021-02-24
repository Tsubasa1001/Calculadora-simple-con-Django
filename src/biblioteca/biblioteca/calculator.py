#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
"""
    ====================================================================
     Title:         Simple Calculator with Prefix and Postfix Expression
     Developed by:  Gustavo L. Franco Moron
     Date:          August 31th, 2017
    ====================================================================
"""

import pdb

# Stack Class------------------------------------------------------------------
class Stack:
    def __init__(self):
        self.items=[]
    
    def Empty(self):
        if len(self.items)==0:
            return True
        return False
    
    def Push(self, value):
        self.items.append(value)
        
    def Pop(self):
        if len(self.items)==0:
            return
        value=self.items.pop()
        return value
        
    def TopS(self):
        l = len(self.items)
        if l==0:
            return
        return self.items[l-1]

# TreeNode Class for the Tree Class--------------------------------------------
class TreeNode:
    
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

# Tree Class-------------------------------------------------------------------
class Tree:
    
    #Class Constructor, No parameters
    def __init__(self):
        self.root = None
    
    #Add Node Method, using TreeNode Class
    def addchar(self, char):
        self.root = TreeNode(char)
        
    def addExp(self, OpNode, RightNode, LeftNode):
        self.root = OpNode
        OpNode.left = LeftNode
        OpNode.right = RightNode
        
    def printPostOrder(self, node):
        if(node==None):
            return
        self.printPostOrder(node.left)
        self.printPostOrder(node.right)
        print(node.data)

    def getPostOrder(self, node):
        cad = ""
        if(node==None):
            return cad
        cad = cad + str(self.getPostOrder(node.left)) + " "
        cad = cad + str(self.getPostOrder(node.right)) + " "
        cad = cad + str(node.data) + " "
        return cad
        
    def Calculate(self, node):
        if(node==None):
            return
        a = self.Calculate(node.left)
        b = self.Calculate(node.right)
        if not (isOperator(node.data)):
            return node.data
        else:
            if (node.data == '*'):
                return float(a)*float(b)
            if (node.data == '/'):
                return float(a)/float(b)
            if (node.data == '+'):
                return float(a)+float(b)
            if (node.data == '-'):
                return float(a)-float(b)
            if (node.data == '^'):
                return float(a)**float(b)
            
#----------------------------------------------------------------------------
#---------------------------------------------------------------------------- 
#Global Functions for main function and Stack and Tree Classes

#It checks if (char) is a Operator or not    
def isOperator(char):
    i = 0
    c ="^*/+-()"
    while i<len(c):
        if char==c[i]:
            return True
        i=i+1
    return False

#Postfix Operators Priority Table from Expression  
def ExpPriority(data):
    if data == '^':
        return 4
    if data == '*' or data == '/':
        return 2
    if data == '+' or data == '-':
        return 1
    if data == '(':
        return 5

#Postfix Operators Priority Table from Stack       
def StackPriority(data):
    if data == '^':
        return 3
    if data == '*' or data == '/':
        return 2
    if data == '+' or data == '-':
        return 1
    if data == '(':
        return 0

#Prefix Operators Priority Table from Expression      
def ExpPriority2(data):
    if data == '^':
        return 4
    if data == '*' or data == '/':
        return 2
    if data == '+' or data == '-':
        return 1
    if data == ')':
        return 5

#Prefix Operators Priority Table from Stack      
def StackPriority2(data):
    if data == '^':
        return 3
    if data == '*' or data == '/':
        return 2
    if data == '+' or data == '-':
        return 1
    if data == ')':
        return 0
#----------------------------------------------------------------------------  
#Check for Parenthesis Correct Order
def parenthesis(Text):
    Stack0 = Stack()
    fullp = True
    op= 0
    clo= 0
    count=0
    while count<len(Text):
        if (Text[count]=='('):
            Stack0.Push('(')
            fullp = False
            op = op + 1
        if (Text[count]==')'):
            clo = clo + 1
            if not (Stack0.Empty()):
                Stack0.Pop()
        count=count+1
    if ((op==0) and (clo == 0)):
        return True
    if (op == clo):
        if (Stack0.Empty()):
            if not fullp:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
#----------------------------------------------------------------------------
#Function to Convert infix Expression to Prefix, it returns the result as String var.
def InfixToPrefix(Text):
    EStack = Stack()
    count=len(Text)-1
    Prefix=""
    a=''
    while (count>=0):
        if not isOperator(Text[count]):
            Prefix =  Prefix + Text[count]
            if (count>0):
                if (Text[count-1]==')'):
                    if ExpPriority2('*') > StackPriority2(EStack.TopS()):
                        EStack.Push('*')
                        Prefix = Prefix + ' '
                    else:
                        while not (EStack.Empty()) and not (EStack.TopS()==')'):
                            a=EStack.Pop()
                            Prefix = Prefix + ' ' + a + ' '
                        EStack.Push('*')
        else:
            if not Text[count]=='(':
                Prefix = Prefix + ' '
            if Text[count]=='(':
                while not ( EStack.TopS()==')' ):
                    a=EStack.Pop()
                    Prefix = Prefix + ' ' + a
                a=EStack.Pop()
                if (count>0):
                    if not isOperator(Text[count-1]):
                        if ExpPriority2('*') > StackPriority2(EStack.TopS()):
                            EStack.Push('*')
                            Prefix = Prefix + ' '
                        else:
                            while not (EStack.Empty()) and not (EStack.TopS()==')'):
                                a=EStack.Pop()
                                Prefix = Prefix + ' ' + a + ' '
                            EStack.Push('*')
            else:
                if EStack.Empty():
                    EStack.Push(Text[count])
                else:
                    if ExpPriority2(Text[count]) > StackPriority2(EStack.TopS()):
                        EStack.Push(Text[count])
                    else:
                        while not (EStack.Empty()) and not (EStack.TopS()==')'):
                            a=EStack.Pop()
                            Prefix = Prefix + ' ' + a + ' '
                        EStack.Push(Text[count])
        count=count-1
    while not EStack.Empty():
        a=EStack.Pop()
        Prefix = Prefix + ' ' + a + ' '
    Prefix2=""
    for h in Prefix:
        Prefix2=h+Prefix2
    return Prefix2

#----------------------------------------------------------------------------
#Function to Convert infix Expression to Postfix, it returns the result as String var.
def InfixToPostfix(Text):
    EStack = Stack()
    count=0
    Postfix=""
    a=''
    while count<len(Text):
        if not isOperator(Text[count]):
            Postfix = Postfix + Text[count]
            if (count<len(Text)-1):
                if (Text[count+1]=='('):
                    if ExpPriority('*') > StackPriority(EStack.TopS()):
                        EStack.Push('*')
                        Postfix = Postfix + ' '
                    else:
                        while not (EStack.Empty()) and not (EStack.TopS()=='('):
                            a=EStack.Pop()
                            Postfix = Postfix + ' ' + a + ' '
                        EStack.Push('*')
        else:
            if not (Text[count]=='('or Text[count]==')'):
                Postfix = Postfix + ' '
            if Text[count]==')':
                while not ( EStack.TopS()=='(' ):
                    a=EStack.Pop()
                    Postfix = Postfix + ' ' + a + ' '
                a=EStack.Pop()
                if (count<len(Text)-1):
                    if not isOperator(Text[count+1]):
                        if ExpPriority('*') > StackPriority(EStack.TopS()):
                            EStack.Push('*')
                            Postfix = Postfix + ' '
                        else:
                            while not (EStack.Empty()) and not (EStack.TopS()=='('):
                                a=EStack.Pop()
                                Postfix = Postfix + ' ' + a + ' '
                            EStack.Push('*')
            else:
                if EStack.Empty():
                    EStack.Push(Text[count])
                else:
                    if ExpPriority(Text[count]) > StackPriority(EStack.TopS()):
                        EStack.Push(Text[count])
                    else:
                        while not (EStack.Empty()) and not (EStack.TopS()=='('):
                            a=EStack.Pop()
                            Postfix = Postfix + ' ' + a + ' '
                        EStack.Push(Text[count])
        count=count+1
    while not EStack.Empty():
        a=EStack.Pop()
        Postfix = Postfix + ' ' + a + ' '
    return Postfix

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------    

def main_tree(cad):
    # print ("======Welcome to Infix - Postfix Expressions======")
    # cad=input('Enter a Arithmetic Epxression: ')
    if (parenthesis(cad)):
        newcad = InfixToPostfix(cad)
        nc = " ".join(newcad.split())
        newcad2 = InfixToPrefix(cad)
        nc2 = " ".join(newcad2.split())
        if not (newcad==""):
            # print ("Postfix Expression")
            # print (nc)
            # print ("Prefix Expression")
            # print (nc2)
            # print ("=================================================\nBinary Tree in PostOrder")
            Stk = Stack()
            c=0
            number = 0
            num = 0
            while c<len(nc):                        #Process to create Binary Tree of Postfix expression
                if nc[c]==' ':
                    c = c + 1
                if not isOperator(nc[c]):
                    if (c<len(nc)-1):
                        num = int(nc[c])
                        number = number * 10 + num
                        if nc[c+1]==' ':
                            ExpTree2 = Tree()
                            ExpTree2.addchar(number)
                            Stk.Push(ExpTree2.root)
                            number = 0
                else:
                    ExpTree3 = Tree()
                    ExpTree = Tree()
                    ExpTree.addchar(nc[c])
                    ExpTree3.root=Stk.Pop()
                    ExpTree2.root=Stk.Pop()
                    ExpTree.addExp(ExpTree.root, ExpTree3.root, ExpTree2.root)
                    Stk.Push(ExpTree.root)
                c=c+1
            return ExpTree.getPostOrder(ExpTree.root)        #Print Binary Tree in PostOrder
            # print ("=================================================\nResult")
            # print (ExpTree.Calculate(ExpTree.root))       #Print the final result of arithmetic expression introduced
    
# if __name__ == "__main__":
#     main()