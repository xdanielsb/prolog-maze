ir([Salidax, Saliday], [Destinox,Destinoy],R):-
	ir0([Salidax, Saliday], [Destinox,Destinoy],[],R).
ir0([Dx,Dy],[Dx,Dy],T,[[Dx,Dy]|T]).
ir0([Sx,Sy],[Dx,Dy],T,R):-
	nodolegal([Sx,Sy],T,[Sigx,Sigy]),
	ir0([Sigx,Sigy],[Dx,Dy],[[Sx,Sy]|T],R).
nodolegal([Sx,Sy],Camino,[Sigx,Sigy]):-(calle(Sx,Sy,Sigx,Sigy);	calle(Sigx,Sigy,Sx,Sy)),\+ member([Sigx,Sigy],Camino).
