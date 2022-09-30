import re;
import unidecode;

with open('filme-1628_comentarios.txt') as arquivoTeste:
    comentarios = arquivoTeste.read().lower();
    comentarios = unidecode.unidecode(comentarios)

def comentariosPositivos(comentarios):
    totpositivos = 0;

    x = re.findall(r"filme (excelente|magnifico|sensacional|perfeito|espetacular|fantastico|impecavel|extraordinario)",comentarios)
    totpositivos = totpositivos+x.__len__();

    x = re.findall(r"otim(o|a)(s)? (filme|trilha sonora|atuac|atuaç|roteiro|trama|direc|direç|fotografia|musica|arte|cg)",comentarios)
    totpositivos = totpositivos+x.__len__();

    x = re.findall(r"excelente(s)? (filme|trilha sonora|atuac|atuaç|roteiro|trama|direc|direç|fotografia|musica|arte|cg)",comentarios)
    totpositivos = totpositivos+x.__len__();

    x = re.findall(r"(otimo|excelente|melhor) filme",comentarios)
    totpositivos = totpositivos+x.__len__();

    x = re.findall(r"muito bom",comentarios)
    totpositivos = totpositivos+x.__len__();

    x = re.findall(r"curti muito",comentarios)
    totpositivos = totpositivos+x.__len__();

    x = re.findall(r"muito interessante",comentarios)
    totpositivos = totpositivos+x.__len__();

    x = re.findall(r"obra prima",comentarios)
    totpositivos = totpositivos+x.__len__();

    x = re.findall(r"vale a pena",comentarios)
    totpositivos = totpositivos+x.__len__();

    x = re.findall(r"história prende",comentarios)
    totpositivos = totpositivos+x.__len__();

    return totpositivos;

def comentariosNegativos(comentarios):
    totNegativos = 0;

    y = re.findall(r"(pior(es)?) (filme|trilha sonora|atuac|atuaç|roteiro|trama|direc|direç|fotografia|musica|arte|cg)",comentarios)
    totNegativos = totNegativos + y.__len__();

    y = re.findall(r"(pessim(o|a))(s)? (filme|trilha sonora|atuac|atuaç|roteiro|trama|direc|direç|fotografia|musica|arte|cg)",comentarios)
    totNegativos = totNegativos + y.__len__();

    y = re.findall(r"filme (muito )?(ruim|horrivel|chato|maçante|cansativo|ridiculo|sem gra|sem sentido|pessimo|lixo|mal feito|incoerente|confuso|exagerado|fraco)",comentarios)
    totNegativos = totNegativos + y.__len__();

    y = re.findall(r"não percam tempo",comentarios)
    totNegativos = totNegativos + y.__len__();

    y = re.findall(r"muito ruim",comentarios)
    totNegativos = totNegativos + y.__len__();

    y = re.findall(r"dormi",comentarios)
    totNegativos = totNegativos + y.__len__();

    y = re.findall(r"filme chato",comentarios)
    totNegativos = totNegativos + y.__len__();

    y = re.findall(r"sem graça",comentarios)
    totNegativos = totNegativos + y.__len__();

    y = re.findall(r"muito fraco",comentarios)
    totNegativos = totNegativos + y.__len__();

    y = re.findall(r"não (recomendo|gostei)",comentarios)
    totNegativos = totNegativos + y.__len__();

    y = re.findall(r"sem sentido",comentarios)
    totNegativos = totNegativos + y.__len__();

    return totNegativos;

def filtrarComentarios(comentarios):    

    totPositivos = comentariosPositivos(comentarios);

    totNegativos = comentariosNegativos(comentarios);

    cacularEstrelas(totPositivos, totNegativos);

def cacularEstrelas(positivos, negativos):
    pontos = 50;

    if(positivos != 0):
        valorDeCadaCriticaOuElogio = 50/positivos;
    else:
        valorDeCadaCriticaOuElogio = 50/negativos;


    pontos = pontos + (positivos*valorDeCadaCriticaOuElogio - negativos*valorDeCadaCriticaOuElogio);

    estrelas = pontos/100;

    print("O filme foi classificado como",5*estrelas,"estrelas");

filtrarComentarios(comentarios);


   