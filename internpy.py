input_string = "7o*W1CNwGJp4]|=hWxCzavcmxp3$qx[[k/>4/qDKP]k4RBsg%1w1}3nN~`JCEYpr^w&p*Y1v*=H`7$fewcEp`$,~%e.f}r<m3mky%6{gW:~ewjVhT};</wnfk+c_>M)OG&SLp,ht!GG]jC>OPN+w%09S,w3PIy^(0bia>mWWb/9kl^$+zDxp]],NO.ypt+tDAsJ^3QW6eQ4.M5d-0|19).w<x>4sC2BMq*KcecJkR40VGJ6Bs-(1CLU.MX{}%a`pTQuey$!mCP(R-3M{s3;_aq1~.K/tb}UFPd5&04>BXx~ETR3d/)~p49DkXjgt,Q{,qr$4%;%?<`pRyfJdL]:sd{v1OeK?UQ:+])2C[NNlZd[m4Oq{%QA2=6Q,(eoA9&(2Af>{ZNM]|A_14s^&i_iN3g45Pbi9%jwt=*!*7Em>=X|A+f`6mR*%A%-EE(RR1zv0wr.Ib$nI95PZkVWhV^pfU8%!v=8,_n{{H6I|}/b.^x)NR<>g4]~_S/_6owO9cZ<i!4Jb<tO&;3lGbNRzF^4,/6-R,t:S-QG;StX!LTobSEO2_zn4TK~Jq=bSz}Q3J${RS+$p)ot*&S!:7p7+V^oxfO%A:xW5cY)1.InjDXZUHk3SJQ[?^y}q+><MbrXURY=w&x}6A8jr>WffnfQ.()>FvdP6p~6_XWW^~oZ+94eXH1LrTQc>3DtI9G}]qUr~e3K|A`11NEw4<)T4~NW?JG5-cJ(gp?~U&gbW;ijc=e4}6t,fjDmSC75qywrf^;`/Biv^I%ahP(kfW)l3pisSe*6NR!7xFKluRnPOT7&[3(ElrQ3fz?&d*xOF}+F&I:u0HG(7uapRL2s&,D]cj/j6J(Lan(B0KtDnM:Pd8PIQ?z$Zxl0h-b+GOzEb$4qizp3.GBJXN^g=mLn(mgJM?1X%I(7so-A?SkZ?4s$Mlz}+e5$d4l?:t<v)y`a2?9CDyU=&{c+nY*4ZqYXH){E,s|a5$Ye)UsFpOzg/y+%S8i:AI}Ka"

output_string = ""
no_of_caps = 0

for x in input_string:
	if(x.isalpha()):
		output_string += x
		if(x.isupper()):
			no_of_caps = no_of_caps + 1
	
	if(x.isdigit()):
		temp = int(x)
		temp = temp - 3
		if(temp < 0):
			temp *= -1
		output_string += str(temp)
x = 0
while x < no_of_caps:
	output_string += '!'
	x = x + 1

print output_string;