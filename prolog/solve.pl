calle('0','4','0','3').
calle('0','2','0','1').
calle('1','3','0','3').
calle('2','0','3','0').
calle('3','0','4','0').
calle('4','3','4','4').
calle('4','2','4','3').
calle('0','0','1','0').
calle('3','4','2','4').
calle('1','0','2','0').
calle('2','2','2','3').
calle('0','1','0','0').
calle('0','3','0','2').
calle('2','3','2','4').
calle('1','4','0','4').
calle('2','4','1','4').
calle('1','2','2','2').
calle('4','0','4','1').
calle('0','2','1','2').
calle('4','1','4','2').
calle('1','3','1','2').
calle('2','3','1','3').
calle('1','3','1','4').
ir([Salidax, Saliday], [Destinox,Destinoy],R):-
	ir0([Salidax, Saliday], [Destinox,Destinoy],[],R).
ir0([Dx,Dy],[Dx,Dy],T,[[Dx,Dy]|T]).
ir0([Sx,Sy],[Dx,Dy],T,R):-
	nodolegal([Sx,Sy],T,[Sigx,Sigy]),
	ir0([Sigx,Sigy],[Dx,Dy],[[Sx,Sy]|T],R).
nodolegal([Sx,Sy],Camino,[Sigx,Sigy]):-(calle(Sx,Sy,Sigx,Sigy);	calle(Sigx,Sigy,Sx,Sy)),\+ member([Sigx,Sigy],Camino).
