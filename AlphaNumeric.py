def Chart():
  for i in range(len(str)):
    if str[i]=="A":
      chr_A=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if ((col==0 or col==6) and (row!=0 and row!=1 and row!=2)) or ((row==4) and (col>0 and col<6)) or (row+col==3) or (col-row==3):
            chr_A[row][col]="#"
      l1.append(chr_A)
    elif str[i]=="B":
      chr_B=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if(col==0) or (col==4 and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):
            chr_B[row][col]="#"
      l1.append(chr_B)
    elif str[i]=="C":
      chr_C=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==0 and (row!=0 and row!=6)) or ((row==0 or row==6)and col>0):
            chr_C[row][col]="#"
      l1.append(chr_C)
    elif str[i]=="D":
      chr_D=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if(col==0) or (col==5 and (row!=6 and row!=0)) or ((row==0 or row==6) and (col>0 and col<5)):
            chr_D[row][col]="#"
      l1.append(chr_D)
    elif str[i]=="E":
      chr_E=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if(row==0 or row==3 or row==6) or (col==0 and (row!=0 or row!=2 or row!=5)):
            chr_E[row][col]="#"
      l1.append(chr_E)
    elif str[i]=="F":
      chr_F=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==0 and row!=0) or ((row==0 or row==3) and (col!=0 and col!=5 and col!=6)):
            chr_F[row][col]="#"
      l1.append(chr_F)
    elif str[i]=="G":
      chr_G=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==0 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col!=5 and col!=0 and col!=6)) or (row==3 and (col<6 and col>1)) or (col==5 and (row!=0 and row!=2 and row!=3 and row!=6)):
            chr_G[row][col]="#"
      l1.append(chr_G)
    elif str[i]=="H":
      chr_H=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
         if (col==0 or col==5) or ((row==3) and (col!=0 and col!=5 and col!=6)):
            chr_H[row][col]="#"
      l1.append(chr_H)
    elif str[i]=="I":
      chr_I=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if ((row==0 or row==6) and (col!=0 and col!=6)) or (col==3 and (row!=0 and row!=6)):
            chr_I[row][col]="#"
      l1.append(chr_I)
    elif str[i]=="J":
      chr_J=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==3 and row!=6) or (row==0 and col!=3) or (row==5 and col<1) or (row==6 and (col>0 and col<3)):
            chr_J[row][col]="#"
      l1.append(chr_J)
    elif str[i]=="K":
      chr_K=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if col==0 or (row==3 and (col>0 and col<2)) or (col==2 and (row!=0 and row!=1 and row!=3 and row!=5 and row!=6)) or (col==3 and (row!=0 and row!=2 and row!=3 and row!=4 and row!=6)) or (col==4 and (row!=2 and row!=1 and row!=3 and row!=5 and row!=4)) :
            chr_K[row][col]="#"
      l1.append(chr_K)
    elif str[i]=="L":
      chr_L=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if(col==0) or (row==6 and col>0):
            chr_L[row][col]="#"
      l1.append(chr_L)
    elif str[i]=="M":
      chr_M=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==0 or col==6) or (row==1 and (col!=0 and col!=2 and col!=3 and col!=4 and col!=6)) or (row==2 and (col!=0 and col!=1 and col!=3 and col!=5 and col!=6)) or (row==3 and (col!=0 and col!=1 and col!=2 and col!=4 and col!=5 and col!=6)):
            chr_M[row][col]="#"
      l1.append(chr_M)
    elif str[i]=="N":
      chr_N=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if col==0 or col==6 or (row==col and (col>0 and col<6)):
            chr_N[row][col]="#"
      l1.append(chr_N)
    elif str[i]=="O":
      chr_O=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if ((col==0 or col==6) and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<6)):
            chr_O[row][col]="#"
      l1.append(chr_O)
    elif str[i]=="P":
      chr_P=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col == 0) or ((row == 0 or row == 3) and (col != 0 and col != 5 and col != 6)) or (col == 5 and (row > 0 and row < 3)):
            chr_P[row][col]="#"
      l1.append(chr_P)
    elif str[i]=="Q":
      chr_Q=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if ((col==0 or col==4) and (row!=0 and row!=6)) or (row==6 and (col!=0 and col!=4 and col!=5)) or (row==4 and (col>2 and col<4)) or ((row==0) and (col>0 and col<4)) or (col==5 and (row>3 and row<5)) or (col==6 and (row>4 and row<6)):
            chr_Q[row][col]="#"
      l1.append(chr_Q)
    elif str[i]=="R":
      chr_R=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if col==0 or (col==4 and(row!=0 and row!=3)) or ((row==0 or row==3) and (col!=5 and col!=6 and col!=4)):
            chr_R[row][col]="#"
      l1.append(chr_R)
    elif str[i]=="S":
      chr_S=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (row==0 and (col>1 and col<5)) or ( row==6 and (col>0 and col<4)) or (row==1 and (col!=0 and col!=2 and col!=3 and col!=4 and col!=6)) or (row==5 and (col!=1 and col!=2 and col!=5 and col!=3 and col!=6)) or (row==2 and (col>1 and col<3)) or (row==3 and (col>2 and col<4)) or (row==4 and (col>3 and col<5)):
            chr_S[row][col]="#"
      l1.append(chr_S)
    elif str[i]=="T":
      chr_T=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==3) or (row==0 and col!=3):
            chr_T[row][col]="#"
      l1.append(chr_T)
    elif str[i]=="U":
      chr_U=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if((col==0 or col==6) and row!=6) or (row==6 and (col>0 and col<6)) :
            chr_U[row][col]="#"
      l1.append(chr_U)
    elif str[i]=="V":
      chr_V=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if((col==0 or col==4) and row<5) or (row==5 and (col!=0 and col!=2 and col!=4 and col!=5 and col!=6)) or (row==6 and (col>1 and col<3)):
            chr_V[row][col]="#"
      l1.append(chr_V)
    elif str[i]=="W":
      chr_W=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==0 or col==6) or (row==3 and (col!=0 and col!=2 and col!=1 and col!=5 and col!=4 and col!=6)) or (row==4 and (col!=0 and col!=1 and col!=3 and col!=5 and col!=6)) or (row==5 and (col!=0 and col!=3 and col!=2 and col!=4 and col!=6)):
            chr_W[row][col]="#"
      l1.append(chr_W)
    elif str[i]=="X":
      chr_X=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (row-col==0) or (row+col==6):
            chr_X[row][col]="#"
      l1.append(chr_X)
    elif str[i]=="Y":
      chr_Y=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==3 and row>2) or (row==2 and (col!=0 and col!=1 and col!=3 and col!=5 and col!=6)) or (row==1 and (col!=0 and col!=2 and col!=3 and col!=4 and col!=6)) or (row==0 and (col!=2 and col!=1 and col!=3 and col!=5 and col!=4)) :
            chr_Y[row][col]="#"
      l1.append(chr_Y)
    elif str[i]=="Z":
      chr_Z=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (row==0 or row==6) or ((col+row==6) and (row>0 and row<6)):
            chr_Z[row][col]="#"
      l1.append(chr_Z)
    elif str[i]=="a":
      chr_a=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==5 and (row!=1 and row!=0)) or ((row==3 or row==5) and (col!=0 and col!=6 and col!=1)) or (col==1 and (row!=0 and row!=1 and row!=3 and row!=5 and row!=2 and row!=6)) or (row==1 and (col>1 and col<5)):
            chr_a[row][col]="#"
      l1.append(chr_a)
    elif str[i]=="b":
      chr_b=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==2) or (col==3 and (row!=0 and row!=1 and row!=2 and row!=4 and row!=5)) or (col==4 and (row!=0 and row!=1 and row!=2 and row!=4 and row!=5)) or (col==5 and (row!=0 and row!=1 and row!=2 and row!=4 and row!=5)) or (col==6 and (row!=0 and row!=1 and row!=2 and row!=3 and row!=6)):
            chr_b[row][col]="#"
      l1.append(chr_b)
    elif str[i]=="c":
      chr_c=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==1 and (row!=0 and row!=1 and row!=6 and row!=2)) or ((row==2 or row==6) and (col>1 and col<5)):
            chr_c[row][col]="#"
      l1.append(chr_c)
    elif str[i]=="d":
      chr_d=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==4) or ((col==3 or col==2 or col==1) and (row!=0 and row!=1 and row!=2 and row!=4 and row!=5)) or (col==0 and (row!=0 and row!=1 and row!=2 and row!=3 and row!=6)):
            chr_d[row][col]="#"
      l1.append(chr_d)
    elif str[i]=="e":
      chr_e=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if ((row==6 or row==2) and (col!=0 and col!=1 and col!=6)) or (col==1 and (row>2 and row<6)) or (row==3 and (col!=0 and col!=1 and col!=3 and col!=4 and col!=2 and col!=6)) or (row==4 and (col!=0 and col!=1 and col!=2 and col!=5 and col!=6)) :
            chr_e[row][col]="#"
      l1.append(chr_e)
    elif str[i]=="f":
      chr_f=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==2) or (row==3 and ( col!=5 and col!=6)) or (row==0 and (col>2 and col<5)) or (col==5 and (row<2 and row>0)):
             chr_f[row][col]="#"
      l1.append(chr_f)
    elif str[i]=="g":
      chr_g=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==5 and (row!=6)) or ((row==0 or row==3 or row==6) and (col!=0 and col!=1 and col!=5 and col!=6)) or (col==1 and (row!=0 and row!=3 and row!=4 and row!=6)) :
            chr_g[row][col]="#"
      l1.append(chr_g)
    elif str[i]=="h":
      chr_h=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==1) or (row==3 and (col>1 and col<5)) or (col==5 and row>2):
            chr_h[row][col]="#"
      l1.append(chr_h)
    elif str[i]=="i":
      chr_i=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==3 and row!=1):
            chr_i[row][col]="#"
      l1.append(chr_i)
    elif str[i]=="j":
      chr_j=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==4 and (row!=1)) or (col==2 and row>5) or (col==1 and (row>4 and row<6)):
            chr_j[row][col]="#"
      l1.append(chr_j)
    elif str[i]=="k":
      chr_k=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==2) or (col==3 and (row>3 and row<5)) or (col==4 and (row!=0 and row!=1 and row!=2 and row!=4 and row!=6)) or (col==5 and (row!=0 and row!=1 and row!=3 and row!=4 and row!=5)):
            chr_k[row][col]="#"
      l1.append(chr_k)
    elif str[i]=="l":
      chr_l=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==3):
            chr_l[row][col]="#"
      l1.append(chr_l)
    elif str[i]=="m":
      chr_m=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==0 and (row!=0 and row!=1)) or (row==3 and (col!=3 and col!=0 and col!=6)) or (col==3 and (row>3)) or (col==6 and row>3):
            chr_m[row][col]="#"
      l1.append(chr_m)
    elif str[i]=="n":
      chr_n=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==1 and (row!=0 and row!=1)) or (row==3 and (col>2 and col<5)) or (col==5 and row>3):
            chr_n[row][col]="#"
      l1.append(chr_n)
    elif str[i]=="o":
      chr_o=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if ((row==2 or row==6) and (col>1 and col<5)) or ((col==1 or col==5) and (row>2 and row<6)):
            chr_o[row][col]="#"
      l1.append(chr_o)
    elif str[i]=="p":
      chr_p=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==0) or ((row==0 or row==3) and (col!=0 and col!=5 and col!=1 and col!=2 and col!=6)) or (col==5 and (row>0 and row<3)) or (col==1 and (row>0 and row<3)):
            chr_p[row][col]="#"
      l1.append(chr_p)
    elif str[i]=="q":
      chr_q=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==4) or ((row==0 or row==3) and (col>1 and col<5)) or (col==1 and (row>0 and row<3)) or (row==5 and (col<6 and col>4)) or (row==4 and col>5):
            chr_q[row][col]="#"
      l1.append(chr_q)
    elif str[i]=="r":
      chr_r=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==2 and row>1) or (row==3 and (col>1 and col<6)) or (row==4 and (col>5)):
            chr_r[row][col]="#"
      l1.append(chr_r)
    elif str[i]=="s":
      chr_s=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if ((row==2 or row==4 or row==6) and (col>1 and col<4)) or ((row==3) and (col!=0 and col!=2 and col!=3 and col!=4 and col!=5 and col!=6 )) or (row==5 and (col!=0 and col!=2 and col!=3 and col!=5 and col!=1 and col!=6)):
            chr_s[row][col]="#"
      l1.append(chr_s)
    elif str[i]=="t":
      chr_t=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==2) or (row==3 and col!=2) or (row==6 and (col>2 and col<5)) or (row==5 and (col>4 and col<6)):
            chr_t[row][col]="#"
      l1.append(chr_t)
    elif str[i]=="u":
      chr_u=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if((col==1 or col==5) and (row>1 and row<6)) or (row==6 and (col>1 and col<5)):
            chr_u[row][col]="#"
      l1.append(chr_u)
    elif str[i]=="v":
      chr_v=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if ((col==1 or col==5) and (row>1 and row<5) ) or (row==5 and (col!=0 and col!=1 and col!=3 and col!=5 and col!=6)) or (row==6 and (col>2 and col<4)):
            chr_v[row][col]="#"
      l1.append(chr_v)
    elif str[i]=="w":
      chr_w=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if ((col==0 or col==6) and (row>1)) or (row==5 and (col!=0 and col!=2 and col!=3 and col!=4 and col!=6)) or (row==4 and (col!=0 and col!=2 and col!=1 and col!=5 and col!=4 and col!=6)):
            chr_w[row][col]="#"
      l1.append(chr_w)
    elif str[i]=="x":
      chr_x=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (row-col==1 and (row!=1)) or (col+row==7 and (row!=1)):
            chr_x[row][col]="#"
      l1.append(chr_x)
    elif str[i]=="y":
      chr_y=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (row+col==7 and row!=1) or (row-col==1 and (row>1 and row<5)):
            chr_y[row][col]="#"
      l1.append(chr_y)
    elif str[i]=="z":
      chr_z=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if ((row==2 or row==6) and (col>0 and col<6)) or (col+row==7 and (row>2 and row<6)):
            chr_z[row][col]="#"
      l1.append(chr_z)
    elif str[i]=="0":
      chr_0=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if ((col==0 or col==6) and (row!=0 and row!=1 and row!=5 and row!=6)) or ((row==0 or row==6) and (col>1 and col<5)) or (col==1 and (row!=0 and row!=1 and row!=2 and row!=3 and row!=4 and row!=6)) or (col==5 and (row!=0 and row!=2 and row!=3 and row!=4 and row!=5 and row!=6)) or (col==1 and (row!=0 and row!=2 and row!=3 and row!=4 and row!=5 and row!=6)) or (col==5 and (row!=0 and row!=1 and row!=2 and row!=3 and row!=4 and row!=6)) or (col==2 and (row!=0 and row!=1 and row!=3 and row!=4 and row!=5 and row!=6)) or (col==3 and (row!=0 and row!=1 and row!=2 and row!=4 and row!=5 and row!=6)) or (col==4 and (row!=0 and row!=1 and row!=2 and row!=3 and row!=5 and row!=6)):
            chr_0[row][col]="#"
      l1.append(chr_0)
    elif str[i]=="1":
      chr_1=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (row==6 and (col!=5 and col!=6)) or (col==2 and row!=6) or (row==1 and (col!=0 and col!=2 and col!=3 and col!=4 and col!=5 and col!=6)) or (row==2 and (col!=1 and col!=2 and col!=3 and col!=4 and col!=5 and col!=6)):
            chr_1[row][col]="#"
      l1.append(chr_1)
    elif str[i]=="2":
      chr_2=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if row==6 or ((row==0 or row==3) and (col>0 and col<6)) or (col==0 and (row!=0 and row!=2 and row!=3 and row!=6)) or (col==6 and (row!=0 and row!=3 and row!=4 and row!=5 and row!=6)):
            chr_2[row][col]="#"
      l1.append(chr_2)
    elif str[i]=="3":
      chr_3=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==4 and (row!=0 and row!=6)) or ((row==0 or row==3 or row==6) and (col<4)):
            chr_3[row][col]="#"
      l1.append(chr_3)
    elif str[i]=="4":
      chr_4=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if row==4 or (col==4 and row!=4) or (row==3 and (col!=0 and col!=2 and col!=3 and col!=4 and col!=5 and col!=6)) or (row==2 and (col!=0 and col!=1 and col!=3 and col!=4 and col!=5 and col!=6)) or (row==1 and (col!=0 and col!=2 and col!=1 and col!=4 and col!=6 and col!=5)) :
            chr_4[row][col]="#"
      l1.append(chr_4)
    elif str[i]=="5":
      chr_5=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if ((row==0 or row==3 or row==6) and (col!=5 and col!=6)) or (col==0 and (row>0 and row<3)) or ((col==4) and (row>3 and row<6)):
            chr_5[row][col]="#"
      l1.append(chr_5)
    elif str[i]=="6":
      chr_6=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==0 and (row>0 and row<6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)) or ((col==4 and (row>2 and row<6))):
            chr_6[row][col]="#"
      l1.append(chr_6)
    elif str[i]=="7":
      chr_7=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if col==6 or (row==0 and col!=6):
            chr_7[row][col]="#"
      l1.append(chr_7)
    elif str[i]=="8":
      chr_8=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if ((col==0 or col==4) and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):
            chr_8[row][col]="#"
      l1.append(chr_8)
    elif str[i]=="9":
      chr_9=[[" " for i in range(7)] for j in range(7)]
      for row in range(7):
        for col in range(7):
          if (col==5 and (row!=0 and row!=6)) or ((row==0 or row==3 or row==6) and (col!=0 and col!=1 and col!=5 and col!=6)) or (col==1 and (row>0 and row<3)) :
            chr_9[row][col]="#"
      l1.append(chr_9)
    else:
      print("Invalid character")
  return l1
str= input("Enter a characteristics:")
l1=[]
l2=Chart()
for i in range(7):
  for j in range(len(l2)):
    for k in range(7):
      print(l2[j][i][k],end="")
    print(end="  ")
  print()

