#!/usr/bin/python
#coding: utf-8 
#19/03/2022
#ph.limma
#Script para formatação de dados de um lista de resultados da CEBRASPE

import PyPDF2 #biblioteca para tratar o PDF

pdfobj=open('resultado-final-petrobras.pdf','rb')
pdfread=PyPDF2.PdfFileReader(pdfobj) #passando os dados para o PyPDF
x=pdfread.numPages #numero de páginas do PDF
texto=str()
for page in range(x):
    pageobj2=pdfread.getPage(page-1) 
    text=pageobj2.extractText()
    text=text.replace(text.split('\n', 1)[0], '') #tira os números de página
    text=text.replace('\n', '') #retira quebras de linha
    texto=texto+text 
    print(page)

#aplica algum tratamento prévio aos dados colhidos
texto=texto.replace('/', '\n')
texto=texto.replace(' AC ', '\n')
texto=texto.replace('Resultado de aprovados final nas provas objetivas dos candidatos que ', '')
texto=texto.replace(', na seguinte ordem: número de inscrição, nome do candidato em ordem alfabética, nota final na prova objetiva de conhecimentos básicos (P1), número de acertos na prova objetiva de conhecimentos básicos (P1), nota final na prova objetiva de conhecimentos específicos (P2), número de acertos na prova objetiva de conhecimentos específicos (P2), nota final no bloco 1 da prova objetiva de conhecimentos específicos (P2), nota final no bloco 2 da prova objetiva de conhecimentos específicos (P2), nota final no bloco 3 da prova objetiva de conhecimentos específicos (P2) e nota final nas provas objetivas.', '\n')
texto=texto.replace('Resultado final de aprovados nas provas objetivas dos candidatos que solicitaram concorrer como pessoas com deficiência, na seguinte ordem: número de inscrição, nome do candidato em ordem alfabética, nota final na prova objetiva de conhecimentos básicos (P), número de acertos na prova objetiva de conhecimentos básicos (P), nota final na prova objetiva de conhecimentos específicos (P2), número de acertos na prova objetiva de conhecimentos específicos (P2), nota final no bloco  da prova objetiva de conhecimentos específicos (P2), nota final no bloco 2 da prova objetiva de conhecimentos específicos (P2), nota final no bloco 3 da prova objetiva de conhecimentos específicos (P2) e nota final nas provas objetivas.', '\n')
texto=texto.replace('Resultado final de aprovados nas provas objetivas dos candidatos que solicitaram concorrer como pessoas com deficiência, na seguinte ordem: número de inscrição, nome do candidato em ordem alfabética, nota final na prova objetiva de conhecimentos básicos (P1), número de acertos na prova objetiva de conhecimentos básicos (P1), nota final na prova objetiva de conhecimentos específicos (P2), número de acertos na prova objetiva de conhecimentos específicos (P2), nota final no bloco 1 da prova objetiva   de conhecimentos específicos (P2), nota final no bloco 2 da prova objetiva de conhecimentos específicos (P2), nota final no bloco 3 da prova objetiva de conhecimentos específicos (P2) e nota final nas provas objetivas.', '\n')
texto=texto.replace('Resultado final de aprovados nas provas objetivas dos candidatos que solicitaram concorrer como pessoas com deficiência, na seguinte ordem: número de inscrição, nome do candidato em ordem alfabética, nota final na prova objetiva de conhecimentos   básicos (P1), número de acertos na prova objetiva de conhecimentos básicos (P1), nota final na prova objetiva de conhecimentos específicos (P2), número de acertos na prova objetiva de conhecimentos específicos (P2), nota final no bloco 1 da prova objetiva de conhecimentos específicos (P2), nota no bloco 2 da prova objetiva de conhecimentos específicos (P2) e nota final nas provas objetivas.', '\n')
texto=texto.replace('Resultado final de aprovados nas provas objetivas dos candidatos que se autodeclararam negros, na seguinte ordem: número de inscrição, nome do candidato em ordem alfabética, nota final na prova objetiva de conhecimentos básicos (P1), número de acertos na prova objetiva de conhecimentos básicos (P1), nota final na prova objetiva de conhecimentos específicos (P2), número de acertos na prova objetiva de conhecimentos específicos (P2), nota final no bloco 1 da prova objetiva de conhecimentos   específicos (P2), nota final no bloco 2 da prova objetiva de conhecimentos específicos (P2), nota final no bloco 3 da prova objetiva de conhecimentos específicos (P2) e nota final nas provas objetivas.', '\n')
texto=texto.replace('Resultado final de aprovados nas provas objetivas e convocação para a avaliação de títulos, na seguinte ordem: número de inscrição, nome do candidato em ordem alfabética, nota final na prova objetiva de conhecimentos básicos (P1), número de acertos na prova objetiva de conhecimentos básicos (P1), nota final na prova objetiva de conhecimentos específicos (P2), número de acertos na prova objetiva de conhecimentos específicos (P2), nota final no bloco 1 da prova objetiva de conhecimentos específicos   (P2), nota final no bloco 2 da prova objetiva de conhecimentos específicos (P2), nota final no bloco 3 da prova objetiva de conhecimentos específicos (P2) e nota final nas provas objetivas.', '\n')
texto=texto.replace('Resultado final de aprovados nas provas objetivas dos candidatos que se autodeclararam negros, na seguinte ordem: número de inscrição, nome do candidato em ordem alfabética, nota final na prova objetiva de conhecimentos básicos (P), número de acertos na prova objetiva de conhecimentos básicos (P), nota final na prova objetiva de conhecimentos específicos (P2), número de acertos na prova objetiva de conhecimentos específicos (P2), nota final no bloco  da prova objetiva de conhecimentos específicos (P2), nota final no bloco 2 da prova objetiva de conhecimentos específicos (P2), nota final no bloco 3 da prova objetiva de conhecimentos específicos (P2) e nota final nas provas objetivas.', '\n')
texto=texto.replace('ÊNFASE', '\nÊNFASE') #separa por ênfase

texto=texto.split('\n') #cria uma lista com o conteúdo de todas as linhas
del texto[0:14] #remove as 14 primeiras linhas
del texto[(len(texto)-7):len(texto)] #remove as sete últimas linhas
texto='\n'.join(map(str, texto))#convertendo de volta a lista para string

arq=open(r"resultado-final-petrobras.txt","a") #salva o conteudo final
arq.writelines(texto)
arq.close()
